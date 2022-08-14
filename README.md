# joypad-profiles

Configuration profiles for joypads and gaming devices, for different games and emulators on Linux.

The repo contains python script to generate usable configurations for games and emulators, with different devices.

The script is able to install the configurations to the right places, but is able to just install the files into the
target folder.

All xbox controller pictures are derivative work (added labels) of
[Jishenaz / CC0](https://commons.wikimedia.org/wiki/File:Xbox_Controller.svg)

## Usage

- Checkout / unpack the joypad-profiles
- use the provided files in "target" folder
- or:
- copy settings.py.template to settings.py and adjust settings, enable install parameter
- run the `python main.py`

## Supported Devices

Device | Description
--- | ---
all | Just generate settings for all devices. Used to fill the target folder
gpdwin2 | GPD Win 2 handheld gaming device, including touchscreen. The keys are like xpad profile with next differences: TL2/TR2 are not analog. THUMBL/THUMBR are placed at LT3/LR3
nsw-joycons | Nintendo Switch combined joycons
nsw-pro | Nintendo Switch Pro Controller, including IMU configuration
[xpad](devices/xpad.svg) | Virtual for all xbox compatible devices. Needs "name" parameter in settings.py file
logitechF700 | Logitech F700 - uses xbox profile. Note, the DirectInput mode is not supported with the joypad-profiles

## Supported Games and emulators

Emulator | Profile | Supported games
--- | --- | ---
dolphin | [GC-Default](profiles/dolphin_profiles/GCPad.svg) | All gamecube games
| |
dolphin | [Horizontal](profiles/dolphin_profiles/Horizontal.svg) | SMN - New Super Mario Bros. Wii
dolphin | Horizontal | MRR New Super Mario Bros. Retro edition
dolphin | Horizontal | NSS New Super Mario Bros. Summer Sun Special
dolphin | Horizontal | R8P Super Paper Mario
| |
dolphin | [Nunchuk](profiles/dolphin_profiles/Nunchuk.svg) | RMG Super Mario Galaxy
dolphin | Nunchuk | SB4 Super Mario Galaxy 2
| |
dosbox + dosbox-x | digger | Digger (1983)
dosbox + dosbox-x | tombraider | Tomb Raider 1 (1996)
dosbox + dosbox-x | turrican2 | Turrican II: The Final Fight (1995)
| |
mupen64plus | [mupen64plus](profiles/mupen64plus.svg) | All games

Detailed key mappings list can be found in [Key mapping overview](profiles/README.md)
