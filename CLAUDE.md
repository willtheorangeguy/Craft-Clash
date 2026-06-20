# CLAUDE.md

## Project Overview

Craft-Clash is a Python GUI game combining Minecraft crafting with Clash of Clans defense mechanics. Players build/craft during the day and defend against monsters at night. Currently in BETA (v0.4.0). Licensed under GPL-3.0.

## Tech Stack

- **Language:** Python 3.9+
- **GUI Framework:** Tkinter
- **Image Processing:** Pillow
- **Packaging:** setuptools (pyproject.toml, setup.py, setup.cfg)
- **Testing:** unittest + pytest
- **Linting:** Pylint, Black (formatter)
- **CI:** GitHub Actions (tests, pylint, CodeQL, PyPI publishing)

## Repository Structure

```
main.py                  # Primary entry point (Tkinter app)
__main__.py              # Alternative entry point
craftclash/              # Main package
  __init__.py            # Exports aboutscreen, optionscreen
  aboutscreen.py         # About/license screen
  optionscreen.py        # Settings UI
  playscreen.old.py      # Legacy game screen
assets/                  # Game resources (textures, sounds, logos)
tests/                   # Unit tests
  test_main.py           # GUI component tests
docs/                    # User documentation
.github/workflows/       # CI/CD pipelines
```

## Common Commands

```bash
# Run the game
python main.py

# Run tests
python -m pytest tests/
python -m unittest discover tests

# Lint
pylint $(git ls-files '*.py')

# Install locally
pip install -e .

# Install dependencies
pip install -r requirements.txt
```

## CI/CD

- **tests.yml** - Runs pytest on push/PR (Python 3.12, Ubuntu)
- **pylint.yml** - Pylint on push
- **codeql-analysis.yml** - Security scanning (main branch, scheduled Tuesdays)
- **push-to-pypi.yml** - Publishes to PyPI on GitHub release (needs `PYPI_API_TOKEN`)

## Development Guidelines

- Follow GitHub Flow (branch from main, PR to merge)
- Format with Black
- Tests cover GUI components (window, buttons, labels, colors)
- Entry point is `craftclash` CLI command (defined in setup.py/setup.cfg)
- Game assets go in `assets/` (PNG textures, JSON configs, M4A audio)
- Package version is maintained in `setup.cfg`
