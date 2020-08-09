# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
import io, csv, base64
from odoo.exceptions import MissingError

class ExportSalesDat(models.TransientModel):
    _name = 'export.sales.data'
    _description = 'Export Sales Data'

    def export_sales_data_action(self):
        # order_recs = order_obj.search([('date_order','<=',previous_start_date),('date_order','>=',previous_new_rec_date)]).ids
        pos_orders = self.env['pos.order'].search_read([],[])
        lines = []
        for rec in pos_orders:  
            lines.append(rec)        
        with open('export_sales_data.csv', 'w') as fp:
            a = csv.writer(fp, delimiter=',')            
            data_lines = lines
            a.writerows(data_lines)
