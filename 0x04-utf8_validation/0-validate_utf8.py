#!/usr/bin/python3
"""
Module that determines if
a given data set reps a valid UTF-8
encoding
"""


def validUTF8(data):
    """
    Function that determines if
    a given data set reps a valid UTF-8
    encoding
    """
    bytes = 0
    for byte in data:
        byte = byte & 255
        if bytes:
            if byte >> 6 != 2:
                return False
            bytes -= 1
            continue
        while (1 << abs(7 - bytes)) & byte:
            bytes += 1
        if bytes == 1 or bytes > 4:
            return False
        bytes = max(bytes - 1, 0)
    return bytes == 0
