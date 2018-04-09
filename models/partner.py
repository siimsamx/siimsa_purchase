# -*- coding: utf-8 -*-
from openerp import fields,models

class Partner(models.Model):
    _inherit = 'res.partner'

    instructor = fields.Boolean('Empleado', default=False)