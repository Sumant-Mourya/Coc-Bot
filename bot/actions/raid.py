"""Clan Capital Raid Weekend: every account uses its raid attacks on the enemy's Clan Capital.

Raid Weekend runs from Friday 07:00 to Monday 07:00 UTC (12:30 India time). An account has 5 raid
attacks (6 with the bonus); how many are left shows as a red badge ("5 ⚔") over the Clan Capital
airship by the river, and over the Raid Map / Raid Info button. One account:
  zoom out, the airship -> the clan's Clan Capital -> army: delete it, then Super Miners only, 1 Frost
  and 2 Graveyard, Save -> Raid Map -> the first district from the top that is not destroyed yet (it
  is attacked again until it is; the last four after swiping the map up; Capital Peak once it opens)
  -> Attack -> zoom out and pan fully down and right: the deploy strip along the district's lower-right
  side is then always at the same place -> the miners on one spot of it (more taps along the strip as
  backup), the spells on the same spot -> the battle ends -> Map: the raid map again, until no raid
  attack is left.
"""

import datetime as dt
import difflib
import logging
import re
import time

import cv2
import numpy as np

from .. import config, states
from ..core import vision
from ..core.context import BotError
from ..core.control import control
from ..core.space import space
from ..states import go_home

log = logging.getLogger("bot")

UTC = dt.timezone.utc
START = (4, 7)                     # Friday (weekday 4) 07:00 UTC
LENGTH = dt.timedelta(days=3)      # to Monday 07:00 UTC

# the districts in the order they are attacked: from the top of the raid map down. The last four are on
# screen after swiping the map up; Capital Peak opens when all the others are destroyed.
ORDER = ["Barbarian Camp", "Wizard Valley", "Dragon Cliffs", "Balloon Lagoon", "Builder's Workshop",
         "Golem Quarry", "Goblin Mines", "Skeleton Park", "Capital Peak"]
LOW = ("Builder's Workshop", "Golem Quarry", "Goblin Mines", "Skeleton Park")
LABEL_TO_HALL = 78                 # a district's hall is this far under its name label (battlefield px)
BAR_ATTACK = (1045, 960, 120, 35)  # the district bar's Attack button (red = can attack, grey = no attack left)
NOTICE = (470, 220, 990, 120)      # the game's red notice at the top of the raid map
DIALOGS = ("raid/attack_now_title", "raid/attack_go")   # centred popups: looked for on the whole screen

# the capital army: (card in Change Capital Army, taps) - as many Super Miners as fit, 1 Frost, 2 Graveyard
ARMY = [("raid/unit_super_miner", 12), ("raid/spell_frost", 1), ("raid/spell_graveyard", 2)]

# In a raid battle, zoomed out and panned fully down and right (the finger goes up and left), the deploy
# strip along the district's lower-right side is on screen: everything is dropped on one spot of it
# (battlefield points; on BlueStacks 1920x1080 the spot is at 560, 650 - all 10 miners went down there on
# Barbarian Camp). Taps that do not deploy are made again along the strip, the nearest spots first.
PAN = ((1466, 784), (623, 268))
DEPLOY = (586, 643)
BACKUP = [(-36, 22), (36, -22), (10, 16), (-10, -16), (-103, 64), (103, -64), (-183, 113), (183, -113)]
BATTLE_CARDS = [("raid/battle_miner", 10), ("raid/battle_frost", 1), ("raid/battle_graveyard", 2)]


def window(now=None):
    """(active, start, end) of the current Raid Weekend, or of the next one when none is on."""
    now = now or dt.datetime.now(UTC)
    day, hour = START
    start = (now - dt.timedelta(days=(now.weekday() - day) % 7)).replace(hour=hour, minute=0, second=0,
                                                                         microsecond=0)
    if start > now:
        start -= dt.timedelta(days=7)
    end = start + LENGTH
    if now < end:
        return True, start, end
    start += dt.timedelta(days=7)
    return False, start, start + LENGTH


def weekend_key(start):
    return start.strftime("%Y-%m-%d")


