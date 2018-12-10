#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

import random
import re

from sympy.parsing.sympy_parser import parse_expr


class R_Dice:

    def d_roll(self, vkinput):
        try:
            p = re.compile('\d+d\d+')
            rolls_dice = ''

            for dice in re.findall(p, vkinput):
                dlist = dice.split('d')
                res, rolls = self.roll(int(dlist[0]), int(dlist[1]))
                # Формируем вывод бросков (Дайс + Броски + Итог)
                rolls_dice = rolls_dice + str(dice) + ' ' + str(rolls) + '= ' + str(res) + '\n'
                # Заменяем формулу дайса значениемм
                vkinput = re.sub(dice, str(res), vkinput)

            math_result = parse_expr(str(vkinput))

            out = "Броски \n" + str(rolls_dice) + ' ( ' + vkinput + ') = ' + str(math_result)

            return out
        except Exception:
            return 'Broad Exception'

    def c_roll(self, vkinput):

        try:
            p = re.compile('\d+d+\Z')

            if re.match(p, vkinput):
                dice = list(vkinput)
                dice[1] = 6
                # Передаем в функцию броска dice0(кол-во), dice1(стороны=6)
                d_res, rolls = self.roll(int(dice[0]), int(dice[1]))
                # Считаем успехи
                d_res = rolls.count(6)
                msg = str(rolls) + ' = ' + str(d_res) + ' Успехов'
                return msg

        except Exception:
            return 'Broad Exception'

    def e_roll(self, vkinput):

        try:
            p = re.compile('\d+d+\Z')

            if re.match(p, vkinput):
                dice = list(vkinput)
                dice[1] = 100
                # Передаем в функцию броска dice0(кол-во), dice1(стороны=6)
                d_res, rolls = self.roll(int(dice[0]), int(dice[1]))
                # Считаем успехи
                msg = str(rolls)
                return msg

        except Exception:
            return 'Broad Exception'


    def inp_form(self, vk_inp):
        form = vk_inp.replace('-', 'd')
        form = form.replace('+', 'd')
        form = form.replace('=', "")
        form = form.split('d')
        form = list((map(int, form)))
        return form

    def roll(self, numb, dice):
        i = 0
        d_res = 0
        rolls = []

        while i < numb:
            i = i + 1
            d_throw = random.randint(1, dice)
            d_res = d_res + d_throw
            rolls.append(d_throw)

        return d_res, rolls
