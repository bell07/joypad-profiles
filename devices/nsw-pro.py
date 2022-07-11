class JS:
    name = "Nintendo Switch Pro Controller"

    # All keys list, sorted by usual drivers order
    buttons = [
        "SOUTH", "EAST", "NORTH", "WEST",
        "RECORD", "TL", "TR", "TL2", "TR2",
        "SELECT", "START", "MODE",
        "THUMBL", "THUMBR",
    ]

    button_names = {
        "RECORD": "Z",
    }

    # Keys settings.
    slider = [
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
    ]

    rumble = [
        "TRIANGLE",
        "SQUARE",
        "SINE",
        "RUMBLE",
        "PERIODIC",
        "GAIN"
    ]


class IMU:
    name = "Nintendo Switch Pro Controller IMU"
    Accelerometer = [
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
            "sign": "-",
        },
        {
            "name": "ACCEL_RIGHT",
            "axis": "Y",
            "sign": "+",
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
    ]

    Gyroscope = [
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
