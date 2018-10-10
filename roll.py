import random
import re


def droll(vkinput, mark):
    d_res = 0

    if '+' in vkinput:
        p = re.compile('\d+d\d+[+]\d+\Z')
        m = p.match(vkinput)

        if m:
            form = vkinput.replace('+', 'd')
            form = form.replace('=', "")
            form = form.split('d')
            form = list((map(int, form)))

            d_res = roll(form[0], form[1])

            formula = str(vkinput)
            rolls = str(d_res[1])
            res = str(d_res[0] + form[2])

            return res_out(formula, rolls, res, mark)


        else:

            return "Error. Print help for cmd list"

    elif '-' in vkinput:
        p = re.compile('\d+d\d+[-]\d+\Z')
        m = p.match(vkinput)

        if m:
            form = vkinput.replace('-', 'd')
            form = form.replace('=', "")
            form = form.split('d')
            form = list((map(int, form)))

            formula = str(vkinput)
            rolls = str(d_res[1])
            res = str(d_res[0] - form[2])

            return res_out(formula, rolls, res, mark)


        else:

            return "Error. Print help for cmd list"
    else:
        p = re.compile('\d+d\d+\Z')
        m = p.match(vkinput)

        if m:
            form = vkinput.replace('=', "")
            form = form.split("d")
            form = list((map(int, form)))

            d_res = roll(form[0], form[1])

            formula = str(vkinput)
            rolls = str(d_res[1])
            res = str(d_res[0])

            return res_out(formula, rolls, res, mark)

        else:

            return "Error. Print help for cmd list"

    return "Что то совсем кривое. Формула 1d20+-Число"


def res_out(form, rolls, res, mark):
    if mark == 0:
        output = str(form) + " " + str(rolls)
        output = re.sub('[(''),]', '', output)
        return output
    else:
        output = str(form) + " " + str(rolls) + " = " + str(res)
        output = re.sub('[(''),]', '', output)

    return output


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
