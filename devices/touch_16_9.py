class Devices:
    devices = {
        "touch_16_9": {
            "device_type": "touchscreen",
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
                    "calibrate": 0.75  # 4:3 => 16:9  ( 3/4 * 0.75 = 9/16 )
                },
                {
                    "name": "TOUCH_RIGHT",
                    "axis": "ABS_Y",
                    "sign": "+",
                    "analog": True,
                    "calibrate": 0.75  # 4:3 => 16:9  ( 3/4 * 0.75 = 9/16 )
                }
            ]
        }
    }
