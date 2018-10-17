#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

import re

from dndreq import d_quer
from output import res_out
from point_buy import sim
from r_choose import race, r_race, r_clear


def clear(vk_text, name):
    vk_text = vk_text.replace(',', '')
    clr = vk_text.split(']', 1)
    roll = str(clr[1])
    clr = roll.strip()
    return d_type(clr, name)


def d_type(vk_text, name):
    p = re.compile('\d+d\Z')
    m = p.match(vk_text)

    if '=' in vk_text:
        f_inp = vk_text.replace('=', "")
        return comm(f_inp, name, 1)
    elif m:
        return comm(vk_text, name, 2)
    else:
        return comm(vk_text, name, 0)


def comm(vk_text, name, mark):
    if 'rlog' in vk_text:

        num_lines = sum(1 for line in open('logs.txt', encoding='utf-8'))

        with open('logs.txt', 'r', encoding='utf-8') as lgs:
            out = lgs.readlines()

        return out

    elif re.match('help|cmd', vk_text):
        out = open('cmd.txt', 'r', encoding='utf=8')

        return out.read()

    elif re.match('ir', vk_text):
        vk_text = vk_text[3:]
        return race(vk_text)

    elif re.match('r_ir', vk_text):

        return r_race()

    elif re.match('c_ir', vk_text):

        return r_clear()


    elif 'clr' in vk_text:
        log = open('logs.txt', 'w', encoding='utf-8')
        log.write('None')
        log.close()

        return "Logs Deleted"

    elif re.match('srd|sdr', vk_text):
        vk_text = vk_text[4:]
        link = d_quer(vk_text)

        return link

    elif re.match('pb', vk_text):
        vk_text = vk_text[3:]
        tp = vk_text.split('d', 1)
        n = int(tp[0])
        d = int(tp[1])
        res = sim(n, d)
        return res


    elif ' ' in vk_text:
        tp = vk_text.split(' ', 1)
        result = res_out(tp[0], mark)
        cmt = tp[1]

        vk_res = str(result) + " {" + str(cmt) + "}"
        vk_res = re.sub('[(),]', '', vk_res)

        log_w(vk_res, name)

        return vk_res

    else:
        vk_res = res_out(vk_text, mark)
        log_w(vk_res, name)

        return vk_res


def log_w(res, name):
    log = str(name) + " " + str(res) + " "
    r_log = open('logs.txt', "a", encoding='utf-8')
    r_log.write(log)
    r_log.close()
    return
