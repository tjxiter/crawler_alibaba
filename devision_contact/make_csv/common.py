#!/usr/bin/python
#coding:UTF-8

from openpyxl import Workbook


def create_csv(source_file, file_name="tmp.csv"):
  
    data = []
    f = open(source_file, 'r')
    for one in f.readlines():
        data.append(one)

    wb = Workbook()
    ws = wb.active

    ws.append([u'City', u'Fax', u'Country/Region', 'name', u'Zip', u'Telephone', u'Mobile Phone', u'Address', u'Province/State'])

    for one in data:
        r = []
        for k, v in one.items():
            r.append(v)
        ws.append(r)

    ws.column_dimensions['D'].width = 80
    wb.save(file_name)

if __name__ == '__main__':
    pass
