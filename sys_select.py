#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
import re

from db_work import Postgres
from log_cmd import Selector
from math_pars import formula

s = Selector()
p = Postgres()


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
    if re.match(d, clr):
        clr = re.sub(d, "", clr)
        return s.sel_dnd(clr)
    elif re.match(c, clr):
        clr = re.sub(c, "", clr)
        return s.sel_ecl(clr)
    elif re.match(e, clr):
        clr = re.sub(e, "", clr)
        return s.sel_cor(clr)
    elif re.match('\Amath\s', clr):
        clr = clr[5:]
        return formula(clr)
    elif re.match('\d+d\d+', clr):
        return s.dice(clr)
    else:
        return db_sys(clr, id)


def db_sys(clr, id):
    d = re.compile('\AD&D\s|\AD&D')
    c = re.compile('\ACoriolis\s|\ACoriolis')
    e = re.compile('\AEclipse Phase\s|\AEclipse Phase')
    f = re.compile('\AFate Core\s|\AFate Core')
    sel = re.compile('\AD&D|\ACoriolis|\AEclipse Phase|\AFate Core')
    unsel = re.compile('\Aunselect\s|\Aunselect')

    if re.match(unsel, clr):
        out = p.unselect(id)
        return str(out)
    elif p.read(id) != '0':
        sys = p.read(id)
        if re.match(d, sys):
            return dnd(clr)
        if re.match(c, sys):
            return coriolis(clr)
        if re.match(f, sys):
            return fatecore(clr)
        if re.match(e, sys):
            return eclipse(clr)
        else:
            p.unselect(id)
            return 'Ошибка в названии системы. Данные из БД удалены. Выберите систему заново.'
    elif re.match(sel, clr):
        out = p.update(id, clr)
        return str(out)
    else:
        return 'Select system by dnd, cor, ecl, fate'


def dnd(clr):
    return s.sel_dnd(clr)


def coriolis(clr):
    return s.sel_cor(clr)


def fatecore(clr):
    return s.sel_dnd(clr)


def eclipse(clr):
    return s.sel_ecl(clr)


def logs(sys, text, name):
    log = str(name) + " " + str(text) + "\n"
    r_log = open('logs.txt', "a", encoding='utf-8')
    r_log.write(log)
    r_log.close()

# def keyboard(clr,id):
#     d = re.compile('\AD&D\s|\AD&D')
#     if re.match(d, clr):
#         return send(d)
#     else:
#         return sys_sel(clr,id)
