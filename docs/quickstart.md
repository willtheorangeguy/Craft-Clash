# CraftClash — Quickstart

## Run it

```bash
git clone https://github.com/willtheorangeguy/Craft-Clash
cd Craft-Clash
python main.py
```

Nothing to install — Tkinter ships with Python.

**Use `python main.py`, not the `craftclash` command.** The installed console script builds the
window and returns without starting the event loop, so it exits immediately. See
[`internal/known-issues.md`](./internal/known-issues.md).

## What you get

A window titled *CraftClash - Windows - 0.0.4 BETA* with the logo and three buttons.

| Button | Does |
|---|---|
| **Play!** | **Quits the program.** Not implemented — see below |
| **Options** | Opens the settings screen |
| **About** | Opens the project information screen |

## Play does not work

It is wired to `exit`. The play screen exists as `craftclash/playscreen.old.py`, renamed out of
the import path, and there is no game loop anywhere in the codebase.

Earlier documentation said the button "launches you into your world". It does not, and pressing
it loses whatever you had open. Recorded in
[`internal/known-issues.md`](./internal/known-issues.md).

## Options

- **Sound volume** and **music volume** sliders
- **In-game name**
- **Difficulty**

Nothing consumes these yet, because nothing plays. They persist for whenever it does.

## About

Renders the project's licences and internal details in-app — the GPL text included, which is why
`aboutscreen.py` is over a thousand lines.

Worth a look if you are wondering what a Tkinter app looks like with no external dependencies at
all.

## Run the tests

```bash
pip install -r requirements.txt
pytest
```

`craftclash()` returns the window **without** calling `mainloop()`, precisely so a test can build
and inspect it. That is a deliberate design choice — and the reason the console entry point is
broken, since it calls the same function and never starts the loop.
