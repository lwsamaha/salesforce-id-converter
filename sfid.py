__author__ = 'lsamaha'

char_codes = {
    "00000": 'A', "00001": 'B', "00010": 'C', "00011": 'D', "00100": 'E',
    "00101": 'F', "00110": 'G', "00111": 'H', "01000": 'I', "01001": 'J',
    "01010": 'K', "01011": 'L', "01100": 'M', "01101": 'N', "01110": 'O',
    "01111": 'P', "10000": 'Q', "10001": 'R', "10010": 'S', "10011": 'T',
    "10100": 'U', "10101": 'V', "10110": 'W', "10111": 'X', "11000": 'Y',
    "11001": 'Z', "11010": '0', "11011": '1', "11100": '2', "11101": '3',
    "11110": '4', "11111": '5'
}


def to_long_id(short_id):
    """
    Given a 15 character "short" Salesforce identifier, compute the 18 character
    Salesforce ID that matches the 15 character ID. The algorithm given by Salesforce is as follows:
    Break any 15 character Salesforce ID into 3 strings of 5 characters. Reverse the characters in each.
    Convert all uppercase alpha characters to 1. Convert any other character to 0. Find each result
    in the char lookup table. Append them to the original ID.

    :return: an 18 character Salesforce ID that matches the 15 character ID
    """
    if short_id is None or len(short_id) != 15:
        return None

    # break into 3 parts
    id_parts = [short_id[0:5], short_id[5:10], short_id[10:15]]

    # reverse each
    id_parts = [word[::-1] for word in id_parts]

    # swap 0|1 for uppercase alpha char|others, ie convert our alpha id into a binary id
    binary_parts = []
    for id_part in id_parts:
        binary_id_part = []
        # Use the list comprehension to place the binary id part into 'binary_id_part'
        [binary_id_part.append('1' if first_char.istitle() else '0') for first_char in id_part]
        # Now add this part to binary_parts which is our final goal
        binary_parts.append(''.join(binary_id_part))

    # append the matching letter code for each set of 0s and 1s to the short ID
    suffix = []
    [suffix.append(char_codes[binary_part]) for binary_part in binary_parts]

    return short_id + ''.join(suffix)

