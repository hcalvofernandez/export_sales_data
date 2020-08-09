# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
import io
import csv
import base64
from odoo.exceptions import MissingError


class ExportSalesDat(models.TransientModel):
    _name = 'export.sales.data'
    _description = 'Export Sales Data'

    def export_sales_data_action(self):
        # pos_orders = self.env['pos.order'].search([('date_order','<=',previous_start_date),('date_order','>=',previous_new_rec_date)]).ids
        pos_orders = self.env['pos.order'].search_read([], [])
        download_file = "export_sales_data.csv"
        columnTitleRow = [pos_orders[0]]
        with open(download_file, 'w') as fp:
            rowWrite = csv.writer(fp, delimiter=',')
            rowWrite.writerows(columnTitleRow)
            for dic in pos_orders:
                for key in dic.keys():
                    row = str(dic[key])+","
                    fp.write(row)
                fp.write('\n')
