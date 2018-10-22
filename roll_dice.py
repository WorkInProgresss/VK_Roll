#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

import random
import re


def droll(vkinput, mark):
    out = ""
    total = 0
    try:
        p = re.compile('\d+d\d+')
        dice = re.findall(p, vkinput)
        for x in dice:
            z = x.split('d')
            res, rolls = roll(int(z[0]), int(z[1]))
            out = str(out) + " " + str(x) + " " + str(rolls) + " - " + str(res) + "\n"
            total += int(res)
        msg = str(out) + ' = ' + str(total)
        return msg
    except Exception:
        return "Nope" "Oh NO"


def inp_form(vk_inp):
    form = vk_inp.replace('-', 'd')
    form = form.replace('+', 'd')
    form = form.replace('=', "")
    form = form.split('d')
    form = list((map(int, form)))
    return form


def roll(numb, dice):
    i = 0
    d_res = 0
    rolls = []

    while i < numb:
        i = i + 1
        d_throw = random.randint(1, dice)
        d_res = d_res + d_throw
        rolls.append(d_throw)

    return d_res, rolls


if __name__ == '__main__':
    roll()
