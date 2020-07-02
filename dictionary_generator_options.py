#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itertools
import random
import string


def generate_words():
    """Main function to generate words for broot"""
    print("Keyword Generator")
    print("B - uppercase", "L - lowercase",
          "S - special symbols", "N - digits", sep="\n")
    data_set = create_data_set()
    while (combination_len := int(input('Specfiy length: '))) <= 1:
        print("Enter integer bigger than 1!!!")
    random_words = possible_combinations(data_set, combination_len)
    write_to_file(random_words, combination_len)
    print(f"Generated {len(random_words)} unique combinations",
          "Done!", sep="\n")


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


def create_data_set():
    """Create data-set based on options"""

    data_set = ""
    options_for_data = str(input("Select Options: ")).replace(" ", "").upper()

    if "B" in options_for_data:
        data_set += string.ascii_uppercase
    if "L" in options_for_data:
        data_set += string.ascii_lowercase
    if "S" in options_for_data:
        data_set += string.punctuation
    if "N" in options_for_data:
        data_set += string.digits

    return data_set


if __name__ == "__main__":
    generate_words()
