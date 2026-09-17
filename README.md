# Coc-Bot

A computer-vision automation bot for a desktop game client, written in Python.

I built this to learn screen automation properly — template matching against a
live window, OCR for reading on-screen numbers, and a state machine robust
enough to recover when the game hangs or disconnects.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)

## How it works

The bot never reads game memory or touches the network. It works purely from
what is on screen:

- **Window capture** — `pygetwindow` and `win32gui` locate and focus the client
  window, `PIL.ImageGrab` grabs frames
- **Template matching** — each UI element the bot needs (buttons, dialogs,
  screens) is stored as a reference PNG and located with `pyautogui`'s
  OpenCV-backed matcher, so the bot adapts to window position
- **OCR** — PaddleOCR reads resource counts and numeric state that has no
  template
- **Recovery** — a watchdog detects the loading screen, a black screen or a
  dropped session and walks the client back to a known state

## Modules

| File | Responsibility |
|---|---|
| `XpIncrease.py` | Main loop — the upgrade and XP routine |
| `clain_join.py` | Clan join and reward-claim flow |
| `check_to_reload_game.py` | Watchdog for hung or closed clients |
| `coordinate.py` | Screen coordinate helpers |
| `remove.py` | Reference-image maintenance |

Reference images live alongside the code and are matched by filename.

## Requirements

Windows, with the game client running at a consistent resolution.

```bash
pip install pyautogui pygetwindow pywin32 pillow numpy paddleocr pynput
python XpIncrease.py
```

## Note

Built as a computer-vision exercise. Automating a game client generally
violates its terms of service — run it against your own account only, and
understand that doing so may get that account banned.

## License

MIT — see [LICENSE](LICENSE).
