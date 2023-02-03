import random


def open_text():
    f = open("text.txt", encoding="utf-8")
    s = f.readlines()
    if len(s) != 0:
        return s[random.randrange(len(s))]