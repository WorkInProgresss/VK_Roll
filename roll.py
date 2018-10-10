import random
import re


def droll(vkinput, mark):

    if '+' in vkinput:
        p = re.compile('\d+d\d+[+]\d+\Z')
        m = p.match(vkinput)

        if m:
            form = inp_form(vkinput)

            d_res = roll(form[0], form[1])
            res = str(d_res[0] + form[2])
            rolls = str(d_res[1])

            to_exp = [rolls, res]

            return to_exp


        else:

            return "Error. Print help for cmd list"

    elif '-' in vkinput:
        p = re.compile('\d+d\d+[-]\d+\Z')
        m = p.match(vkinput)

        if m:
            form = inp_form(vkinput)

            d_res = roll(form[0], form[1])
            res = str(d_res[0] - form[2])
            rolls = str(d_res[1])

            to_exp = [rolls, res]

            return to_exp


        else:

            return "Error. Print help for cmd list"
    else:
        p = re.compile('\d+d\d+\Z')
        m = p.match(vkinput)

        if m:
            form = inp_form(vkinput)

            d_res = roll(form[0], form[1])
            res = str(d_res[0])
            rolls = str(d_res[1])

            to_exp = [rolls, res]

            return to_exp

        else:

            return "Error. Print help for cmd list"

    return "Что то совсем кривое. Формула 1d20+-Число"


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


def inp_form(vk_inp):
    form = vk_inp.replace('-', 'd')
    form = form.replace('+', 'd')
    form = form.replace('=', "")
    form = form.split('d')
    form = list((map(int, form)))
    return form
