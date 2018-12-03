#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
import re

from log_cmd import Selector
from math_pars import formula

s = Selector()


def clear(vk_text, id):
    vk_text = vk_text.replace(',', '')
    clr = vk_text.split(']', 1)
    roll = str(clr[1])
    clr = roll.strip()
    return sys_sel(clr, id)


def sys_sel(clr, id):
    d = re.compile('\Adnd\s|\Adnd|\Ad\s|\Ad')
    c = re.compile('\Aecl\s|\Aecl|\Ae\s|\Ae')
    e = re.compile('\Acor\s|\Acor|\Ac\s|\Ac')
    sel = re.compile('\Aselect\s|\Aselect')
    if re.match(d, clr):
        clr = re.sub('\Adnd\s|\Adnd|\Ad\s|\Ad\s', "", clr)
        return s.sel_dnd(clr)
    elif re.match(c, clr):
        clr = re.sub(c, "", clr)
        print(clr)
        return s.sel_ecl(clr)
    elif re.match(e, clr):
        clr = re.sub(e, "", clr)
        print(clr)
        return s.sel_cor(clr)
    elif re.match('\Amath\s', clr):
        clr = clr[5:]
        return formula(clr)
    elif re.match('\d+d\d+', clr):
        return s.dice(clr)
    #    elif re.match(sel, clr):

    else:
        return 'Select system: dnd, ecl, cor'


def logs(sys, text, name):
    log = str(name) + " " + str(text) + "\n"
    r_log = open('logs.txt', "a", encoding='utf-8')
    r_log.write(log)
    r_log.close()
