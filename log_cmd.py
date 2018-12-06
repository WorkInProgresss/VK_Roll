#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

import re

from dndreq import d_quer
from r_choose import race, r_race, r_clear
from roll_dice import R_Dice

d = R_Dice()


class Selector:

    def sel_dnd(self, inp):

        if re.match('help|cmd', inp):
            out = open('cmd_dnd.txt', 'r', encoding='utf=8')

            return out.read()

        elif re.match('ir', inp):
            vk_text = inp[3:]

            return race(vk_text)

        elif re.match('r_ir', inp):

            return r_race()

        elif re.match('c_ir', inp):

            return r_clear()

        elif 'clr' in inp:
            log = open('logs.txt', 'w', encoding='utf-8')
            log.write('None')
            log.close()

            return "Logs Deleted"

        elif re.match('srd|sdr', inp):
            vk_text = inp[4:]
            link = d_quer(vk_text)

            return link

        elif re.match('books', inp):
            link = 'https://drive.google.com/drive/folders/0B89W9HjJUAgnVTcxdzlzN2RlbG8?usp=sharing'
            return link

        elif re.match('\d+d\d+|d\d+', inp):
            result = d.d_roll(inp)

            vk_res = str(result)
            vk_res = re.sub('[(),]', '', vk_res)

            return vk_res

        else:
            vk_text = inp
            link = d_quer(vk_text)

            return link

    def sel_ecl(self, inp):

        if re.match('help|cmd', inp):
            out = open('cmd_ecl.txt', 'r', encoding='utf=8')
            return out.read()

        elif re.match('\d+d+\Z', inp):
            result = d.e_roll(inp)
            vk_res = str(result)
            vk_res = re.sub('[(),]', '', vk_res)
            return vk_res

        elif re.match('books', inp):
            link = 'https://drive.google.com/open?id=1tn50Se62xdbIWGj1_QcbVh36Cd08NHVh'
            return link

        else:
            out = open('cmd_ecl.txt', 'r', encoding='utf=8')
            return out.read()

    def sel_cor(self, inp):

        if re.match('help|cmd', inp):
            out = open('cmd_cor.txt', 'r', encoding='utf=8')
            return out.read()

        elif re.match('books', inp):
            link = 'https://drive.google.com/open?id=1fEa8qXoCVmHIS6QvftRjOAcNe6Fx0L0Y'
            return link

        elif re.match('\d+d+\Z', inp):
            result = d.c_roll(inp)
            vk_res = str(result)
            vk_res = re.sub('[(),]', '', vk_res)
            return vk_res

        else:
            out = open('cmd_cor.txt', 'r', encoding='utf=8')
            return out.read()

    def dice(self, inp):
        result = d.d_roll(inp)

        vk_res = str(result)
        vk_res = re.sub('[(),]', '', vk_res)

        return vk_res
