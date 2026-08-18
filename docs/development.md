# CraftClash — Development

## Setup

```bash
git clone https://github.com/willtheorangeguy/Craft-Clash
cd Craft-Clash
pip install -r requirements.txt
python main.py
```

No runtime dependencies; `requirements.txt` is the development tooling.

## Commands

```bash
python main.py             # run
pytest                     # tests
pylint main.py craftclash  # what CI lints with
pyinstaller main.spec      # the Windows executable
```

## Tests

`tests/test_main.py` builds the main window via `craftclash()` and asserts on the widgets it
constructed. That works because the function returns the window without entering the event loop.

**Keep that property.** Adding a `mainloop()` call inside `craftclash()` would fix the console
entry point and break every test — the right fix is a separate wrapper that calls both. See
[`internal/known-issues.md`](./internal/known-issues.md).

The options and about screens are untested, because both create their own `Tk()` and call
`mainloop()` internally. Extracting a build-and-return function from each, as `main.py` does,
would make them testable the same way.

## Style

- **Pylint**, with per-file disables at the top (`import-error`, `invalid-name`,
  `too-many-lines`).
- **GPL header on every module** — required by the licence, not decoration.
- **Resolve paths against `__file__`**, never the working directory.
- **Bind `PhotoImage` objects to a widget attribute** so Tk does not lose them.

## Packaging

Three descriptions coexist — `pyproject.toml`, `setup.py`, and `setup.cfg` — all naming version
`0.4.0` and the entry point `craftclash = main:craftclash`. `MANIFEST.in` includes the assets.

Consolidating on `pyproject.toml` would remove a class of drift; the version strings inside
`main.py` and `aboutscreen.py` are already out of step with it.

## Working on the play screen

`craftclash/playscreen.old.py` is the disabled implementation. Reviving it means renaming it into
the package, importing it in `main.py`, and pointing `btn_play` at it instead of `exit`.

Until then, the button quits — which is the single most misleading thing about the running
program.

## CI

| Workflow | Does |
|---|---|
| `tests.yml` | pytest |
| `pylint.yml` | Lint |
| `codeql-analysis.yml` | Security scan |
| `push-to-pypi.yml` | Publish |

Note that publishing succeeds regardless of whether the published command works — nothing runs
the installed entry point.

## Licence

GPL v3, covering the assets as well. Contributions are GPL, and anything derived from this must
be too. Keep the header on new modules.

## Recording defects

Bugs found while working here go in [`internal/known-issues.md`](./internal/known-issues.md)
rather than being fixed in passing, unless fixing them is the job you are on.
