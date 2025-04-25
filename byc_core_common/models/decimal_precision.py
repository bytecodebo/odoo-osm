from odoo import models, fields, api, tools


class DecimalPrecision(models.Model):
    _inherit = 'decimal.precision'

    def name_get(self):
        result = []
        for rec in self:
            display_name = "[%sd] %s" % (rec.digits,rec.name)
            result.append((rec.id, display_name))
        return result

    name = fields.Char('Usage', index=True, required=True)
    precision_id = fields.Many2one('decimal.precision', string="Pre. by default")
    digits = fields.Integer('Digits', required=True, default=2, compute='_compute_precision', store=True)
    enable_filter = fields.Boolean(default=False)

    @api.depends('precision_id')
    def _compute_precision(self):
        for rec in self:
            digits = rec.digits or 2
            if rec.precision_id:
                digits = rec.precision_id.digits
            if digits != rec.digits:
                rec.digits = digits

    @api.model
    @tools.ormcache('application')
    def precision_get(self, application):
        # self.flush_model(['name', 'digits'])
        # self.env.cr.execute('select digits from decimal_precision where name=%s', (application,))
        # res = self.env.cr.fetchone()
        # return res[0] if res else 2
        # print(application)
        return super().precision_get(application)

    @api.model
    @tools.ormcache('self.env.company.id', 'model_name', 'field_name', 'doc_sector_id')
    def precision_dynamic_get(self, model_name, field_name, doc_sector_id):
        """ params:
                company_id = %s and  % 1
                model_name = %s and % account.move
                field_name = %s and  % amount_tax
                (doc_sector_id = %s or code = %s) % 35   -- Code
                or precision = %s   % '5 digits' -- name of precision
                return digits
        """

        self.flush_model(['name', 'digits', 'precision_id', 'enable_filter'])
        sql_query = """
            select digits from siat_doc_sector_precision where company_id=%s and model_name=%s
            and field_name=%s and doc_sector_id=%s          
        """
        params = [self.env.company.id, model_name, field_name, (doc_sector_id,)]
        self.env.cr.execute(sql_query, params)
        res = self.env.cr.fetchone()
        result = res[0] if res else 2
        # print(result, res)
        return result