def _done(bot):
    """{account: "done" | n attacks used} of the current Raid Weekend (kept in the bot's state)."""
    active, start, _ = window()
    if bot.state is None:
        return {}
    slot = bot.state.setdefault("raid", {})
    for k in [k for k in slot if k != weekend_key(start)]:
        slot.pop(k)                                      # an older weekend
    return slot.setdefault(weekend_key(start), {})


def pending(bot, names):
    """The accounts that still have raid attacks this weekend (as far as the bot knows)."""
    done = _done(bot)
    return [n for n in names if done.get(n) != "done"]


def _save_state(bot):
    if bot.state is not None:
        config.save_state(bot.state)


# ----------------------------------------------------------------------------- the village
def _badges(frame):
    """Red badges like the airship's "5 ⚔" (a rounded red box): [(x, y, w, h)]. The badge hangs over the
    village, so its size goes with the village's (and a little with how far the pinch zoomed out)."""
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    m = (((hsv[:, :, 0] < 7) | (hsv[:, :, 0] > 173)) & (hsv[:, :, 1] > 150) & (hsv[:, :, 2] > 140)).astype(np.uint8)
    n, _, st, _ = cv2.connectedComponentsWithStats(m)
    out = []
    for i in range(1, n):
        x, y, w, h, a = st[i]
        if space.f(44) <= w <= space.f(80) and space.f(32) <= h <= space.f(56) and a / (w * h) > 0.6 \
                and space.s(200) < y < space.s(1000) and space.s(150) < x < space.s(1500):
            out.append((int(x), int(y), int(w), int(h)))
    return out


def _digits(text):
    """The number in a short OCR'd text, with the usual letter/digit mix-ups fixed (or None)."""
    for a, b in (("S", "5"), ("s", "5"), ("l", "1"), ("I", "1"), ("O", "0"), ("o", "0")):
        text = text.replace(a, b)
    digits = re.sub(r"\D", "", text)
    return int(digits) if digits else None


