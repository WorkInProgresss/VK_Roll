import random
import re

import numpy


def droll(vkinput, mark):

    if '+' in vkinput:


        if m:

            form = inp_form(vkinput)

            d_res = roll(form[0], form[1])
            res = str(d_res[0] + form[2])
            rolls = list(d_res[1])

            if mark == 0:

                r_plus = numpy.array(rolls)
                r_plus = r_plus + form[2]
                r_plus = [r_plus, res]

                return r_plus

            else:
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

            if mark == 0:

                r_plus = numpy.array(rolls)
                r_plus = r_plus + form[2]
                r_plus = str(r_plus)

                return r_plus

            else:
                to_exp = rolls + res

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
