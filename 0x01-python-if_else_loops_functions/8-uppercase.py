#!/usr/bin/python3
def uppercase(str):
    uppercase_string = ""
    for i in range(0, len(str)):
        if 'a' <= str[i] <= 'z':
            ascii_value = ord(str[i]) - 32
            uppercase_string += chr(ascii_value)

        else:
            ascii_value = ord(str[i])
            uppercase_string += chr(ascii_value)

    print("{}".format(uppercase_string, end=""))
