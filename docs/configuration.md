# CraftClash — Configuration

No configuration file, no command-line options, no environment variables. Settings live in the
options screen, and everything else is a constant in the source.

## The options screen

Reached from **Options** on the main menu.

| Setting | Control |
|---|---|
| Sound volume | Slider |
| Music volume | Slider |
| In-game name | Text entry |
| Difficulty | Selection |

**Nothing consumes these yet**, because there is no gameplay to apply them to. They are the
interface for a game that has not been built.

## Assets

```
assets/
├── logo/       titlelogo.gif, titlethumbnail.{png,ico,gif}
├── sounds/     ambient_1.m4a
└── textures/   coal, copper, stone, wood, tree — .png plus .json models
```

Resolved from `main.py`'s own location:

```python
ASSETS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
```

That is the correct pattern and worth preserving — it is why the game runs from any working
directory, and it is exactly what a sibling project in this org gets wrong.

### Image formats

The title logo is a **GIF** because Tkinter's `PhotoImage` reads GIF and PNG only. Adding a JPEG
asset would need Pillow, which would be the project's first runtime dependency.

### The `.json` files

Alongside the fence textures — model definitions from Cubik Studio, credited in the README. Not
read by any current code path.

## Versions

Three places, and they disagree:

| Where | Says |
|---|---|
| `pyproject.toml`, `setup.py`, `setup.cfg` | `0.4.0` |
| Window title in `main.py` | `0.0.4 BETA` |
| Copyright label in `main.py` | `0.0.4 BETA` |
| Every `aboutscreen.py` window title | `0.0.4 BETA` |

Recorded in [`internal/known-issues.md`](./internal/known-issues.md).

## Window layout

Fixed in `main.py`: buttons `height=3, width=60`, `bd=4`, `relief=RAISED`, a `sky blue`
background, and a grid with the title spanning two rows.

## Packaging

`pyproject.toml`, `setup.py`, and `setup.cfg` all describe the same package, and `MANIFEST.in`
lists the asset files to include. `main.spec` is the PyInstaller build.
