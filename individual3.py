#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == "__main__":
    word = input("Введите слово: ")
    s = int(input("Введите номер буквы, которую желаете переставить: "))
    k = int(input("Введите номер буквы, на место которой желаете поставить введённую букву: "))

    s -= 1
    k -= 1

    st = word[s]
    temp = word[0:s]
    temp2 = word[k + 1]
    word = word[s+1:k + 1]

    print(temp + word + st + temp2)