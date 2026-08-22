# CraftClash — Documentation

A Tkinter game in progress. The menus, options, and about screens work; the game itself does
not exist yet.

```text
Craft-Clash/
├── main.py                      the main menu window
├── craftclash/
│   ├── optionscreen.py          sound, music, name, difficulty
│   ├── aboutscreen.py           licences and project info, in-app
│   └── playscreen.old.py        the disabled play screen
├── assets/
│   ├── logo/   sounds/   textures/
├── tests/test_main.py
└── docs/                        this documentation
```

## Pages

- [Quickstart](./quickstart.md) — run it, and what you will find
- [Installation](./installation.md) — source, PyPI, and the executable
- [Configuration](./configuration.md) — the options screen and the asset layout
- [Architecture](./architecture.md) — windows, screens, and the assets path
- [Development](./development.md) — tests, packaging, style
- [FAQ](./faq.md) — why Play does nothing, why GPL, what the assets are
- [Troubleshooting](./troubleshooting.md) — Tkinter, images, the pip command
- [Roadmap](./roadmap.md) — direction and non-goals
- [Known issues](./internal/known-issues.md) — recorded defects

## What state this is in

**Beta, version 0.4.0, and the game is not implemented.**

| Screen | Works |
|---|---|
| Main menu | Yes |
| Options | Yes — sliders, name, difficulty |
| About | Yes — licences and project details |
| Play | **No.** The button is wired to `exit` |

`craftclash/playscreen.old.py` is the play screen, renamed out of the import path. Nothing in the
codebase generates a world, and there is no game loop.

These docs describe what runs. Where the code and the older documentation disagreed — and they
did, in several places — the code wins, and the disagreement is recorded in
[`internal/known-issues.md`](./internal/known-issues.md).

## The idea

Clash of Clans' build-and-defend loop with Minecraft's crafting: spend the day gathering ore,
crafting tools and walls, and upgrading buildings; spend the night defending what you built.

One world per install, deliberately — the appeal is a place that persists and accumulates rather
than one you restart.

## GPL, not MIT

Unusually for this org, CraftClash is **GPL v3**, and the licence explicitly covers the non-code
assets as well. Anything derived from it must also be GPL.
