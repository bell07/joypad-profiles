class Devices:
    devices = {
        "touch_16_10": {
            "device_type": "touchscreen",
            "buttons": ["TOUCH"],
            "slider": [
                {
                    "name": "TOUCH_UP",
                    "axis": "ABS_X",
                    "sign": "+",
                    "analog": True,
                    "calibrate": 1.1111
                },
                {
                    "name": "TOUCH_DOWN",
                    "axis": "ABS_X",
                    "sign": "-",
                    "analog": True,
                    "calibrate": 1.1111
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
                }
            ]
        }
    }
