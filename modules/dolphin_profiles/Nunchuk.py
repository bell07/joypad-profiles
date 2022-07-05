ProfileName = "Nunchuk"
Type = "Wiimote"

# Wiimote only Horizontal profile

Map = [
    ["Buttons/A", "SOUTH", "TR", "CLICK_LEFT", "TOUCH"],
    ["Buttons/B", "TR2", "CLICK_RIGHT"],
    ["Buttons/1", "NORTH"],
    ["Buttons/2", "EAST"],
    ["Buttons/-", "SELECT"],
    ["Buttons/+", "START"],
    ["Buttons/Home", "MODE"],

    ["IR/Auto-Hide"],
    ["IR/Up", "_FORMAT_IR_UP", "POINTER_UP", "TOUCH_UP"],
    ["IR/Down", "_FORMAT_IR_DOWN", "POINTER_DOWN", "TOUCH_DOWN"],
    ["IR/Left", "_FORMAT_IR_LEFT", "POINTER_LEFT", "TOUCH_LEFT"],
    ["IR/Right", "_FORMAT_IR_RIGHT", "POINTER_RIGHT", "TOUCH_RIGHT"],

    ["Tilt/Angle"],
    ["Tilt/Forward", "_FORMAT_TILT_UP"],
    ["Tilt/Backward", "_FORMAT_TILT_DOWN"],
    ["Tilt/Left", "_FORMAT_TILT_LEFT"],
    ["Tilt/Right", "_FORMAT_TILT_RIGHT"],

    ["Shake/X", "WEST"],
    ["Shake/Y", "WEST"],
    ["Shake/Z", "WEST"],

    ["Extension"],
    ["Nunchuk/Buttons/C", "TL"],
    ["Nunchuk/Buttons/Z", "TL2"],

    ["Nunchuk/Stick/Up", "_FORMAT_NC_STICK_UP"],
    ["Nunchuk/Stick/Down", "_FORMAT_NC_STICK_DOWN"],
    ["Nunchuk/Stick/Left", "_FORMAT_NC_STICK_LEFT"],
    ["Nunchuk/Stick/Right", "_FORMAT_NC_STICK_RIGHT"],

    ["Nunchuk/Tilt/Forward", "_FORMAT_NC_TILT_UP"],
    ["Nunchuk/Tilt/Backward", "_FORMAT_NC_TILT_DOWN"],
    ["Nunchuk/Tilt/Left", "_FORMAT_NC_TILT_LEFT"],
    ["Nunchuk/Tilt/Right", "_FORMAT_NC_TILT_RIGHT"],

    ["Rumble/Motor"],

    ["D-Pad/Up", "DPAD_UP"],
    ["D-Pad/Down", "DPAD_DOWN"],
    ["D-Pad/Left", "DPAD_LEFT"],
    ["D-Pad/Right", "DPAD_RIGHT"],
]

FixedValues = {
    "IR/Auto-Hide": "True",
    "Tilt/Angle": "100.00000000000000",
    "Extension": "Nunchuk",
}

FormattedValues = {
    "_FORMAT_IR_UP": ["(!toggle({}) & {})", "THUMBR", "RS_UP"],
    "_FORMAT_IR_DOWN": ["(!toggle({}) & {})", "THUMBR", "RS_DOWN"],
    "_FORMAT_IR_LEFT": ["(!toggle({}) & {})", "THUMBR", "RS_LEFT"],
    "_FORMAT_IR_RIGHT": ["(!toggle({}) & {})", "THUMBR", "RS_RIGHT"],

    "_FORMAT_TILT_UP": ["(toggle({}) & {})", "THUMBR", "RS_UP"],
    "_FORMAT_TILT_DOWN": ["(toggle({}) & {})", "THUMBR", "RS_DOWN"],
    "_FORMAT_TILT_LEFT": ["(toggle({}) & {})", "THUMBR", "RS_LEFT"],
    "_FORMAT_TILT_RIGHT": ["(toggle({}) & {})", "THUMBR", "RS_RIGHT"],

    "_FORMAT_NC_STICK_UP": ["!toggle({}) & {}", "THUMBL", "LS_UP"],
    "_FORMAT_NC_STICK_DOWN": ["!toggle({}) & {}", "THUMBL", "LS_DOWN"],
    "_FORMAT_NC_STICK_LEFT": ["!toggle({}) & {}", "THUMBL", "LS_LEFT"],
    "_FORMAT_NC_STICK_RIGHT": ["!toggle({}) & {}", "THUMBL", "LS_RIGHT"],

    "_FORMAT_NC_TILT_UP": ["toggle({}) & {}", "THUMBL", "LS_UP"],
    "_FORMAT_NC_TILT_DOWN": ["toggle({}) & {}", "THUMBL", "LS_DOWN"],
    "_FORMAT_NC_TILT_LEFT": ["toggle({}) & {}", "THUMBL", "LS_LEFT"],
    "_FORMAT_NC_TILT_RIGHT": ["toggle({}) & {}", "THUMBL", "LS_RIGHT"],
}

Games = [
    "RMG",  # Super Mario Galaxy
    "SB4",  # Super Mario Galaxy 2
]
