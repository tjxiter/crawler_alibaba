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
    'CID33904', 'CID33905', 'CID32801', 'CID33913', 'CID32212', 'CID324',
]


if __name__ == "__main__":
    for i in range(6):
        t = threading.Thread(target=common.crawl_all, args=('fashion.txt', [cids[i]],))
        t.start()
