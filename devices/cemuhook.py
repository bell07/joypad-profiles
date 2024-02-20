class Devices:
    devices = {
        "cemuhook": {
            "device_type": "DSUClient",

            "Accelerometer": [
                {
                    "name": "ACCEL_UP",
                    "axis": "Z",
                    "sign": "+",
                },
                {
                    "name": "ACCEL_DOWN",
                    "axis": "Z",
                    "sign": "-",
                },
                {
                    "name": "ACCEL_LEFT",
                    "axis": "Y",
                    "sign": "+",
                },
                {
                    "name": "ACCEL_RIGHT",
                    "axis": "Y",
                    "sign": "-",
                },
                {
                    "name": "ACCEL_FORWARD",
                    "axis": "X",
                    "sign": "+",
                },
                {
                    "name": "ACCEL_BACKWARD",
                    "axis": "X",
                    "sign": "-",
                }
            ],

            "Gyroscope": [
                {
                    "name": "PITCH_UP",
                    "axis": "Y",
                    "sign": "-",
                },
                {
                    "name": "PITCH_DOWN",
                    "axis": "Y",
                    "sign": "+",
                },
                {
                    "name": "ROLL_LEFT",
                    "axis": "X",
                    "sign": "-",
                },
                {
                    "name": "ROLL_RIGHT",
                    "axis": "X",
                    "sign": "+",
                },
                {
                    "name": "YAW_LEFT",
                    "axis": "Z",
                    "sign": "+",
                },
                {
                    "name": "YAW_RIGHT",
                    "axis": "Z",
                    "sign": "-",
                }
            ]
        }
    }
