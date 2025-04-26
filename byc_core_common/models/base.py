from odoo import fields, models, api, _


class Base(models.AbstractModel):
    _inherit = "base"

    # def set_round_precision(self, amount=0.0, precision=2, rounding=None):
    #     return fn_set_round_precision(amount=amount, precision=precision, rounding=rounding)
