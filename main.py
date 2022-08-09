from settings import device_settings, fields_with_multiply_bytes, field1, field4, field8
import string

def convert_heximal_to_binary(binary_payload):
    return bin(int(binary_payload, 16))[2:].zfill(32)


def get_parameters_from_binary(payload):
    result = {}
    try:
        payload_final = convert_heximal_to_binary(payload)
    except ValueError:
        raise "The payload should be hexadecimal"

    split_by_byte = [payload_final[i:i + 8][::-1] for i in range(0, len(payload_final), 8)]
    check = all(c in string.hexdigits for c in payload_final)
    if check is False:
        raise ValueError("All the symbols should be hexadecimal")
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
                current_field = fields_with_multiply_bytes[parameter[1]]
                result[parameter[1]] = current_field[str(integer_parameter)]

        current_byte += 1
    return result

