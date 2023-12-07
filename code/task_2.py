#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    sentence = input("Enter a sentence: ")
    counter = 0
    comma_index = sentence.find(",")

    if comma_index != -1:

        for letter in sentence[:comma_index]:
            if letter.lower() == "н":
                counter += 1
        print(f"The number of letters 'н' preceding the first comma: {counter}")
    else:

        for letter in sentence:
            if letter.lower() == "н":
                counter += 1

        print('There are no commas!')

        print(f"Number of letters 'н': {counter}")

