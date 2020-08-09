# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
import io
import csv
import base64
import os
from odoo.exceptions import MissingError


class ExportSalesDat(models.TransientModel):
    _name = 'export.sales.data'
    _description = 'Export Sales Data'

    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')

    def export_sales_data_action(self):
        pos_orders = self.env['pos.order'].search_read([('date_order','>=',self.start_date),('date_order','<=',self.end_date)], [])
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
