#!/usr/bin/python
#coding:UTF-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import time
import urllib2
import re

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
    'CID405', 'CID423', 'CID100000941', 'CID408', 'CID100000948', 'CID415', 'CID100000938', 'CID100000936'
]

if __name__ == "__main__":
    common.crawl_all('textiles.txt', cids)
