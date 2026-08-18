<!-- Logo -->
<h1 align="center">
  <img src="https://raw.githubusercontent.com/willtheorangeguy/.github/main/icons/Craft-Clash/logo.png" height="250px" width="400px" alt="CraftClash">
  <br>
  CraftClash
  <br>
</h1>

<!-- Copy -->
<h4 align="center">A day-and-night survival game: build and craft by day, hold off the monsters by night.</h4>

<!-- Badges -->
<div align="center">
  <img alt="PyPI Build State" src="https://github.com/willtheorangeguy/Craft-Clash/actions/workflows/push-to-pypi.yml/badge.svg">
  <img alt="Pytest State" src="https://github.com/willtheorangeguy/Craft-Clash/actions/workflows/tests.yml/badge.svg">
  <img alt="Pylint State" src="https://github.com/willtheorangeguy/Craft-Clash/actions/workflows/pylint.yml/badge.svg">
  <img alt="CodeQL State" src="https://github.com/willtheorangeguy/Craft-Clash/actions/workflows/codeql-analysis.yml/badge.svg">
  <img alt="GitHub Version" src="https://img.shields.io/github/v/release/willtheorangeguy/Craft-Clash?include_prereleases">
  <img alt="GitHub Issues" src="https://img.shields.io/github/issues/willtheorangeguy/Craft-Clash">
  <img alt="GitHub Pull Requests" src="https://img.shields.io/github/issues-pr/willtheorangeguy/Craft-Clash">
</div>

<!-- Navigation -->
<p align="center">
  <a href="#status">Status</a> •
  <a href="#key-features">Key Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#documentation">Documentation</a> •
  <a href="#support">Support</a> •
  <a href="#contributing">Contributing</a> •
  <a href="#credits">Credits</a> •
  <a href="#license">License</a>
</p>

<!-- Screenshot -->
<div align="center">
  <img src="https://raw.githubusercontent.com/willtheorangeguy/.github/main/icons/Craft-Clash/mainscreen.png" alt="CraftClash main screen">
</div>

## Status

**Beta, and the game itself is not built yet.** The main menu, the options screen, and the about screen all work. The **Play!** button does not start a game — it is currently wired to exit, and `craftclash/playscreen.old.py` is the disabled play screen.

`PLANNING.md` tracks what remains. Everything below describes what runs today; see [`docs/roadmap.md`](docs/roadmap.md) for what does not, and [`docs/internal/known-issues.md`](docs/internal/known-issues.md) for the defects found while writing these docs.

## Key Features

- A Tkinter main menu with three screens — play, options, and about.
- **Options**: sound volume, music volume, in-game name, and difficulty.
- **About**: the project's licences and internal details, rendered in-app.
- Pure standard library: Tkinter only, no game engine and nothing to install beyond Python.
- Cross-platform — Windows, macOS, Linux.

## Installation

```bash
git clone https://github.com/willtheorangeguy/Craft-Clash
cd Craft-Clash
python main.py
```

There is also a PyPI package and a Windows executable, both with caveats — see [`docs/installation.md`](docs/installation.md).

## Usage

Run `python main.py`. The menu offers **Play!**, **Options**, and **About**.

## Documentation

Full documentation lives in [`docs/`](docs/README.md):
[Quickstart](docs/quickstart.md) · [Installation](docs/installation.md) · [Configuration](docs/configuration.md) · [Architecture](docs/architecture.md) · [Development](docs/development.md) · [FAQ](docs/faq.md) · [Troubleshooting](docs/troubleshooting.md) · [Roadmap](docs/roadmap.md)

## Support

