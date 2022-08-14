class JS:
    name = "Nintendo Switch Combined Joy-Cons"

    # All keys list, sorted by usual drivers order
    buttons = [
        "SOUTH", "EAST", "NORTH", "WEST",
        "RECORD", "TL", "TR", "TL2", "TR2",
        "SELECT", "START", "MODE",
        "THUMBL", "THUMBR",
        "DPAD_UP", "DPAD_DOWN", "DPAD_LEFT", "DPAD_RIGHT"
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
    ]

    rumble = [
        "TRIANGLE",
        "SQUARE",
        "SINE",
        "RUMBLE",
        "PERIODIC",
        "GAIN"
    ]


class L_IMU:
    name = "Nintendo Switch Left Joy-Con IMU"
    Accelerometer = [
        {
            "name": "L_ACCEL_UP",
            "axis": "Z",
            "sign": "+",
        },
        {
            "name": "L_ACCEL_DOWN",
            "axis": "Z",
            "sign": "-",
        },
        {
            "name": "L_ACCEL_LEFT",
            "axis": "Y",
            "sign": "+",
        },
        {
            "name": "L_ACCEL_RIGHT",
            "axis": "Y",
            "sign": "-",
        },
        {
            "name": "L_ACCEL_FORWARD",
            "axis": "X",
            "sign": "+",
        },
        {
            "name": "L_ACCEL_BACKWARD",
            "axis": "X",
            "sign": "-",
        }
    ]

    Gyroscope = [
        {
            "name": "L_PITCH_UP",
            "axis": "Y",
            "sign": "-",
        },
        {
            "name": "L_PITCH_DOWN",
            "axis": "Y",
            "sign": "+",
        },
        {
            "name": "L_ROLL_LEFT",
            "axis": "X",
            "sign": "-",
        },
        {
            "name": "L_ROLL_RIGHT",
            "axis": "X",
            "sign": "+",
        },
        {
            "name": "L_YAW_LEFT",
            "axis": "Z",
            "sign": "+",
        },
        {
            "name": "L_YAW_RIGHT",
            "axis": "Z",
            "sign": "-",
        }
    ]

class R_IMU:
    name = "Nintendo Switch Right Joy-Con IMU"
    Accelerometer = [
        {
            "name": "R_ACCEL_UP",
            "axis": "Z",
            "sign": "+",
        },
        {
            "name": "R_ACCEL_DOWN",
            "axis": "Z",
            "sign": "-",
        },
        {
            "name": "R_ACCEL_LEFT",
            "axis": "Y",
            "sign": "+",
        },
        {
            "name": "R_ACCEL_RIGHT",
            "axis": "Y",
            "sign": "-",
        },
        {
            "name": "R_ACCEL_FORWARD",
            "axis": "X",
            "sign": "+",
        },
        {
            "name": "R_ACCEL_BACKWARD",
            "axis": "X",
            "sign": "-",
        }
    ]

    Gyroscope = [
        {
            "name": "R_PITCH_UP",
            "axis": "Y",
            "sign": "-",
        },
        {
            "name": "R_PITCH_DOWN",
            "axis": "Y",
            "sign": "+",
        },
        {
            "name": "R_ROLL_LEFT",
            "axis": "X",
            "sign": "-",
        },
        {
            "name": "R_ROLL_RIGHT",
            "axis": "X",
            "sign": "+",
        },
        {
            "name": "R_YAW_LEFT",
            "axis": "Z",
            "sign": "+",
        },
        {
            "name": "R_YAW_RIGHT",
            "axis": "Z",
            "sign": "-",
        }
    ]
