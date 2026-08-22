# Known Issues — Craft-Clash

Concrete defects and gaps found while writing this repository's documentation in
August 2026. **Nothing here was changed** — each one needs a code, configuration, or
licensing decision rather than a documentation one.

Ordered by severity. See [`docs/roadmap.md`](../roadmap.md) for the narrative version,
which also covers deliberate non-goals.

**5 open:** 2 high, 2 medium, 1 low.

## 1. The installed console command exits immediately without showing a window

**Severity:** High
**Where:** `setup.py` / `setup.cfg` -> `console_scripts`, `main.py` -> `craftclash`

**What:** Both packaging files declare `craftclash = main:craftclash`. `craftclash()` builds the window and returns it **without** calling `mainloop()` -- deliberately, and documented in its own docstring: 'The window is returned without starting the Tk event loop so that it can be created and inspected by tests. Call `mainloop()` on the returned window (see `__main__` below).' `main.py`'s `if __name__ == "__main__"` block supplies the missing call; the entry point does not.

**Why it matters:** `pip install craftclash && craftclash` -- the route the README, `docs/USAGE.md`, and the PyPI listing all describe -- starts, constructs a window nobody sees, and exits with status 0. There is no error to search for and no traceback, so it reads as the program being broken rather than the packaging. The publish workflow cannot catch it either: it builds and uploads without ever running the installed command, so every release ships this way with a green badge.

**Suggested fix:** Add a thin wrapper and point the entry point at it: `def main(): craftclash().mainloop()`. Do **not** move `mainloop()` inside `craftclash()` -- that would fix the command and break every test, since the test suite depends on getting the window back un-started.

## 2. The Play button is wired to exit, while the documentation says it starts the game

**Severity:** High
**Where:** `main.py` -> `btn_play`; `craftclash/playscreen.old.py`

**What:** `btn_play = Button(window, text="Play!", ..., command=exit)`. The play screen exists as `craftclash/playscreen.old.py` -- renamed out of the import path, imported by nothing -- and there is no game loop anywhere in the codebase. The README's Support section stated: 'The **Play!** button launches you into your world.'

**Why it matters:** The primary action of a game quits it. A new player presses the biggest button on the menu and the program vanishes, which is indistinguishable from a crash -- and the documentation told them it would start a game, so they will report it as one. `exit` is also a blunt instrument: it raises `SystemExit` through Tk's callback, so any other window open at the time goes with it.

**Suggested fix:** Until the play screen is revived, disable the button (`state="disabled"`) or point it at a message saying the game is not implemented -- either is honest. The README now says so; the running program should agree. Reviving it means renaming `playscreen.old.py` into the package and importing it.

## 3. The packaging version and the version shown in the UI disagree

**Severity:** Medium
**Where:** `pyproject.toml`, `setup.py`, `setup.cfg` (0.4.0) vs `main.py` and `craftclash/aboutscreen.py` (0.0.4 BETA)

**What:** All three packaging files declare `0.4.0`. `main.py`'s window title reads `CraftClash - Windows - 0.0.4 BETA` and its copyright label repeats `Version 0.0.4 BETA`; every window title in `aboutscreen.py` carries the same string. The two are not the same number transposed -- 0.4.0 and 0.0.4 are different versions.

**Why it matters:** The version a user can see is the one in the title bar, and it is the one they will quote in a bug report -- against a release that does not exist. `0.0.4` also reads as far earlier in the project's life than `0.4.0`, which misrepresents how finished it is in the opposite direction to everything else. Because the string is hardcoded in many places, a release bump updates the packaging and silently leaves the UI behind.

**Suggested fix:** Read the version once from package metadata (`importlib.metadata.version("craftclash")`) and interpolate it into the titles, so a release bump reaches the UI. Failing that, define it as a single constant and reference it.

## 4. The README logo used a /blob/ URL while the screenshot used raw

**Severity:** Medium
**Where:** `README.md` (fixed in this pass)

**What:** The logo was `https://github.com/willtheorangeguy/Craft-Clash/blob/main/docs/images/logo.png` -- the `/blob/` path serves GitHub's HTML viewer, not image bytes -- while the screenshot immediately below used `raw.githubusercontent.com` and worked. Several links in the How To Use section also omitted `/blob/` entirely (`https://github.com/willtheorangeguy/Craft-Clash/main/README.md#git`) and returned 404.

**Why it matters:** The first thing on the page was a broken image and the second was a working one, which is a worse impression than either alone -- it reads as neglect rather than a mistake. `/blob/` returns HTML to every client, so the logo was broken on github.com, on PyPI, and anywhere else the README is rendered. Having the correct form a few lines below shows the fix was known.

**Suggested fix:** Fixed in this pass: both images now come from `raw.githubusercontent.com/willtheorangeguy/.github/main/icons/Craft-Clash/`, and the self-referential links are relative. This depends on the `.github` repository staying public.

## 5. Each screen creates its own Tk() root instead of a Toplevel()

**Severity:** Low
**Where:** `main.py`, `craftclash/optionscreen.py`, `craftclash/aboutscreen.py`

**What:** `craftclash()` constructs `Tk()`, and so does every function in `optionscreen.py` and `aboutscreen.py` that opens a window -- `aboutscreen.py` alone does it in several places. Tkinter supports one true root per process; `Toplevel()` is the construct for secondary windows.

**Why it matters:** Additional `Tk()` instances work in practice but share one interpreter and event loop, so destroying the wrong one can take the others with it -- closing the About window can close the menu behind it. It also means each screen runs its own `mainloop()`, which is why neither the options nor the about screen can be tested the way `main.py` is: there is no way to build one and get it back without entering a loop.

**Suggested fix:** Pass the parent window down and use `Toplevel(parent)`. Doing so would also let each screen expose a build-and-return function like `craftclash()`, making them testable.

---

## Also, across every repository

**`.bandit` is present on disk but untracked in git.** Verified in PyWorkout, treklogger,
skyscanner-cli, booking-cli, piggy, and aibot — the config file exists locally in each but
`git ls-files` does not know about it, so none of it reached GitHub.

The August 2026 security sweep therefore looks complete locally and landed nowhere. Worth
checking across all 44 repositories it covered.