Open a [GitHub Discussion](https://github.com/willtheorangeguy/Craft-Clash/discussions/new), file an [issue](https://github.com/willtheorangeguy/Craft-Clash/issues/new/choose), or join the [Discord](https://discord.gg/vdaABVxGHf).

## Contributing

Please contribute using [GitHub Flow](https://guides.github.com/introduction/flow). Create a branch, add commits, and [open a pull request](https://github.com/willtheorangeguy/Craft-Clash/compare).

See the org-wide [Contributing Guide](https://github.com/willtheorangeguy/.github/blob/main/CONTRIBUTING.md) and [Code of Conduct](https://github.com/willtheorangeguy/.github/blob/main/CODE_OF_CONDUCT.md).

## Credits

This software uses the following open source packages, projects, services or websites:

<!-- Credits Table -->
<table>
  <tr>
    <th align="center"><img src="https://applets.imgix.net/https%3A%2F%2Fassets.ifttt.com%2Fimages%2Fchannels%2F2107379463%2Ficons%2Fmonochrome_large.png?w=240&h=240&s=8a19bbc158996d098e2fb18310ba7f33" width="150" height="150" alt="GitHub"/></th>
    <th align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/182px-Python-logo-notext.svg.png" width="150" height="150" alt="PSF"/></th>
    <th align="center"><img src="https://pyinstaller.readthedocs.io/en/v4.2/_static/pyinstaller-draft1a.ico" width="150" height="150" alt="PyInstaller"/></th>
    <th align="center"><img src="https://pbs.twimg.com/profile_images/871321943219347457/WJRtI_QH_400x400.jpg" width="150" height="150" alt="BDCraft"/></th>
  </tr>
  <tr>
    <td align="center">GitHub</td>
    <td align="center">Python Software Foundation</td>
    <td align="center">PyInstaller</td>
    <td align="center">BDCraft Cubix</td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/">Web</a> - <a href="https://github.com/pricing">Plans</a></td>
    <td align="center"><a href="https://www.python.org/">Web</a> - <a href="https://psfmember.org/civicrm/contribute/transact?reset=1&id=2">Donate</a></td>
    <td align="center"><a href="https://pyinstaller.readthedocs.io/en/stable/">Web</a> - <a href="https://www.pyinstaller.org/funding.html#funding-by-individuals">Donate</a></td>
    <td align="center"><a href="https://bdcraft.net/reco-cubik-studio/">Web</a></td>
  </tr>
    <tr>
    <th align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Microsoft_Paint.svg/2048px-Microsoft_Paint.svg.png" width="150" height="150" alt="Microsoft Paint"/></th>
    <th align="center"><img src="https://pbs.twimg.com/profile_images/454744766836527104/AmyB7c-a_400x400.png" width="150" height="150" alt="Piskel"/></th>
    <th align="center"><img src="https://pbs.twimg.com/profile_images/1559209238076919809/H57ucjs2_400x400.jpg" width="150" height="150" alt="Minecraft"/></th>
    <th align="center"><img src="https://www.sir-apfelot.de/wp-content/uploads/2022/06/terraria-logo-1024x1024.jpg" width="150" height="150" alt="Terraria"/></th>
  </tr>
  <tr>
    <td align="center">Microsoft Paint</td>
    <td align="center">Piskel</td>
    <td align="center">Minecraft</td>
    <td align="center">Terraria</td>
  </tr>
  <tr>
    <td align="center"><a href="https://apps.microsoft.com/store/detail/paint/9PCFS5B6T72H?hl=en-us&gl=us">Web</a></td>
    <td align="center"><a href="https://www.piskelapp.com/">Web</a></td>
    <td align="center"><a href="https://www.minecraft.net/en-us">Web</a> - <a href="https://www.minecraft.net/get-minecraft">Buy</a></td>
    <td align="center"><a href="https://terraria.org/">Web</a> - <a href="https://store.steampowered.com/app/105600/">Buy</a></td>
  </tr>
</table>

Sponsor [@willtheorangeguy](https://github.com/willtheorangeguy) on [PayPal](https://paypal.me/wvdg44?country.x=CA&locale.x=en_US).

## License

This project, **including its non-code assets**, is licensed under the [GNU General Public License v3](https://www.gnu.org/licenses/gpl-3.0.en.html) — see [`LICENSE.md`](LICENSE.md).

Note this is GPL, not the MIT licence used elsewhere in this org: anything derived from it must be GPL too.
