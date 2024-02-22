class Devices:
    devices = {
        "steamdeck": {
            "name": "Steam Deck",
            "device_type": "joypad",

            # All keys list, sorted by usual drivers order
            "buttons": [
                "TOUCH_PRESS_L", "TOUCH_PRESS_R",
                "QUICK",  # Quick access (Dots)
                "SOUTH", "EAST", "WEST", "NORTH",
                "TL", "TR", "TL2", "TR2",
                "SELECT", "START", "MODE",  # Mode is Steam Button
                "THUMBL", "THUMBR",
                "DPAD_UP", "DPAD_DOWN", "DPAD_LEFT", "DPAD_RIGHT",
                "TRIGGER_HAPPY1", "TRIGGER_HAPPY2", "TRIGGER_HAPPY3", "TRIGGER_HAPPY4"
            ],

            "button_names": {
                "TOUCH_PRESS_L": "THUMB",
                "TOUCH_PRESS_R": "THUMB2",
                "QUICK": "BASE",
                # As of kernel-5.18 the NORTH and WEST are swapped in xpad driver
                # Seems to be the standard :(
                "NORTH": "WEST",
                "WEST": "NORTH",
            },

            # Keys settings.
            "slider": [
                {
                    "name": "LS_LEFT",
                    "axis": "X",
                    "sign": "-",
                    "analog": True,
                },
                {
                    "name": "LS_RIGHT",
                    "axis": "X",
                    "sign": "+",
                    "analog": True,
                },
                {
                    "name": "LS_UP",
                    "axis": "Y",
                    "sign": "-",
                    "analog": True,
                },
                {
                    "name": "LS_DOWN",
                    "axis": "Y",
                    "sign": "+",
                    "analog": True,
                },
                {
                    "name": "RS_LEFT",
                    "axis": "RX",
                    "sign": "-",
                    "analog": True,
                },
                {
                    "name": "RS_RIGHT",
                    "axis": "RX",
                    "sign": "+",
                    "analog": True,
                },
                {
                    "name": "RS_UP",
                    "axis": "RY",
                    "sign": "-",
                    "analog": True,
                },
                {
                    "name": "RS_DOWN",
                    "axis": "RY",
                    "sign": "+",
                    "analog": True,
                },
                {
                    "name": "LP_LEFT",
                    "axis": "HAT0X",
                    "sign": "-",
                    "analog": False,
                },
                {
                    "name": "LP_RIGHT",
                    "axis": "HAT0X",
                    "sign": "+",
                    "analog": False,
                },
                {
                    "name": "LP_UP",
                    "axis": "HAT0Y",
                    "sign": "-",
                    "analog": False,
                },
                {
                    "name": "LP_DOWN",
                    "axis": "HAT0Y",
                    "sign": "+",
                    "analog": False,
                },
                {
                    "name": "RP_LEFT",
                    "axis": "HAT1X",
                    "sign": "-",
                    "analog": False,
                },
                {
                    "name": "RP_RIGHT",
                    "axis": "HAT1X",
                    "sign": "+",
                    "analog": False,
                },
                {
                    "name": "RP_UP",
                    "axis": "HAT1Y",
                    "sign": "-",
                    "analog": False,
                },
                {
                    "name": "RP_DOWN",
                    "axis": "HAT1Y",
                    "sign": "+",
                    "analog": False,
                },
                {
                    "name": "TL2",
                    "axis": "HAT2X",
                    "sign": "-",
                    "analog": True,
                    "full": True,
                },
                {
                    "name": "TR2",
                    "axis": "HAT2Y",
                    "sign": "-",
                    "analog": True,
                    "full": True,
                },
            ],

            "rumble": [
                "TRIANGLE",
                "SQUARE",
                "SINE",
                "RUMBLE",
                "PERIODIC",
                "GAIN"
            ]
        }
    }


