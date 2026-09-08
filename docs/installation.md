# CraftClash — Installation

## Requirements

| | |
|---|---|
| Python | 3.x with Tkinter |
| Dependencies | None at runtime |

Tkinter ships with Python on Windows and macOS. On Linux it is usually separate:

```bash
sudo apt install python3-tk        # Debian, Ubuntu
sudo dnf install python3-tkinter   # Fedora
```

## From source — the recommended route

```bash
git clone https://github.com/willtheorangeguy/Craft-Clash
cd Craft-Clash
python main.py
```

Assets are resolved relative to `main.py`, so unlike some of its siblings this works from any
working directory.

## From PyPI — currently broken

```bash
pip install craftclash
craftclash
```

The command installs and runs, and **exits immediately without showing a window**. The entry
point is `main:craftclash`, and that function deliberately returns the window without calling
`mainloop()` so tests can inspect it. Nothing calls `mainloop()` on the way through.

Recorded in [`internal/known-issues.md`](./internal/known-issues.md). Until it is fixed, run from
source.

## Windows executable

A prebuilt launcher is attached to
[releases](https://github.com/willtheorangeguy/Craft-Clash/releases/latest), built with
PyInstaller from `main.spec`. No Python needed.

1. Download and extract the `.zip`.
2. Run `main.exe`.

## Verify

```bash
python main.py
```

A window with the logo and three buttons. If the window appears with a blank space where the logo
should be, see [Troubleshooting](./troubleshooting.md) — that is the Tkinter image-reference
problem, which this codebase already handles, so it would mean something else.

## Tests

```bash
pip install -r requirements.txt
pytest
```

## Uninstall

```bash
pip uninstall craftclash
```

The game writes no save files and no configuration, so nothing is left behind. That will change
when there is a world to save.
