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
    'CID100003244', 'CID100003109', 'CID328', 'CID301', 'CID100003070', 'CID100003241', 'CID100003199', 'CID100005786', 'CID100005769', 'CID100003234',
]


if __name__ == "__main__":
    common.crawl_all('apparel.txt', cids)
