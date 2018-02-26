# -*- coding: utf-8 -*-

from odoo import api, models
import odoo.addons.l10n_gt_extra.a_letras

class ReportAbstractPayment(models.AbstractModel):
    _name = 'grupo2g.abstract.reporte_account_payment'

    nombre_reporte = ''

    def totales(self, o):
        t = {'debito': 0, 'credito': 0}
        for l in o.move_line_ids:
            t['debito'] += l.debit
            t['credito'] += l.credit
        return t

    @api.model
    def render_html(self, docids, data=None):
        self.model = 'account.payment'
        docs = self.env[self.model].browse(docids)

        docargs = {
            'doc_ids': docids,
            'doc_model': self.model,
            'docs': docs,
            'a_letras': odoo.addons.l10n_gt_extra.a_letras,
            'totales': self.totales,
        }
        return self.env['report'].render(self.nombre_reporte, docargs)

class ReportPayment1(models.AbstractModel):
    _name = 'report.grupo2g.reporte_account_payment1'
    _inherit = 'grupo2g.abstract.reporte_account_payment'

    nombre_reporte = 'grupo2g.reporte_account_payment1'

class ReportPayment2(models.AbstractModel):
    _name = 'report.grupo2g.reporte_account_payment2'
    _inherit = 'grupo2g.abstract.reporte_account_payment'

    nombre_reporte = 'grupo2g.reporte_account_payment2'

class ReportPayment3(models.AbstractModel):
    _name = 'report.grupo2g.reporte_account_payment3'
    _inherit = 'grupo2g.abstract.reporte_account_payment'

    nombre_reporte = 'grupo2g.reporte_account_payment3'

class ReportPayment4(models.AbstractModel):
    _name = 'report.grupo2g.reporte_account_payment4'
    _inherit = 'grupo2g.abstract.reporte_account_payment'

    nombre_reporte = 'grupo2g.reporte_account_payment4'

class ReportPayment5(models.AbstractModel):
    _name = 'report.grupo2g.reporte_account_payment5'
    _inherit = 'grupo2g.abstract.reporte_account_payment'

    nombre_reporte = 'grupo2g.reporte_account_payment5'

class ReportPayment6(models.AbstractModel):
    _name = 'report.grupo2g.reporte_account_payment6'
    _inherit = 'grupo2g.abstract.reporte_account_payment'

    nombre_reporte = 'grupo2g.reporte_account_payment6'

class ReportPayment7(models.AbstractModel):
    _name = 'report.grupo2g.reporte_account_payment7'
    _inherit = 'grupo2g.abstract.reporte_account_payment'

    nombre_reporte = 'grupo2g.reporte_account_payment7'
