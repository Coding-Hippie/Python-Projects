# SPDX-FileCopyright Text: 2022 Jacob Stack 
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys: Firefox macros with weblink capabilty 

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {# REQUIRED dict, must be named 'app'
    'name' : 'Linux', # Application name
    'macros' : [# List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x073079, '< Home', [Keycode.CONTROL, 'a']),# Moves to the beginning of cmd line
        (0x090049, 'End >', [Keycode.CONTROL, 'e']), #Moves to the end of cmd line
        (0x072019, 'Lol-Cat',[""" lolcat """]), # Input URL
        # 2nd row ----------
        (0x024960, 'Freeze', [Keycode.CONTROL, 's']),
        (0x071517, 'Unfreeze', [Keycode.CONTROL, 'q']),
        (0x007200, 'Figlet', [""" figlet """]), # Input URL
        # 3rd row ----------
        (0x000090, 'Clear', [""" clear """]), #cleans terminal screen 
        (0x000090, 'Term', [Keycode.CONTROL, 'c']), #Terminates working command
        (0x000090, 'Pause', [Keycode.CONTROL, 'z']), # Pause working command
        # 4th row ----------
        (0x002400, 'sudo ^', [""" sudo apt install """]), # install 
        (0x900090, 'Weather', [""" curl http://wttr.in """]),# sudo weather 
        (0x002400, 'Cal', [""" cal """]), # Calendar (sudo apt install ncal)
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, 'w']) # Close window/tab
    ]
}
