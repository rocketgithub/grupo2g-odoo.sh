# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    codigo_viejo = fields.Char('Codigo viejo')
    marca_id = fields.Many2one('grupo2g.marca', string='Marca')
    estado = fields.Selection([
        ('en_desarrollo', 'En desarrollo'),
        ('normal', 'Normal'),
        ('fin_de_ciclo', 'Fin de ciclo'),
        ('obsoleto', 'Obsoleto'),
        ], string='Estado')
