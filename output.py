#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

from roll_dice import droll


def res_out(in_vk):
    #        roll, res = droll(in_vk, mark)
    #        output = str(in_vk) + " " + str(roll) + " = " + str(res)
    #        output = re.sub('[(''),]', '', output)
    return droll(in_vk)


if __name__ == '__main__':
    res_out()
