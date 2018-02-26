# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Marca(models.Model):
    _name = 'grupo2g.marca'

    name = fields.Char("Nombre", required=True)
