#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

import random
import re

from sympy.parsing.sympy_parser import parse_expr


def droll(vkinput):
    out = ""
    total = 0
    try:
        p = re.compile('\d+d\d+')
        dice = re.findall(p, vkinput)
        math = re.sub(p, "", vkinput)
        math = math.replace('+-', '-')
        math = math.replace('-+', '-')
        math = math.replace('++', '+')
        math = math.replace('--', '-')
        print(math)
        for x in dice:
            z = x.split('d')
            res, rolls = roll(int(z[0]), int(z[1]))
            out = str(out) + " " + str(x) + " " + str(rolls) + " - " + str(res) + "\n"
            total += int(res)
        math_result = parse_expr(str(math))
        print(math_result)
        res_fin = total + math_result
        if total == 0:
            msg = math + " = " + str(res_fin)
        else:
            msg = str(out) + ' = ' + str(total) + ' ' + math + ' = ' + str(res_fin)
        return msg
    except Exception:
        return "Nope" " Input Error"


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
