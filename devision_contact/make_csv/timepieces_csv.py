#!/usr/bin/python
#coding:UTF-8

import sys
sys.path.append('.')
sys.path.append('../')
sys.path.append('../../')
import common


if __name__ == '__main__':
    common.create_csv('../make_txt/contact_txt/timepieces_phone.txt', 'timepieces.csv')
