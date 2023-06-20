#!/usr/bin/python3
for letter in "abcdefghijklmnopqrstuvwxyz":
    if (letter == "e" or letter == "q"):
        continue
    else:
        print("{}".format(letter), end="")
