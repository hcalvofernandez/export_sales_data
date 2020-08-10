# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
import io
import csv
import base64
import os
from datetime import datetime
# from gcloud import datastore
from google.cloud import storage
from dateutil.relativedelta import relativedelta
from odoo.exceptions import MissingError


class ExportSalesDat(models.TransientModel):
    _name = 'export.sales.data'
    _description = 'Export Sales Data'

    start_date = fields.Date(
        string='Start Date',
        default=datetime.today() - relativedelta(months=1)
    )
    end_date = fields.Date(
        string='End Date',
        default=datetime.today()
    )

    def export_sales_data_action(self):
        # Settings of runtime enviroments
        directory_file = "gcloud-storage"
        upload_file = "export_sales_data_"+str(self.start_date)+"-"+str(self.end_date)+".csv"
        auth_file = "dofleini-stuffs-5a7e872105dc.json"
        my_bucket = "odoo-sales-sync"
        
        # Getting the main recordset
        main_record = self.env['pos.order.line'].search(
            [
                ('create_date', '>=', self.start_date),
                ('create_date', '<=', self.end_date)
            ]
        )

        # Getting the associated POS Orders
        pos_orders = self.env['pos.order'].search_read(
            [
                ('id', 'in', main_record.order_id.ids)
            ]
        )

        # Getting the Associated Products
        product_product = self.env['product.product'].search_read(
            [
                ('id', 'in', main_record.product_id.ids)
            ]
        )

        # Getting the Associated Partners
        res_partner = self.env['res.partner'].search_read(
            [
                ('id', 'in', main_record.order_id.partner_id.ids)
            ]
        )

        # Returning the error message for debugging
        raise MissingError(main_record)
    
        # with open(directory_file+'/'+upload_file, 'w') as fp:
        #     for pol_key in pos_order_lines[0].keys():
        #         header = "\"pos_order_line_"+str(pol_key)+"\""+","
        #     for pp_key in product_products[0].keys():
        #         header += "\"product_product_"+str(pp_key)+"\""+","
        #     for po_key in pos_orders[0].keys():
        #         header += "\"pos_order_"+str(po_key)+"\""+","
        #     for rp_key in res_partners[0].keys():
        #         header += "\"res_partner_"+str(rp_key)+"\""+","
        #     fp.write(header)
        #     for pol in pos_order_lines:
        #         for pol_k in pols.keys():
        #             row = "\""+str(pol[pol_k])+"\""+","
        #             for pp in product_products.search_read(['id', '=', pol['product_id'][0]])
        #                 for pp_k in pp.keys():
        #                     row += "\""+str(pp[pp_k])+"\""+","
        #             for po in pos_orders.search_read(['id', '=', pol['order_id'][0]])
        #                 for po_k in po.keys():
        #                     row += "\""+str(po[po_k])+"\""+","
        #                 for rp in res_partners.search_read(['id', '=', po['partner_id'][0]])
        #                     for rp_k in rp.keys():
        #                         row += "\""+str(rp[pp_k])+"\""+","
        #         fp.write(row+'\n')
        #     for dic in pos_orders:
        #         for key in dic.keys():
        #             row = "\""+str(dic[key])+"\""+","
        #             fp.write(row)
        #         fp.write('\n')
        # os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = directory_file+'/'+auth_file
        # storage_client = storage.Client()
        # bucket = storage_client.get_bucket(my_bucket)
        # blob = bucket.blob('export_sales_data')
        # blob.upload_from_filename(directory_file+'/'+upload_file)
        # raise MissingError(blob.public_url)
