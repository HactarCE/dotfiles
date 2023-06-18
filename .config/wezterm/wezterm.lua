local wezterm = require 'wezterm'
local config = {}

config.colors = {
--   -- The default text color
--   foreground = 'silver',
--   -- The default background color
--   background = 'black',

--   -- Overrides the cell background color when the current cell is occupied by the
--   -- cursor and the cursor style is set to Block
--   cursor_bg = '#52ad70',
--   -- Overrides the text color when the current cell is occupied by the cursor
--   cursor_fg = 'black',
--   -- Specifies the border color of the cursor when the cursor style is set to Block,
--   -- or the color of the vertical or horizontal bar when the cursor style is set to
--   -- Bar or Underline.
--   cursor_border = '#52ad70',

--   -- the foreground color of selected text
--   selection_fg = 'black',
--   -- the background color of selected text
--   selection_bg = '#fffacd',

  -- The color of the scrollbar "thumb"; the portion that represents the current viewport
  scrollbar_thumb = '#222222',

  -- The color of the split lines between panes
  split = '#444444',

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



-- local custom = wezterm.color.get_builtin_schemes()["Catppuccin Mocha"]
-- custom.background = "#000000"
-- custom.tab_bar.background = "#040404"
-- custom.tab_bar.inactive_tab.bg_color = "#0f0f0f"
-- custom.tab_bar.new_tab.bg_color = "#080808"

-- config.window_background_image = "/Users/andrew/Documents/PlatonicSolidsBackground/platonic_solids_7_compressed.jpg"
-- config.window_background_image_hsb = {
--     hue = 1.0,
--     saturation = 1.0,
--     brightness = 0.2,
-- }
config.window_background_opacity = 0.8
config.macos_window_background_blur = 10






-- config.color_scheme = 'Catppuccin Mocha'
config.font = wezterm.font { family = 'FiraCode Nerd Font Mono', weight = 'Regular' }
config.adjust_window_size_when_changing_font_size = false
config.warn_about_missing_glyphs = true
config.use_fancy_tab_bar = true
config.enable_tab_bar = true
config.hide_tab_bar_if_only_one_tab = true

-- config.color_schemes = { ["OLEDppuccin"] = custom }
-- config.color_scheme = "OLEDppuccin"

return config
