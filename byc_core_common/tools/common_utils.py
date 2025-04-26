from __future__ import print_function
from odoo.tools import float_round
from decimal import ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN

__all__ = ['fn_set_round_precision']

def fn_round_number(n, decimals=2, rounding=ROUND_UP):
    multiplier = 10 ** (decimals + 1)
    return (n * multiplier * 2 + 1)//2/multiplier

def fn_set_round_precision(amount=0.0, precision=2, rounding=ROUND_UP):
    if amount == 0.0:
        return amount
    if not rounding:
        rounding = ROUND_UP
    return round(float_round(fn_round_number(amount, precision,rounding=rounding),precision_digits=precision),ndigits=precision)
