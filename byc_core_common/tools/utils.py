from odoo.tools import float_round
from decimal import ROUND_HALF_UP, Decimal


def fn_round_number(n, decimals=2, rounding=ROUND_HALF_UP):
    multiplier = 10 ** (decimals + 1)
    return (n * multiplier * 2 + 1)//2/multiplier

def fn_set_round_precision(amount=0.0, precision=2, rounding=None):
    if amount == 0.0:
        return amount
    if not rounding:
        rounding = precision
    return round(float_round(amount, precision), rounding)
