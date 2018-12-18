#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
import re

from db_work import Postgres
from keyboard import keyboard, basic
from log_cmd import Selector
from math_pars import formula

s = Selector()
p = Postgres()


def clear(vk_text, vk_obj):
    vk_text = vk_text.replace(',', '')
    clr = vk_text.split(']', 1)
    roll = str(clr[1])
    clr = roll.strip()
    return sys_sel(clr, vk_obj)


def sys_sel(clr, vk_obj):
    d = re.compile('\Adnd\s|\Adnd|\Ad\s|\Ad')
    c = re.compile('\Aecl\s|\Aecl|\Ae\s|\Ae')
    e = re.compile('\Acor\s|\Acor|\Ac\s|\Ac')
    set = re.compile('\AChangelog')
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
    elif re.match(set, clr):
        return changelog()
    else:
        return db_sys(clr, vk_obj)


def db_sys(clr, vk_obj):
    d = re.compile('\AD&D\s|\AD&D')
    c = re.compile('\ACoriolis\s|\ACoriolis')
    e = re.compile('\AEclipse Phase\s|\AEclipse Phase')
    f = re.compile('\AFate Core\s|\AFate Core')
    sel = re.compile('\AD&D|\ACoriolis|\AEclipse Phase|\AFate Core')
    unsel = re.compile('\Aunselect\s|\Aunselect')
    set = re.compile(
        '\AНастройки|\AТекущая система|\AУдалить выбор|\AChangelog|\AВозврат|\AВыбор системы|\Aregister chat')

    if re.match(unsel, clr):
        out = p.unselect(vk_obj.obj.from_id)
        return str(out)
    # Проверка на пункты настроек
    elif re.match(set, clr):
        k = str(kbd(clr, vk_obj))
        return k
    elif p.read(vk_obj.obj.from_id) != '0':
        sys = p.read(vk_obj.obj.from_id)
        if re.match(d, sys):
            return dnd(clr)
        elif re.match(c, sys):
            return coriolis(clr)
        elif re.match(f, sys):
            return fatecore(clr)
        elif re.match(e, sys):
            return eclipse(clr)
        else:
            p.unselect(vk_obj.obj.from_id)
            return 'Ошибка в названии системы. Данные из БД удалены. Выберите систему заново.'
    elif re.match(sel, clr):
        out = p.update(vk_obj.obj.from_id, clr)
        return str(out)
    else:
        return 'Select system by dnd, cor, ecl, fate'


def kbd(clr, vk_obj):
    if re.match('\AНастройки', clr):
        keyboard(1, vk_obj)
        return 'Opened'
    elif re.match('\AТекущая система', clr):
        out = str(p.read(vk_obj.obj.from_id))
        return out
    elif re.match('\AУдалить выбор', clr):
        p.unselect(vk_obj.obj.from_id)
        return 'Выбор системы удален'
    elif re.match('\AВозврат', clr):
        basic(vk_obj)
        return 'Основное'
    elif re.match('\AВыбор системы', clr):
        keyboard(2, vk_obj)
        return 'Выбора системы'
    elif re.match('\Aregister chat', clr):
        if vk_obj.obj.from_id == 5050831:
            return 'Чат зарегестрирован'
        else:
            return 'Не Админ.'
    else:
        return 'Keyboard exception'



def dnd(clr):
    return s.sel_dnd(clr)


def coriolis(clr):
    return s.sel_cor(clr)


def fatecore(clr):
    return s.sel_dnd(clr)


def eclipse(clr):
    return s.sel_ecl(clr)


def changelog():
    log = open('changelog.txt', 'r', encoding='utf-8')
    return log.read()

def logs(sys, text, name):
    log = str(name) + " " + str(text) + "\n"
    r_log = open('logs.txt', "a", encoding='utf-8')
    r_log.write(log)
    r_log.close()
