#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == "__main__":
    s = input("Введите предложение: ")
    s += " "

    if s.startswith("к"):
        k = s.find(" ")
        print(s[:k])
    else:
        while not s.startswith("к"):
            k = s.find(" ")
            s = s[k + 1:]
            if s.startswith("к"):
                k = s.find(" ")
                print(s[:k])