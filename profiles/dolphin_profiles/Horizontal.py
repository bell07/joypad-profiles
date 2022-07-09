ProfileName = "Horizontal"
Type = "Wiimote"

# Wiimote only Horizontal profile

Map = [
    ["Buttons/A", "NORTH", "TR", "CLICK_LEFT", "TOUCH"],
    ["Buttons/B", "TL", "CLICK_RIGHT"],
    ["Buttons/1", "WEST"],
    ["Buttons/2", "SOUTH"],
    ["Buttons/-", "SELECT"],
    ["Buttons/+", "START"],
    ["Buttons/Home", "MODE"],
    ["IR/Auto-Hide"],
    ["IR/Up", "LS_UP", "POINTER_UP", "TOUCH_UP"],
    ["IR/Down", "LS_DOWN", "POINTER_DOWN", "TOUCH_DOWN"],
    ["IR/Left", "LS_LEFT", "POINTER_LEFT", "TOUCH_LEFT"],
    ["IR/Right", "LS_RIGHT", "POINTER_RIGHT", "TOUCH_RIGHT"],
    ["Tilt/Forward", "TL2"],
    ["Tilt/Backward", "TR2"],
    ["Tilt/Left", "RS_DOWN"],
    ["Tilt/Right", "RS_UP"],
    ["Shake/X", "TR"],
    ["Shake/Y", "TR"],
    ["Shake/Z", "TR"],
    ["Rumble/Motor"],
    ["D-Pad/Up", "DPAD_LEFT"],
    ["D-Pad/Down", "DPAD_RIGHT"],
    ["D-Pad/Left", "DPAD_DOWN"],
    ["D-Pad/Right", "DPAD_UP"],

    ["IMUAccelerometer/Up", "ACCEL_UP"],
    ["IMUAccelerometer/Down", "ACCEL_DOWN"],
    ["IMUAccelerometer/Left", "ACCEL_FORWARD"],
    ["IMUAccelerometer/Right", "ACCEL_BACKWARD"],
    ["IMUAccelerometer/Forward", "ACCEL_RIGHT"],
    ["IMUAccelerometer/Backward", "ACCEL_LEFT"],
    ["IMUGyroscope/Pitch Up", "ROLL_LEFT"],
    ["IMUGyroscope/Pitch Down", "ROLL_RIGHT"],
    ["IMUGyroscope/Roll Left", "PITCH_UP"],
    ["IMUGyroscope/Roll Right", "PITCH_DOWN"],
    ["IMUGyroscope/Yaw Left", "YAW_LEFT"],
    ["IMUGyroscope/Yaw Right", "YAW_RIGHT"],
    ["IMUIR/Enabled"],
]

FixedValues = {
    "IR/Auto-Hide": "True",
    "IMUIR/Enabled": "False",
}

Games = [
    "SMN",  # New Super Mario Bros. Wii
    "MRR",  # New Super Mario Bros. Retro edition
    "NSS",  # New Super Mario Bros. Summer Sun Special

    "R8P",  # Super Paper Mario
]
