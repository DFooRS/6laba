#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == "__main__":
    word = input("Введите слово: ")
    s = int(input("Введите номер буквы, которую желаете переставить: "))
    k = int(input("Введите номер буквы, "
                  "на место которой желаете поставить введённую букву: "))

    if s >= k:
        print("Недопустимое значение", file=sys.stderr)
        exit(1)

    s -= 1
    k -= 1

    print(word[:s] + word[s + 1:k + 1] + word[s] + word[k + 1:])