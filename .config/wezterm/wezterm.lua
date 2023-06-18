local wezterm = require 'wezterm'
local config = {}

-- Colors
config.colors = {
  ansi = {
    '#333333',
    '#ff3333',
    '#00ee00',
    '#eeee00',
    '#33aaff',
    '#cc33cc',
    '#66dddd',
    '#666666',
  },
  brights = {
    '#ffffff',
    '#ff7777',
    '#88ff88',
    '#ffff99',
    '#77ccff',
    '#dd77dd',
    '#aaffff',
    '#999999',
  },
}

-- Background
config.window_background_opacity = 0.8
config.macos_window_background_blur = 10

-- Font
config.font = wezterm.font { family = 'FiraCode Nerd Font Mono', weight = 'Regular' }
config.warn_about_missing_glyphs = true

-- Tabs
config.enable_tab_bar = true
config.hide_tab_bar_if_only_one_tab = true
config.use_fancy_tab_bar = true

return config
