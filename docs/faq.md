# CraftClash — FAQ

### Why does the Play button close the game?

Because it is wired to `exit`. The play screen was never finished —
`craftclash/playscreen.old.py` is the disabled implementation, and there is no game loop
anywhere in the codebase.

Earlier documentation claimed it "launches you into your world". It does not. Recorded in
[`internal/known-issues.md`](./internal/known-issues.md).

### So is there a game?

Not yet. The menus, options, and about screens work. `PLANNING.md` tracks the rest.

### `pip install craftclash` then `craftclash` does nothing.

The console entry point calls a function that returns the window without starting the event
loop, so the process exits immediately. Run `python main.py` from a clone instead. Same
known-issues file.

### Why is it GPL when everything else here is MIT?

A deliberate choice for this project, and the licence explicitly covers the non-code assets too.
Anything derived from CraftClash must also be GPL — worth knowing before borrowing code or art
from it.

### What are the textures?

Original pixel art in `assets/textures/`, drawn with the tools credited in the README (Paint and
Piskel), with Cubik Studio model definitions alongside the fences. Minecraft and Terraria are
credited as **inspirations**, not as sources of assets.

### Why is `aboutscreen.py` over a thousand lines?

It renders the full GPL text as Tkinter labels. The licence is most of the file.

### Why GIF for the logo?

Tkinter's `PhotoImage` reads GIF and PNG only. A JPEG would need Pillow, which would be this
project's first runtime dependency.

### Do the options do anything?

Not yet — they are the interface for gameplay that does not exist. The values are collected;
nothing consumes them.

### Which version is it?

Depends where you look: `0.4.0` in the packaging, `0.0.4 BETA` in the window title and the
copyright label. Recorded in [`internal/known-issues.md`](./internal/known-issues.md).

### Does it save anything?

No. No save file, no config, nothing written to disk. That will have to change when there is a
world.

### Is there a Windows executable?

Yes, attached to [releases](https://github.com/willtheorangeguy/Craft-Clash/releases/latest),
built with PyInstaller from `main.spec`.

### Can I contribute the play screen?

Yes, and it is the work that matters most. See [Development](./development.md) — and note
contributions are GPL.
