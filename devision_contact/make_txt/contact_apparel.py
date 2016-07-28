#!/usr/bin/python
#coding:UTF-8

import sys
sys.path.append('.')
sys.path.append('../')
sys.path.append('../../')
import threading

import common


if __name__ == "__main__":
    common.crawl_all('../../devision_product/apparel.txt', 'contact_txt/apparel_phone.txt', 'continue_point/continue_apparel.txt')
