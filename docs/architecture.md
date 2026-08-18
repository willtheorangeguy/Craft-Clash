# CraftClash — Architecture

Three Tkinter windows and an assets directory. No engine, no framework, no dependencies.

```
main.py
 └── craftclash()                    builds and returns the main window
      ├── Play!    → exit            not implemented
      ├── Options  → optionsscreen()
      └── About    → aboutscreen()
```

## `main.py`

`craftclash()` builds the window and **returns it without calling `mainloop()`**:

> The window is returned without starting the Tk event loop so that it can be created and
> inspected by tests. Call `mainloop()` on the returned window (see `__main__` below) to actually
> run the game.

That is a deliberate and good testability decision — it is what lets `tests/test_main.py` assert
on the constructed widgets with no display. `if __name__ == "__main__":` supplies the
`mainloop()`.

The console entry point does not, which is why the installed command exits immediately. See
[`internal/known-issues.md`](./internal/known-issues.md).

## Assets

```python
ASSETS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
```

Resolved against the module, not the working directory — so the game runs from anywhere. The
comment says why, and it is worth keeping: a sibling project in this org resolves assets against
the CWD and is unusable once installed.

The title image is also bound to the label:

```python
title_label.image = titleimg
```

Tkinter keeps no Python reference to a `PhotoImage`, so one held only by a local would be
garbage-collected when the function returns — leaving a blank space and no error. The comment
records that too.

Both are the kind of small correctness detail that is invisible when right and baffling when
wrong.

## The screens

**`optionscreen.py`** (105 lines) — sliders for sound and music, an entry for the player name, and
a difficulty control. Opens its own `Tk()` window.

**`aboutscreen.py`** (1,163 lines) — project information and the full licence texts, rendered as
Tkinter labels. Its size is almost entirely the GPL, hardcoded as string literals across several
functions, each opening its own window.

**`playscreen.old.py`** (76 lines) — the play screen, renamed out of the import path. Nothing
imports it, and the `.old` suffix means it is not a module.

## Multiple `Tk()` roots

Each screen constructs its own `Tk()` rather than a `Toplevel()`. Tkinter supports only one true
root per process; additional `Tk()` instances work in practice but share the same interpreter and
event loop, and closing the wrong one can take the others with it.

`Toplevel()` is the intended construct for secondary windows. This is a design observation rather
than a bug — the screens do open and function.

## Testing

`tests/test_main.py` builds the window through `craftclash()` and asserts on its widgets. The
no-`mainloop` return is what makes this possible.

The options and about screens are not tested; both call `Tk()` and `mainloop()` internally.

## What is not here

No game loop, no world model, no save format, no rendering beyond the menus, and no code that
reads `assets/textures/`. The textures and models are ready for a game that has not been written.
