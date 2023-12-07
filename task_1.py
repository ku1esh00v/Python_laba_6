#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    counter = 0
    sentence = input('Enter a sentence: ')

    for letter in sentence:

        if letter.lower() == 'и':
            # Добавил счётчик кол-ва букв "и" в строке: считаю это полезным.
            counter += 1
            print(letter)

    print(f'Number of letters "и": {counter}')