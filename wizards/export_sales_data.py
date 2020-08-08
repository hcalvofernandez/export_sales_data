# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import MissingError

class ExportSalesDat(models.TransientModel):
    _name = 'export.sales.data'
    _description = 'Export Sales Data'

    def export_sales_data_action(self):
        raise MissingError(_('OK'))
