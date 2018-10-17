#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

import random


def race(vk_input):
    with open('r_roll.txt', 'a') as f:
        inp = vk_input + "\n"
        f.write(inp)

    return "Race Added"


def r_race():
    num_lines = sum(1 for line in open('r_roll.txt'))
    d_throw = random.randint(0, num_lines - 1)
    f = open('r_roll.txt')
    lines = f.readlines()

    return lines[d_throw]


def r_clear():
    open('r_roll.txt', 'w')
    return 'Файл очищен'
