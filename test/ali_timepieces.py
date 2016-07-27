#!/usr/bin/python
#coding:UTF-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import time
import urllib2
import re
import threading

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException

import common

'''
apparel: 10
Textiles & Leather Products: 8
Fashion: 6
Timepieces: 4
'''
cids = [
    'CID1509', 'CID1511', 'CID1512', 'CID1528'
]


if __name__ == "__main__":
    threads = []
    for i in range(4):
        t = threading.Thread(target=common.crawl_all, args=('timepieces.txt', [cids[i]],))
        t.start()
