"""Game space: the screen as the bot sees it, for any window size or aspect ratio.

Templates, click points and read regions are measured on the profile's base
screen (1920x1080 by default). Clash of Clans scales its interface uniformly
(by the smaller of width/1920 and height/1080) and pins buttons to the screen
edges, while the village stays centred. So the bot:

  1. scales the device image uniformly so it is 1080 tall (or 1920 wide),
     giving a game space of e.g. 1920x1080, 2400x1080 (phone) or 1920x1200 (16:10);
  2. moves edge-pinned coordinates by the extra width/height: things in the left
     third stay, the right third moves right, the middle moves half;
  3. keeps battlefield points (deploy positions) centred.

With a 16:9 device all of this is the identity, so nothing changes there.

Clash of Clans on Android draws its interface bigger than on Google Play Games (BlueStacks:
1.2x at any resolution or DPI). The device's `ui_scale` shrinks its picture by that much first,
so a 1920x1080 BlueStacks becomes a 1600x900 game space in which the PC pictures fit. The
village does not grow as much, so battlefield points and lengths are scaled by the device's
`field_scale` (the village at full zoom-out in game space, relative to the PC's).
"""

import logging

from .profile import profile

log = logging.getLogger("bot")


class Space:
    def __init__(self):
        self.native = None          # (w, h) of the device in its own pixels
        self.scale = 1.0            # native pixels per game-space pixel
        self.field = 1.0            # battlefield size in game space relative to the base screen
        self.w, self.h = profile.size

    @property
    def base(self):
        return profile.size

    def update(self, native_w, native_h, ui_scale=1.0, field_scale=1.0):
        bw, bh = self.base
        s = min(native_w / bw, native_h / bh) * ui_scale
        w, h = round(native_w / s), round(native_h / s)
        if (native_w, native_h, ui_scale, field_scale) != self.native:
            self.native = (native_w, native_h, ui_scale, field_scale)
            self.scale, self.w, self.h, self.field = s, w, h, field_scale
            log.info("Game screen %dx%d (aspect %.2f, interface x%.2f, village x%.2f) -> game space %dx%d, "
                     "scale %.3f", native_w, native_h, native_w / native_h, ui_scale, field_scale, w, h, s)
            if abs(native_w / native_h - bw / bh) > 0.02:
                log.info("The aspect ratio differs from the %dx%d profile; buttons are mapped by screen "
                         "edge. If something is not found, re-capture it in the Templates tab.", bw, bh)
        return w, h

    @property
    def dx(self):
        return self.w - self.base[0]

    @property
    def dy(self):
        return self.h - self.base[1]

    def s(self, length):
        """A length measured on the base screen (button size, offset from a button) in game space.
        The interface is drawn at the profile's size, so lengths do not change."""
        return int(round(length))

    # --- base -> game space ----------------------------------------------------------
    def _ax(self, x, ref=None):
        ref = x if ref is None else ref
        bw = self.base[0]
        if ref < bw / 3:
            return x
        if ref > 2 * bw / 3:
            return x + self.dx
        return x + self.dx / 2

    def _ay(self, y, ref=None):
        ref = y if ref is None else ref
        bh = self.base[1]
        if ref < bh / 3:
            return y
        if ref > 2 * bh / 3:
            return y + self.dy
        return y + self.dy / 2

    def point(self, x, y):
        """A UI point measured on the base screen, pinned to its nearest edge."""
        return round(self._ax(x)), round(self._ay(y))

    def region(self, x, y, w, h):
        """A UI region measured on the base screen, pinned by its centre."""
        cx, cy = x + w / 2, y + h / 2
        return round(self._ax(x, cx)), round(self._ay(y, cy)), int(w), int(h)

    def center(self, x, y):
        """A battlefield/village point: stays centred (and scaled with the battlefield)."""
        bw, bh = self.base
        return round(self.w / 2 + (x - bw / 2) * self.field), round(self.h / 2 + (y - bh / 2) * self.field)

    def f(self, length):
        """A battlefield length measured on the base screen at full zoom-out, in game space."""
        return length * self.field

    # --- game space -> base (when saving captures) ---------------------------------------
    def region_to_base(self, x, y, w, h):
        if self.dx == 0 and self.dy == 0:
            return [int(x), int(y), int(w), int(h)]
        bw, bh = self.base
        cx, cy = x + w / 2, y + h / 2
        # undo the shift that region() would apply for a region at this place; the thirds meet halfway
        # between where region() puts them (they overlap when the game space is smaller than the base)
        fx = 0 if cx < bw / 3 + self.dx / 4 else (1 if cx > 2 * bw / 3 + 3 * self.dx / 4 else 0.5)
        fy = 0 if cy < bh / 3 + self.dy / 4 else (1 if cy > 2 * bh / 3 + 3 * self.dy / 4 else 0.5)
        return [int(round(x - fx * self.dx)), int(round(y - fy * self.dy)), int(w), int(h)]


space = Space()
