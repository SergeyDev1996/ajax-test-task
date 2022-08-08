device_settings = [
    {0: [3, "field1"], 3: [1, "field2"], 4: [1, "field3"], 5: [3, "field4"]},
    {
        0: [1, "field5"],
        1: [1, "field6"],
        2: [1, "field7"],
        3: [3, "field8"],
    },
    {0: [1, "field9"], 5: [1, "field10"]},
    {},
]

field1 = {
    "0": "Low",
    "1": "reserved",
    "2": "reserved",
    "3": "reserved",
    "4": "Medium",
    "5": "reserved",
    "6": "reserved",
    "7": "High",
}
field4 = {
    "0": "00",
    "1": "10",
    "2": "20",
    "3": "30",
    "4": "40",
    "5": "50",
    "6": "60",
    "7": "70",
}
field8 = {
    "0": "Very Low",
    "1": "reserved",
    "2": "Low",
    "3": "reserved",
    "4": "Medium",
    "5": "High",
    "6": "reserved",
    "7": "Very High",
}

device_extended_fields = {
    "field1": field1,
    "field4": field4,
    "field8": field8,
}


def convert_heximal_to_binary(binary_payload):
    return bin(int(binary_payload, 16))[2:].zfill(32)


def get_parameters_from_binary(payload):
    result = {}
    payload_final = convert_heximal_to_binary(payload)
    split_by_byte = [payload_final[i:i + 8][::-1] for i in range(0, len(payload_final), 8)]
    current_byte = 0
    for setting in device_settings:

        for bit_number, parameter in setting.items():
            parameter_length = parameter[0]
            parameter_beginning = bit_number
            parameter_end = bit_number + parameter_length
            current_parameter = split_by_byte[current_byte][parameter_beginning:parameter_end]
            if current_parameter == "1" or current_parameter == "0":
                result[parameter[1]] = "0" + current_parameter
            else:
                integer_parameter = int(current_parameter, 2)
                current_field = device_extended_fields[parameter[1]]
                result[parameter[1]] = current_field[str(integer_parameter)]

        current_byte += 1
    return result

