class Devices:
    devices = {
        "gpdwin2": {
            "device_type": "joypad",
            "name": "GPD Win 2 X-Box Controller",

            # All keys list, sorted by usual drivers order
            "buttons": [
                "SOUTH", "EAST", "WEST", "NORTH",
                "TL", "TR",
                "SELECT", "START", "MODE",
                "THUMBL", "THUMBR",
            ],

            "button_names": {
                # As of kernel-5.18 the NORTH and WEST are swapped in xpad driver
                "NORTH": "WEST",
                "WEST": "NORTH"
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
                    "name": "TL2",
                    "axis": "Z",
                    "sign": "+",
                    "analog": False,
                    "full": True,
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
                    "name": "TR2",
                    "axis": "RZ",
                    "sign": "+",
                    "analog": False,
                    "full": True,
                },
                {
                    "name": "DPAD_LEFT",
                    "axis": "HAT0X",
                    "sign": "-",
                    "analog": False,
                },
                {
                    "name": "DPAD_RIGHT",
                    "axis": "HAT0X",
                    "sign": "+",
                    "analog": False,
                },
                {
                    "name": "DPAD_UP",
                    "axis": "HAT0Y",
                    "sign": "-",
                    "analog": False,
                },
                {
                    "name": "DPAD_DOWN",
                    "axis": "HAT0Y",
                    "sign": "+",
                    "analog": False,
                }
            ],

            "rumble": [
                "TRIANGLE",
                "SQUARE",
                "SINE",
                "RUMBLE",
                "PERIODIC",
                "GAIN"
            ],
        },

        "gpdwin2-touch": {
            "device_type": "touchscreen",
            "name": "Goodix Capacitive TouchScreen",
            "buttons": ["TOUCH"],

            "slider": [
                {
                    "name": "TOUCH_UP",
                    "axis": "ABS_X",
                    "sign": "+",
                    "analog": True,
                },
                {
                    "name": "TOUCH_DOWN",
                    "axis": "ABS_X",
                    "sign": "-",
                    "analog": True,
                },
                {
                    "name": "TOUCH_LEFT",
                    "axis": "ABS_Y",
                    "sign": "-",
                    "analog": True,
                    "calibrate": 0.75
                },
                {
                    "name": "TOUCH_RIGHT",
                    "axis": "ABS_Y",
                    "sign": "+",
                    "analog": True,
                    "calibrate": 0.75
                },
            ],
        }
    }
