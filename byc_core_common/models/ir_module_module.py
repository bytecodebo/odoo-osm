import logging

from odoo import api, fields, models
from odoo.modules.module import get_module_path

_logger = logging.getLogger(__name__)


class IrModule(models.Model):
    _inherit = 'ir.module.module'

    finding_path = fields.Boolean(default=True, compute="_compute_finding_path", store=True)

    @api.depends('icon', 'icon_image', 'state')
    def _compute_finding_path(self):
        for rec in self:
            check_pack = rec.finding_path
            exist_path = get_module_path(rec.name, display_warning=True)
            if not exist_path:
                check_pack = False
            if check_pack != rec.finding_path:
                rec.finding_path = check_pack

    def module_multiple_uninstall(self):
        # we select ids of the selected modules using active_ids and then perform button_immediate_uninstall()
        module_ids = self.browse(self.env.context.get('active_ids')).button_immediate_uninstall()
        return True