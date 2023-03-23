# SPDX-FileCopyright Text: 2023 Jacob Stack
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys: For use with adafruit RP2040 Macro Pad

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {# REQUIRED dict, must be named 'app'
    'name' : ' ', # Application name
    'macros' : [# List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x002400, 'name', ["""User Text string""", Keycode.ENTER]), # Text + Enter
        (0x000090, 'TskMgr', [Keycode.CONTROL, Keycode.SHIFT, Keycode.ESCAPE]), # Task Manager
        (0x002400, 'name', ["""User Text string""", Keycode.ENTER]),
        # 2nd row ----------
        (0x060600, 'PrtSc', [Keycode.PRINT_SCREEN]),
        (0x000090, 'GUI', [Keycode.GUI, 'r']), # Opens windows run GUI console
        (0x049620, 'name', ["""User Text string""", Keycode.ENTER]),
        # 3rd row ----------
        (0x000090, 'Home', [Keycode.HOME]), # Moves cursor to beginning of line of text
        (0x090049, ' /|\ ', [Keycode.CONTROL, Keycode.UP_ARROW]), # Moves the cursor up
        (0x000090, 'ScrRcd', [Keycode.GUI, Keycode.ALT, 'r']), # Opens xbox screen recorder app
        # 4th row ----------
        (0x090049, '<<<', [Keycode.CONTROL, Keycode.LEFT_ARROW]), # Moves cursor to the next left space in any line of text
        (0x071517, '\|/', [Keycode.CONTROL, 'q']),# Moves the cursor down
        (0x073079, '>>>', [Keycode.CONTROL, Keycode.RIGHT_ARROW]),# Moves cursor to the next right space in any line of text
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, Keycode.F4]) # Close window/tab
    ]
}
