# -*- coding: utf-8 -*-

from openerp import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    partner_id = fields.Integer(store=True)
    name = fields.Char(required=True)
    skill = fields.Float()
    years = fields.Date()
    percent = fields.Float()
    company_id = fields.Many2one(
    	"res.company",
    	"Compañia",
    	index=True
    )