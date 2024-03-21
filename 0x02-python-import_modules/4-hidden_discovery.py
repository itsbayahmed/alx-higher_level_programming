#!/usr/bin/python3
if __name__ == '__main__':

    import hidden_4
    import re

    s = dir(hidden_4)
    for n in range(1, len(s)):
        x = re.findall(r"\A__", s[n])
        if not x:
            print(s[n])
