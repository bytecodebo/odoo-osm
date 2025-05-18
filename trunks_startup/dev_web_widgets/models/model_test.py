from odoo import fields, models, api
from odoo.tools import float_round


class WebWidgetModelTest(models.Model):
    _name = 'web.widget.model.test'
    _inherit = ['web.widget.base.test']
    _description = 'TestModel'

