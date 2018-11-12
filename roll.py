#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

import random
import re


def d_roll(vkinput):
    error = "Error. Print help for cmd list"
    err = ""
    if '+' in vkinput:

        p = re.compile('\d+d\d+[+]\d+\Z')
        m = p.match(vkinput)

        if m:

            form = inp_form(vkinput)

            d_res = roll(form[0], form[1])
            res = str(d_res[0] + form[2])
            rolls = list(d_res[1])

        else:

            return error, err

    elif '-' in vkinput:

        p = re.compile('\d+d\d+[-]\d+\Z')
        m = p.match(vkinput)

        if m:
            form = inp_form(vkinput)

            d_res = roll(form[0], form[1])
            res = str(d_res[0] - form[2])
            rolls = str(d_res[1])

            return rolls, res

        else:

            return error, err
    else:
        p = re.compile('\d+d\d+\Z')
        m = p.match(vkinput)

        if m:
            form = inp_form(vkinput)

            d_res = roll(form[0], form[1])
            res = str(d_res[0])
            rolls = str(d_res[1])

            return rolls, res

        else:

            return error, err

    return "Что то совсем кривое. Формула 1d20+-Число"


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

    d_res = [d_res, rolls]
    return d_res


if __name__ == '__main__':
    roll()
