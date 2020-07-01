#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itertools
import random
import string


def generate_words():
    """Main function to generate words for broot"""
    print("Keyword Generator")
    while True:
        try:
            combination_len = int(input("Specify Length: "))
            break
        except ValueError:
            print("Enter integer bigger than 0!!!")
    combination_data = string.ascii_letters + string.digits
    random_words = possible_combinations(combination_data, combination_len)
    write_to_file(random_words, combination_len)
    print(f"Generated {len(random_words)} unique combinations", "Done!", sep="\n")


def possible_combinations(combination_set, combination_length):
    """""Getting all possible combinations"""
    combinations = [''.join(x) for x in itertools.product(
        combination_set, repeat=combination_length)]
    random.shuffle(combinations)
    return combinations


def write_to_file(words, file_id):
    """""Write all possible combinations to file"""
    with open(f'num_dic{file_id}.txt', 'w') as random_choices:
        for number in words:
            random_choices.write(''.join(str(s) for s in number) + '\n')


if __name__ == "__main__":
    generate_words()
