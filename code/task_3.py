#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    word = input("Введите слово: ")

    result = ""

    for letter in word:
        if letter not in result:
            result += letter

    print(f"Result: {result}")
