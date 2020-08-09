# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
import io
import csv
import base64
import os
from datetime import datetime
#from gcloud import datastore
from google.cloud import storage
from dateutil.relativedelta import relativedelta
from odoo.exceptions import MissingError


class ExportSalesDat(models.TransientModel):
    _name = 'export.sales.data'
    _description = 'Export Sales Data'

    start_date = fields.Date(
        string='Start Date',
        default=datetime.today() - relativedelta(month=1)
    )
    end_date = fields.Date(
        string='End Date',
        default=datetime.today()
    )

    def export_sales_data_action(self):
        pos_orders = self.env['pos.order'].search_read(
            [
                ('date_order','>=',self.start_date),
                ('date_order','<=',self.end_date)
            ], []
        )
        directory_file = "gcloud-storage"
        upload_file = "export_sales_data.csv"
        auth_file = "dofleini-stuffs-5a7e872105dc.json"
        my_bucket = "odoo-sales-sync"
        columnTitleRow = [pos_orders[0]]
        with open(directory_file+'/'+upload_file, 'w') as fp:
            rowWrite = csv.writer(fp, delimiter=',')
            rowWrite.writerows(columnTitleRow)
            for dic in pos_orders:
                for key in dic.keys():
                    row = str(dic[key])+","
                    fp.write(row)
                fp.write('\n')
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = directory_file+'/'+auth_file
        storage_client = storage.Client()
        bucket = storage_client.get_bucket(my_bucket)
        blob = bucket.blob('export_sales_data')
        blob.upload_from_filename(directory_file+'/'+upload_file)
        raise MissingError(blob.public_url)

