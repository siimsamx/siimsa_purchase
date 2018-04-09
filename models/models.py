# -*- coding: utf-8 -*-
from datetime import timedelta
from odoo import models, fields, api

class Requisicion(models.Model):
		_name = 'siimsa_purchase.requisicion'
		_inherit = ['mail.thread']
		_description = "LdM"

		name 	 = fields.Char('Folio', required=True)
		tpo_com = fields.Selection([('Papeleria','Papelería'),
								 ('Limpieza','Limpieza'),
								 ('Produccion','Producción'),
								 ('Computo','Cómputo'),('Otro','Otro')],'Tipo de compra')
		pro_des = fields.Char('Proyecto/Destino')
		fec_sol = fields.Datetime('Fecha', required=True)
		nom_emp	= fields.Char('Empleado')
		des_act = fields.Text('Observaciones')
		col_cal = fields.Integer()
		listado = fields.Many2many('siimsa_purchase.lista')
		emp_ids = fields.Many2one('res.partner', 'Empleado')
		state = fields.Selection([
									('draft', ('Nuevo')), 
									('confirmed', ('En proceso')), 
									('done', ('Hecho')),
									], 'Estado', default='draft')
		
		@api.depends('fec_sol')
		def _get_end_date(self):
			for r in self:
				if not r.fec_sol:
					r.fec_sol = r.fec_sol
					continue
					print 'Ok'
					
		@api.multi
		def action_draft(self):
			self.state = 'draft'

		@api.multi
		def action_confirmed(self):
			self.state = 'confirmed'
			
		@api.multi
		def action_done(self):
			self.state = 'done'

class Lista(models.Model):
		_name = 'siimsa_purchase.lista'
		
		name = fields.Char('Material', required=True)
		des_mat	= fields.Char('Descripción', required=True)
		can_mat = fields.Float('Cantidad', required=True)
		pos_mat = fields.Char('Posición')
		uni_med = fields.Char('UdM', required=True)
		