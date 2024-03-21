#!/usr/bin/python3
if __name__ == '__main__':

    import sys

    total_sum = 0

    for n in range(1, len(sys.argv)):
        total_sum += int(sys.argv[n])
    print("{}".format(total_sum))
