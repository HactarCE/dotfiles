# Dotfiles

These are my [dotfiles](https://askubuntu.com/questions/94780/what-are-dot-files). Use them however you see fit. I use a [bare git repository](https://www.atlassian.com/git/tutorials/dotfiles) with the alias `dot` (abbreviated `d`) to manage them.

I am currently using macOS on an M2 Macbook Pro.

## History

Before April 2020, I was dual-booting Windows 10 with i3wm on Arch Linux, using Linux as my primary driver. Those dotfiles can be found on the [`linux-2020` branch](https://github.com/HactarCE/dotfiles/tree/linux-2020) of this repo.

Unfortunately, the lack of support for eGPU hotplug and mixed DPI drove me to run Windows as my main OS. From April 2020 to June 2023, I was using Windows.

In June 2023, after seeing what Apple's new ARM processors did to Rust compile times, I switched to macOS.

## Software

* **OS:** macOS
* **Terminal:** [Wezterm][wezterm]
  * **Shell:** [Fish][fish]
    * **Prompt:** [Starship][starship-prompt]
  * **Color scheme:** [custom][custom-terminal-colors]
* **Dotfiles manager:** [yadm][yadm]

[wezterm]: https://wezfurlong.org/wezterm/
[fish]: https://fishshell.com/
[starship-prompt]: https://starship.rs/
[yadm]: https://yadm.io/

### Applications

* **Web browser:** [Firefox][firefox]
* **Password manager:** [Bitwarden][bitwarden]
* **Notes:** [Obsidian][obsidian]

[firefox]: https://www.mozilla.org/en-US/firefox/
[bitwarden]: https://bitwarden.com/
[obsidian]: https://obsidian.md/

### Daemons

* **Window management software:** [Contexts][contexts] and [Rectangle][rectangle]
* **Keybinding daemons:** [BetterTouchTool][bettertouchtool] and [Karabiner-Elements][karabiner-elements]

[contexts]: https://contexts.co/
[rectangle]: https://rectangleapp.com/
[bettertouchtool]: https://folivora.ai/
[karabiner-elements]: https://karabiner-elements.pqrs.org/

### Editors

* **Text editor:** TBD (considering VSCode, Neovim, and Helix)
  * **Theme:** TBD
  * **Color scheme:** TBD
  * **Modal editing keybinds:** TBD (probably custom)
* **Bitmap image editor:** [GIMP][gimp]
* **Vector image editor:** [Inkscape][inkscape]
* **Video editor:** [Kdenlive][kdenlive]

[gimp]: https://www.gimp.org/
[inkscape]: https://inkscape.org/
[kdenlive]: https://kdenlive.org/en/

### Utilities

* **Calculator:** [SpeedCrunch][speedcrunch]
    * **Color scheme:** [Behave][custom-behave] ([original][st3-behave])

[speedcrunch]: https://speedcrunch.org/
[custom-behave]: https://github.com/HactarCE/dotfiles/blob/master/.local/share/SpeedCrunch/color-schemes/Behave.json
[st3-behave]: https://packagecontrol.io/packages/Behave%20Color%20Scheme

## Configuration

### Fonts

* [Fira Code Mono][font-fira-code] [Nerd font][nerd-font] - terminal
* [Input Mono][font-input] - TODO might use if I can patch it to make it a nerd font
* [Iosevka SS04][font-iosevka] - TODO might use if I can patch it to make it a nerd font

[font-fira-code]: https://fonts.google.com/specimen/Fira+Code
[font-input]: https://input.fontbureau.com/
[font-iosevka]: https://typeof.net/Iosevka/
[nerd-font]: https://www.nerdfonts.com/

### Other

* **Keyboard layout:** [Colemak][colemak]
* **Wallpaper:** [4D Platonic Solids][platonic-solids-wallpaper]

[colemak]: https://colemak.com/

## Hardware

* **Model:** Macbook Pro 14-inch
* **CPU:** M2
* **Memory:** 32 GB
* **Peripherals:**
  * [ZSA Moonlander Mark I][Moonlander]
  * Logitech G600 MMO Gaming Mouse

[Moonlander]: https://www.zsa.io/moonlander/
