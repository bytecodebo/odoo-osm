from odoo import fields, models, api, _


class WebWidgetBaseTest(models.AbstractModel):
    _name = 'web.widget.base.test'
    _description = 'Base Test Abstract'

    @api.model
    def _default_company_id(self):
        return self.env.user.company_id.id

    @api.model
    def _default_user_id(self):
        return self.env.user.id

    id = fields.Id()
    name = fields.Char(
        string="# Document",
        default="/",
        required=True,
        copy=False,
        readonly=True,
        states={"draft": [("readonly", False)]},
    )
    company_id = fields.Many2one(
        string="Company",
        comodel_name="res.company",
        required=True,
        default=lambda self: self._default_company_id(),
        copy=True,
    )
    company_partner_id = fields.Many2one(
        string="Company Partner",
        related="company_id.partner_id",
        store=False,
    )
    user_id = fields.Many2one(
        string="Responsible",
        comodel_name="res.users",
        required=True,
        default=lambda self: self._default_user_id(),
        copy=False,
        readonly=True,
        states={"draft": [("readonly", False)]},
    )
    state = fields.Selection(selection=[('draft', 'Draft'),('posted', 'Posted'), ('cancel', 'Cancelled')],
                             string='Status', required=True, copy=False, default='draft')
