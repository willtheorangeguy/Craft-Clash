# CraftClash — Troubleshooting

## `craftclash` runs and nothing happens

The installed console script exits immediately — it calls a function that returns the window
without starting the event loop.

```bash
git clone https://github.com/willtheorangeguy/Craft-Clash
cd Craft-Clash
python main.py
```

Recorded in [`internal/known-issues.md`](./internal/known-issues.md).

## The Play button closed the game

Not a crash. It is wired to `exit`, because the play screen is not finished. Same file.

## `ModuleNotFoundError: No module named 'tkinter'`

Bundled with Python on Windows and macOS; separate on most Linux distributions:

```bash
sudo apt install python3-tk        # Debian, Ubuntu
sudo dnf install python3-tkinter   # Fedora
```

## `TclError: couldn't open ... titlelogo.gif`

The assets directory is missing or incomplete. `main.py` resolves it against its own location,
so this is not a working-directory problem — check `assets/logo/titlelogo.gif` exists in the
clone.

If you installed from PyPI, confirm `MANIFEST.in` packaged the assets in your version.

## `TclError: couldn't recognize data in image file`

An image that is not GIF or PNG. Tkinter's `PhotoImage` reads nothing else without Pillow.

## The window opens with a blank space where the logo should be

Normally this means a `PhotoImage` was garbage-collected — but `main.py` binds it to
`title_label.image` specifically to prevent that. If you see it anyway, the file is likely
present but unreadable rather than missing.

## Closing the About or Options window closed everything

Each screen constructs its own `Tk()` rather than a `Toplevel()`. Multiple `Tk()` roots share one
interpreter, and closing the wrong one can take the others down. See
[Architecture](./architecture.md).

## No sound

There is no audio playback code. `assets/sounds/ambient_1.m4a` exists; nothing plays it, and the
volume sliders are not connected to anything.

## `pytest` collects nothing

Run from the repository root — `pytest.ini`-less projects rely on discovery from the working
directory.

## Tests pass but the app misbehaves

The suite builds the main window and inspects widgets; it does not run the event loop or open the
other screens. A button wired to the wrong callback still passes — which is how the Play button
came to be wired to `exit` with a green test badge.

## The version number is wrong

`0.4.0` in the packaging, `0.0.4 BETA` in the UI. Both are in the repository; neither is a
display bug. Recorded in [`internal/known-issues.md`](./internal/known-issues.md).

## Still stuck

[Open an issue](https://github.com/willtheorangeguy/Craft-Clash/issues/new/choose), or ask on the
[Discord](https://discord.gg/vdaABVxGHf). Include your OS, Python version, and how you launched it.
