ProfileName = "GC-Default"
Type = "GCPad"
Map = [
    ["Buttons/A", "SOUTH"],
    ["Buttons/B", "WEST"],
    ["Buttons/X", "EAST"],
    ["Buttons/Y", "NORTH"],
    ["Buttons/Z", "TR"],
    ["Buttons/Start", "START"],
    ["Main Stick/Up", "LS_UP"],
    ["Main Stick/Down", "LS_DOWN"],
    ["Main Stick/Left", "LS_LEFT"],
    ["Main Stick/Right", "LS_RIGHT"],
    ["C-Stick/Up", "RS_UP"],
    ["C-Stick/Down", "RS_DOWN"],
    ["C-Stick/Left", "RS_LEFT"],
    ["C-Stick/Right", "RS_RIGHT"],
    ["Triggers/L", "TL2"],
    ["Triggers/R", "TR2"],
    ["Triggers/L-Analog", "TL2"],
    ["Triggers/R-Analog", "TR2"],
    ["Rumble/Motor"],
    ["D-Pad/Up", "DPAD_UP"],
    ["D-Pad/Down", "DPAD_DOWN"],
    ["D-Pad/Left", "DPAD_LEFT"],
    ["D-Pad/Right", "DPAD_RIGHT"]
]


def get_profile_for_device(device):
    tl2 = device.get_button("TL2")

    return_map = []
    #  set trigger depending if analog slider or just a button
    if tl2 is not None and tl2.is_slider is True and tl2.analog is True:
        for line in Map:
            if not (line[0] == "Triggers/L" or line[0] == "Triggers/R"):
                return_map.append(line)
    else:
        for line in Map:
            if not (line[0] == "Triggers/L-Analog" or line[0] == "Triggers/R-Analog"):
                return_map.append(line)

    return {"map": return_map}
