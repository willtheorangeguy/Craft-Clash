# CraftClash — Roadmap

Direction, not a schedule. `PLANNING.md` holds the version checklist; defects are in
[`internal/known-issues.md`](./internal/known-issues.md).

## Where it is

Menus, options, and about screens: done. The game: not started. The Play button exits.

## Planned

**The play screen.** Everything else is waiting on it. `craftclash/playscreen.old.py` is the
disabled implementation to revive or replace, and `assets/textures/` already holds the art for
ore, stone, wood, and fences.

Then, roughly in the order the idea needs them:

- A world model, and one world per install — including somewhere to save it.
- The day loop: mining, crafting, building, upgrading.
- The night loop: monsters, damage to what you built, elixir for surviving.
- Wiring the options screen to gameplay that can use it.
- Audio playback, so the volume sliders and `ambient_1.m4a` mean something.

## Considered

**Fixing the console entry point.** `pip install craftclash && craftclash` currently exits
immediately.

**One version number.** The packaging and the UI disagree.

**`Toplevel()` for secondary windows** instead of a second `Tk()` root.

**Testable option and about screens.** Both call `mainloop()` internally; extracting a
build-and-return function, as `main.py` does, would make them assertable.

## Non-goals

**A game engine.** Tkinter and the standard library, deliberately — it keeps the install to
"have Python" and the source readable by someone learning.

**Multiplayer.** One world per install is the design, not a limitation to lift. The appeal is a
place that accumulates.

**Runtime dependencies.** Pillow would buy JPEG support and is still not worth being the first.

**3D.** The look is flat pixel art, and the assets are drawn for it.

**Reusing Minecraft or Terraria assets.** They are credited as inspirations. The art here is
original, and the GPL covering the assets depends on it staying that way.

## Contributing

Issues and pull requests welcome — see the
[Contributing Guide](https://github.com/willtheorangeguy/.github/blob/main/CONTRIBUTING.md) or
the [Discord](https://discord.gg/vdaABVxGHf). Contributions are GPL v3.

The play screen is the work that unblocks everything else.
