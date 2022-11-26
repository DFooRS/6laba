#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == "__main__":
    word = input("Введите слово: ")
    s = int(input("Введите № буквы, которую желаете переставить: "))
    k = int(input("Введите № буквы, на место которой нужно поставить букву: "))

    if s >= k:
        print("Недопустимое значение", file=sys.stderr)
        exit(1)

    s -= 1
    k -= 1

    print(word[:s] + word[s + 1:k + 1] + word[s] + word[k + 1:])