def find_airship(bot):
    """Zoom out and bring the river into view: the airship's badge (x, y, w, h) and the raid attacks
    left it shows, or (None, 0) when there is no badge (no raid attack left). The badge is found by its
    colour and shape (the same in every village scenery - the airship itself looks different in each),
    looked for twice before deciding there is none."""
    found = []
    for attempt in range(2):
        go_home(bot, 30)
        bot.device.zoom_out()
        control.sleep(0.6)
        bot.swipe(space.center(900, 800), space.center(1100, 350 + 120 * attempt), 700)
        control.sleep(1.2)
        f = bot.shot()
        found = _badges(f)
        if found:
            break
    if not found:
        return None, 0
    x, y, w, h = max(found, key=lambda b: b[1])          # the lowest one: the airship is by the river
    text, conf = vision.text_reader.read_line(f, (x + space.s(4), y + space.s(2), w // 2, h - space.s(6)))
    left = _digits(text)
    return (x, y, w, h), (left if left and left <= 6 else 1)


# ----------------------------------------------------------------------------- the Capital
def _find(frame, key):
    if key in DIALOGS:
        return vision.find(frame, key, region=(0, 0, frame.shape[1], frame.shape[0]))
    return vision.find(frame, key)


def _wait_any(bot, keys, timeout):
    end = time.monotonic() + timeout
    while time.monotonic() < end:
        f = bot.shot()
        for k in keys:
            if vision.templates.has(k) and _find(f, k):
                return k
        control.sleep(0.5)
    return None


def _red_share(frame, region):
    """How much of a game-space region is bright red (badges, the Attack button)."""
    x, y, w, h = region
    p = cv2.cvtColor(frame[max(0, y):y + h, max(0, x):x + w], cv2.COLOR_BGR2HSV).reshape(-1, 3).astype(int)
    if not len(p):
        return 0.0
    return float((((p[:, 0] < 8) | (p[:, 0] > 172)) & (p[:, 1] > 120) & (p[:, 2] > 120)).mean())


def _red(frame, box):
    return _red_share(frame, space.region(*box)) > 0.3


def open_capital(bot, badge):
    """Tap the airship (under its badge). Returns the screen that opened: the clan's own Clan Capital
    ("raid/capital_title"), the raid map ("raid/attacking_title"), the summary of the last raid
    ("raid/next_raid") or None."""
    x, y, w, h = badge
    bot.tap(x + w // 2, y + h + space.s(75), jitter=3)
    return _wait_any(bot, ["raid/capital_title", "raid/attacking_title", "raid/next_raid"], 25)


def attacks_left(frame):
    """Raid attacks left: the number on the red badge over Raid Map / Raid Info (bottom right); 0 when
    there is no badge, None when neither button is on screen."""
    m = vision.find(frame, "raid/raid_map") or vision.find(frame, "raid/raid_info")
    if not m:
        return None
    if _red_share(frame, (m.x - space.s(70), m.y - space.s(165), space.s(140), space.s(55))) < 0.3:
        return 0
    text, _ = vision.text_reader.read_line(frame, (m.x - space.s(45), m.y - space.s(160), space.s(50),
                                                   space.s(45)))
    left = _digits(text)
    return left if left and left <= 6 else 1


def _card(frame, key):
    """A card that can still be used: found, and in colour - a full army greys the cards of the unit list,
    and a used-up card of the battle bar turns grey (grey ~10, the pale Frost card ~58)."""
    m = vision.find(frame, key)
    if not m:
        return None
    x, y, w, h = m.box
    return m if cv2.cvtColor(frame[y:y + h, x:x + w], cv2.COLOR_BGR2HSV)[:, :, 1].mean() > 30 else None


def set_army(bot):
    """Change Capital Army (the button bottom left of the Capital and of the raid map): delete the army,
    then Super Miners only (as many as fit), 1 Frost and 2 Graveyard, Save. True when it was saved; when
    a card is missing the window is cancelled and the army stays as it was."""
    if not bot.tap_template("raid/army_button", timeout=5):
        return False
    title = bot.wait("raid/army_title", 8)
    if not title:
        return False
    if bot.find("raid/army_trash"):                          # red while the army has units
        bot.tap_template("raid/army_trash", timeout=2, after=0.8)
    row = title.y + space.s(610)                             # the unit list, under the buttons
    for _ in range(2):         # it starts with Super Barbarian: the Super Miner and the spells are at its end
        bot.swipe((title.x + space.s(450), row), (title.x - space.s(450), row), 600)
        control.sleep(0.6)
    for key, taps in ARMY:
        m = _card(bot.shot(), key)
        if not m:
            log.warning("Raid army: no %s to add (not unlocked in this clan?) - the army is left as it was",
                        key.split("/")[1].replace("_", " "))
            bot.save_error("raid-army")
            bot.tap(title.x + space.s(30), title.y + space.s(331), jitter=3)    # Cancel
            bot.wait_gone("raid/army_title", 5)
            return False
        bot.tap(m.x, m.y, jitter=4, times=taps, interval=0.25)
        control.sleep(0.4)
    bot.tap_template("raid/army_save", timeout=3)
    return bot.wait_gone("raid/army_title", 6)


def open_raid_map(bot):
    """From the clan's Clan Capital to the raid map (past the summary of the last raid). True when it is
    on screen."""
    if not bot.tap_template("raid/raid_map", timeout=3):
        return False
    key = _wait_any(bot, ["raid/attacking_title", "raid/next_raid"], 15)
    if key == "raid/next_raid":
        bot.tap_template("raid/next_raid", timeout=3)
        key = _wait_any(bot, ["raid/attacking_title"], 15)
    return key == "raid/attacking_title"


# ----------------------------------------------------------------------------- the raid map
def _norm(text):
    return re.sub(r"[^a-z]", "", text.lower())


def _name_of(text):
    """The district a label reads as (OCR mix-ups allowed), or None."""
    t = _norm(text)
    if len(t) < 5:
        return None
    ratio, name = max((difflib.SequenceMatcher(None, t, _norm(n)).ratio(), n) for n in ORDER)
    return name if ratio >= 0.75 else None


def _tappable(x, y):
    """On screen and not under the raid map's buttons (Map and army bottom left, Raid Info bottom right)."""
    if not (0 < x < space.w and 0 < y < space.h - space.s(40)):
        return False
    return not (y > space.h - space.s(240) and (x < space.s(340) or x > space.w - space.s(340)))


def read_map(frame):
    """The districts on screen: {name: {"hall": (x, y) to tap, or None when off screen / under a button,
    "pct": destruction % or None, "locked": bool}}, from their name labels and the "0%" / "Locked" over
    them."""
    # only where district labels can be: not the clan name, timer and buttons along the edges (faster)
    texts = vision.text_reader.read(frame, (space.s(300), space.s(140), space.w - space.s(600),
                                            space.h - space.s(140)))
    out = {}
    for text, _, (x, y, w, h) in texts:
        name = _name_of(text)
        if not name or name in out:
            continue
        above = [t for t, _, (tx, ty, tw, th) in texts if y - space.s(50) <= ty < y and tx < x + w and tx + tw > x]
        pct = next((_digits(t[:t.index("%")]) for t in above if "%" in t and _digits(t[:t.index("%")]) is not None),
                   None)
        hall = (x + w // 2, y + h + int(space.f(LABEL_TO_HALL)))
        out[name] = {"hall": hall if _tappable(*hall) else None, "pct": pct,
                     "locked": any("lock" in t.lower() for t in above)}
    return out


def _scroll(bot, down):
    """Swipe the raid map to its bottom (the finger goes up: the last four districts) or back to its top."""
    a, b = space.center(960, 880), space.center(960, 230)
    for _ in range(2):
        bot.swipe(a if down else b, b if down else a, 600)
        control.sleep(0.5)
    control.sleep(0.8)


def _close_bar(bot):
    bot.tap(*space.center(1650, 400), jitter=3)
    control.sleep(0.6)


def _bar_name(frame, bar):
    """The district named on the bar under a tapped district (bar = its Scout button)."""
    text, _ = vision.text_reader.read_line(frame, (bar.x - space.s(365), bar.y + space.s(8), space.s(245),
                                                   space.s(42)))
    return _name_of(text)


def choose_district(bot):
    """Tap the first district from the top that can still be attacked. Returns its name with its bar open
    (Attack is red), or None when no district can be attacked now."""
    _scroll(bot, down=False)
    view, seen = "top", None
    for name in ORDER:
        control.checkpoint()
        want = "low" if name in LOW else "top"
        if want != view:
            _scroll(bot, down=want == "low")
            view, seen = want, None
        if seen is None:
            seen = read_map(bot.shot())
        d = seen.get(name)
        if d is None or not d["hall"] or d["locked"] or (d["pct"] or 0) >= 100:
            continue                                     # not read, locked or destroyed
        bot.tap(*d["hall"], jitter=4)
        control.sleep(1.0)
        f = bot.shot()
        bar = vision.find(f, "raid/district_bar")
        if not bar:
            continue
        on_bar = _bar_name(f, bar)
        if on_bar != name or not _red(f, BAR_ATTACK):
            log.info("Raid: %s cannot be attacked (%s)", name,
                     f"the tap opened {on_bar}" if on_bar != name else "destroyed, or no raid attack left")
            _close_bar(bot)
            continue
        log.info("Raid: next district %s (%s%% destroyed)", name, d["pct"] if d["pct"] is not None else "?")
        return name
    return None


# ----------------------------------------------------------------------------- the battle
def _not_allowed(frame):
    """The game's notice "Only members who were in the clan before the Raid Weekend began can attack!"
    (an account that joined the clan during the weekend; Elders and up can attack anyway)."""
    x, y, w, h = space.region(*NOTICE)
    p = cv2.cvtColor(frame[y:y + h, x:x + w], cv2.COLOR_BGR2HSV).reshape(-1, 3).astype(int)
    if float((((p[:, 0] < 8) | (p[:, 0] > 172)) & (p[:, 1] > 170) & (p[:, 2] > 170)).mean()) < 0.02:
        return False
    text = re.sub(r"[^a-z]", "", " ".join(t for t, _, _ in vision.text_reader.read(frame, (x, y, w, h))).lower())
    return "before" in text and "raid" in text or "onlymembers" in text


def _wait_battle(bot, timeout):
    """Wait for the raid battle; returns "battle", "not_allowed" or None."""
    end = time.monotonic() + timeout
    while time.monotonic() < end:
        f = bot.shot()
        if vision.find(f, "raid/battle_starts") or vision.find(f, "battle/surrender"):
            return "battle"
        if _not_allowed(f):
            return "not_allowed"
        control.sleep(0.4)
    return None


def start_attack(bot):
    """The district's bar is open: Attack (-> "Attack Now?" Attack) until the battle has started.
    Returns "started", "not_allowed" or "failed"."""
    x0, y0, w0, h0 = space.region(*BAR_ATTACK)
    key = None
    for _ in range(3):                               # a tap while the bar slides in is lost: again
        bot.tap(x0 + w0 // 2, y0 + h0 // 2, jitter=3)
        key = _wait_any(bot, ["raid/attack_now_title", "raid/battle_starts", "battle/surrender"], 5)
        if key:
            break
    for _ in range(3):
        if key != "raid/attack_now_title":
            break
        m = _find(bot.shot(), "raid/attack_go")
        if m:
            bot.tap_match(m)
        got = _wait_battle(bot, 8)
        if got == "not_allowed":
            return "not_allowed"
        key = "raid/battle_starts" if got == "battle" else _wait_any(bot, ["raid/attack_now_title"], 1)
    if key in ("raid/battle_starts", "battle/surrender"):
        return "started"
    bot.save_error("raid-no-battle")
    return "failed"


def deploy(bot):
    """In the raid battle: zoom out, pan fully down and right, then each card of the army on the deploy
    spot - the Super Miners first. While a card still has something left (a tap that did not deploy, or a
    bigger army), one more tap at a time along the strip."""
    bot.device.zoom_out()
    control.sleep(0.5)
    for _ in range(4):
        bot.swipe(space.center(*PAN[0]), space.center(*PAN[1]), 500)
        control.sleep(0.3)
    control.sleep(0.8)
    spot = space.center(*DEPLOY)
    backup = [(spot[0] + int(space.f(dx)), spot[1] + int(space.f(dy))) for dx, dy in BACKUP]
    for key, taps in BATTLE_CARDS:
        control.checkpoint()
        card = _card(bot.shot(), key)
        if not card:
            log.info("Raid: no %s to deploy", key.split("_", 1)[1])
            continue
        bot.tap_match(card)
        control.sleep(0.3)
        bot.tap(*spot, jitter=2, times=taps, interval=0.2)
        for x, y in backup * 2:
            control.sleep(0.4)
            if not _card(bot.shot(), key):
                break
            bot.tap(x, y, jitter=2)
        else:
            log.warning("Raid: some %s could not be deployed on the strip", key.split("_", 1)[1])
            bot.save_error("raid-deploy")
        control.sleep(0.4)


def finish_battle(bot, timeout=240):
    """Wait until the raid battle is over and the raid map is back. True when it is."""
    end = time.monotonic() + timeout
    while time.monotonic() < end:
        f = bot.shot()
        if _find(f, "raid/attacking_title"):
            return True
        for k in ("raid/battle_end", "raid/return_map"):
            m = vision.templates.has(k) and _find(f, k)
            if m:
                bot.tap_match(m)
                control.sleep(1.5)
                break
        control.sleep(1.0)
    bot.save_error("raid-battle-end")
    return False


def restart(bot):
    """Close the game and open it again (to get out of a screen the bot does not know)."""
    bot.device.close_game()
    end = time.monotonic() + 20
    while bot.device.is_game_running() and time.monotonic() < end:
        control.sleep(0.5)
    control.sleep(1.0)
    states.ensure_game(bot)


def leave(bot):
    """From the raid map back to the village: Map -> the Clan Capital -> Return Home (else restart)."""
    for key in ("raid/map_button", "raid/return_home"):
        if not bot.tap_template(key, timeout=8, after=2.0):
            break
    if not go_home(bot, 30):
        restart(bot)


# ----------------------------------------------------------------------------- one account
def run(bot, account, max_attacks=6):
    """Use this account's raid attacks. Returns the number of raid attacks made."""
    active, _, _ = window()
    if not active:
        return 0
    name = account["name"]
    done = _done(bot)
    if done.get(name) == "done":
        return 0
    badge, left = find_airship(bot)
    if badge is None:
        log.info("%s: no raid attack left this Raid Weekend", name)
        done[name] = "done"
        _save_state(bot)
        return 0
    screen = open_capital(bot, badge)
    if screen == "raid/next_raid":                   # the summary of the last raid: Next Raid
        bot.tap_template("raid/next_raid", timeout=3)
        screen = _wait_any(bot, ["raid/attacking_title"], 15)
    if screen is None:
        log.info("%s: the Clan Capital did not open (a game tutorial still pending?) - skipped this Raid "
                 "Weekend", name)
        bot.save_error("raid-no-capital")
        done[name] = "done"                          # not tried again and again this weekend
        _save_state(bot)
        restart(bot)
        return 0
    left = attacks_left(bot.shot())
    if left == 0:
        log.info("%s: no raid attack left this Raid Weekend", name)
        done[name] = "done"
        _save_state(bot)
        leave(bot)
        return 0
    log.info("%s: %s raid attack(s) left - setting the army: Super Miners, 1 Frost, 2 Graveyard", name, left)
    bot.status(account=name, action="Raid: setting the army")
    if not set_army(bot):
        log.warning("%s: the capital army was not changed - attacking with the army it has", name)
    if screen != "raid/attacking_title" and not open_raid_map(bot):
        log.info("%s: the raid map did not open", name)
        bot.save_error("raid-no-map")
        leave(bot)
        return 0
    made, failed = 0, 0
    while made < max_attacks:
        control.checkpoint()
        left = attacks_left(bot.shot())
        if left == 0:
            log.info("%s: no raid attack left", name)
            done[name] = "done"
            break
        bot.status(account=name, action=f"Raid attack {made + 1} ({left} left)")
        district = choose_district(bot)
        if district is None:
            if bot.tap_template("raid/next_raid", timeout=2):
                _wait_any(bot, ["raid/attacking_title"], 15)     # this raid is over: on to the next clan
                continue
            log.info("%s: no district can be attacked now", name)
            bot.save_error("raid-no-district")
            break
        status = start_attack(bot)
        if status == "not_allowed":
            log.info("%s: joined the clan after this Raid Weekend began - the game lets it raid only if promoted "
                     "(Elder) or the clan is Invite Only; skipped this weekend", name)
            done[name] = "done"
            break
        if status == "failed":
            failed += 1
            log.info("%s: the raid attack on %s did not start", name, district)
            if failed >= 2:
                break
            _close_bar(bot)
            continue
        log.info("%s: raid attack on %s", name, district)
        deploy(bot)
        made += 1
        bot.stats["raids"] = bot.stats.get("raids", 0) + 1
        _save_state(bot)
        if not finish_battle(bot):
            log.warning("%s: the raid battle did not end on the raid map - restarting the game", name)
            restart(bot)
            break
    _save_state(bot)
    if made:
        log.info("%s: %d raid attack(s) made", name, made)
    leave(bot)
    return made


def raid_accounts(bot, accounts, state, switch, start_from=None):
    """Raid Weekend: every account that still has raid attacks uses them. switch(acc) opens an account.
    start_from: the account to begin with (then the ones after it, then the ones before it)."""
    active, _, end = window()
    if not active:
        return 0
    if start_from is not None:
        i = next((k for k, a in enumerate(accounts) if a["name"] == start_from), 0)
        accounts = accounts[i:] + accounts[:i]
    names = pending(bot, [a["name"] for a in accounts])
    if not names:
        return 0
    left = end - dt.datetime.now(UTC)
    log.info("== Raid Weekend (%dh %dm left): raid attacks on %d account(s)", left.days * 24 + left.seconds // 3600,
             left.seconds % 3600 // 60, len(names))
    total = 0
    for acc in accounts:
        if acc["name"] not in names:
            continue
        control.checkpoint()
        if not window()[0]:
            break
        if not switch(acc):
            continue
        try:
            total += run(bot, acc, (bot.settings.get("steps", {}).get("raid") or {}).get("attacks", 6))
        except BotError as e:
            log.warning("%s: raid: %s", acc["name"], e)
            restart(bot)
    log.info("== Raid Weekend: %d raid attack(s) made", total)
    return total
