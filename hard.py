#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    word_1 = input('Enter the first sentence: ')
    word_2 = input('Enter the second sentence: ')

    unique_letters = ""
    result = ""

    for letter in word_1:
        if letter not in word_2:
            unique_letters += letter
            result += letter + ' '

    for letter in word_2:
        if letter not in word_1 and letter not in unique_letters:
            unique_letters += letter
            result += letter + ' '

    print(result)