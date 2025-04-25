# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class byc_web_settings(models.Model):
#     _name = 'byc_web_settings.byc_web_settings'
#     _description = 'byc_web_settings.byc_web_settings'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
