#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

from sympy.parsing.sympy_parser import parse_expr


def formula(inp_form):
    try:
        math_result = parse_expr(str(inp_form))
        return str(math_result)
    except Exception:
        return 'Input Error'
