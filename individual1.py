#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    s = input("Введите предложение: ")

    print((s.count("а") / len(s)) * 100, "%")