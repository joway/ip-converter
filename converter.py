"""
Requirements:
 - iterate the string once.
 - a string with spaces between a digit and a dot is a valid input
 - a string with spaces between two digits is not.
"""


class FormatError(Exception):
    pass


def convert_ip(ip):
    """
    :param ip: null-terminated string
    :return: 32-bit integer
    """
    count = len(ip)
    bits32 = ''
    bits8 = ''
    if ip[count - 1] != '\0':
        raise FormatError
    for pos in range(count):
        c = ip[pos]
        # verify format
        if c == ' ':
            if pos == 0 or pos == count - 1:
                raise FormatError
            if not ((ip[pos - 1].isdigit() and ip[pos + 1] == '.') or
                    (ip[pos - 1] == '.' and ip[pos + 1].isdigit())):
                raise FormatError
            continue

        if c == '.' or c == '\0':
            bits32 += f'{int(bits8):08b}'
            bits8 = ''
            continue

        # digit check
        # if not c.isdigit():
        #     raise FormatError
        # OR: trust the input
        bits8 += c
    return int(bits32, 2)
