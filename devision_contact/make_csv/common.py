#!/usr/bin/python
#coding:UTF-8

import json

from openpyxl import Workbook


def create_csv(source_file, file_name):

    data = []
    f = open(source_file, 'r')
    for one in f.readlines():
        data.append(one)

    wb = Workbook()
    ws = wb.active

    ws.append(["City", "Fax", "Country/Region", "name", "Zip", "Telephone", "Mobile Phone", "Address", "main_markets", "Province/State"])

    for one in data:
        #import pdb; pdb.set_trace()
        tmp = json.loads(one[:-1])
        print type(tmp)
        r = []
        for k, v in tmp.items():
            r.append(v)
        print r
        ws.append(r)

    ws.column_dimensions['D'].width = 80
    print file_name
    wb.save(file_name)

if __name__ == '__main__':
    pass
