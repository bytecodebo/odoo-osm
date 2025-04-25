from odoo import fields, models, api


class WebWidgetModelTest(models.Model):
    _name = 'web.widget.model.test'
    _inherit = ['web.widget.base.test']
    _description = 'Model Tes Widget'

    @api.model
    def _get_default_precision(self):
        dp_id = self.env['decimal.precision'].sudo().search([], limit=1, order="id")
        return dp_id

    name = fields.Char()
    enabled = fields.Boolean(default=True)
    active = fields.Boolean(default=True)
    start_date = fields.Date(default=fields.Date.context_today)
    end_date = fields.Date()
    currency_id = fields.Many2one('res.currency')
    # amount_total = fields.Monetary(string="Total")
    # dp_amount_id = fields.Many2one(comodel_name='decimal.precision')
    # qty_amount_fd = fields.Float(string="Amount Dynamic")
    # qty_amount_currency = fields.Float(string="Amount Currency F", digits="5 Digits")
    # # qty_amount_mon = fields.FloatDynamic(string="Monetary Dynamic", currency_field='currency_id')
    # qty_amount = fields.Float(string="Amount Dynamic")
    # qty_amount_mon = fields.Float(string="Monetary Dynamic")
    #
    # dp_quantity_id = fields.Many2one(comodel_name='decimal.precision', string="dp_quantity_id")
    # dp_pu_id = fields.Many2one(comodel_name='decimal.precision', string="dp_pu_id")
    # dp_subtotal_currency_id = fields.Many2one(comodel_name='decimal.precision', string="dp_subtotal_currency_id")
    # dp_subtotal_id = fields.Many2one(comodel_name='decimal.precision', string="dp_subtotal_id")
    # dp_total_id = fields.Many2one(comodel_name='decimal.precision', string="dp_total_id")
    #
    # product_uom_qty = fields.Float(string="Quantity", help="dp_quantity_id fd")
    # price_unit = fields.Float(string="UnitPrice", help="dp_pu_id fd")
    # subtotal_amount_currency = FloatDynamic(string="subtotal_amount_currency",
    #                                                precision_field="dp_subtotal_currency_id", help="dp_subtotal_currency_id fd")
    # product_uom_qty_float = fields.Float(string="Quantity Float", precision="dp_quantity_id", help=" float")
    # price_unit_float = fields.Float(string="UnitPrice Float", help=" float")
    # amount_residual = fields.Float(string="Total Amount Due", default=0.0, store=True, help=" float")
    # montoTotal = fields.Float(digits="3 digits FD",
    #     readonly=True, states={"draft": [("readonly", False)]}, copy=False, help=" float"
    # )
    # montoTotalMoneda = fields.Float(digits="2 digits FD",
    #     readonly=True, states={"draft": [("readonly", False)]}, help=" float"
    # )
    # subtotal_amount = FloatDynamic(string="Subtotal Amount",
    #                                       precision_field="dp_subtotal_id", help="dp_subtotal_id fd")
    # total_amount = FloatDynamic(string="Total", help=" currency_field=company_currency_id fd")

    def write(self, vals):
        print('update write:::', vals)
        return super().write(vals=vals)

    @api.model_create_multi
    def create(self, vals_list):
        print(vals_list)
        return super().create(vals_list=vals_list)

    def action_recalcule(self):
        pass

