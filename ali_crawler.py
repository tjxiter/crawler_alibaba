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


'''
apparel: 10
Textiles & Leather Products: 8
Fashion: 6
Timepieces: 4
'''
cids = [
    'CID100003244', 'CID100003109', 'CID328', 'CID301', 'CID100003070', 'CID100003241', 'CID100003199', 'CID100005786', 'CID100005769', 'CID100003234',
    'CID405', 'CID423', 'CID100000941', 'CID408', 'CID100000948', 'CID415', 'CID100000938', 'CID100000936'
    'CID33904', 'CID33905', 'CID32801', 'CID33913', 'CID32212', 'CID324',
    'CID1509', 'CID1511', 'CID1512', 'CID1528'
]

url = 'https://www.alibaba.com/catalogs/products/%s'


def crawl_all():

    br = webdriver.Firefox()
    global cids

    all_urls = []
    for cid in cids:
        print cid
        ali_url = url % cid
        urls = crawl_ali_contact(br, cid, ali_url)
        all_urls.extend(urls)

    f = open('product_url.txt', 'w')
    text = ''
    for one in all_urls:
        text = '%s\nhttp://%s' % (text, one)
    f.write(text)


def crawl_ali_contact(br, cid, ali_url):

    br.get(ali_url)
    soup = BeautifulSoup(br.page_source)
    nav_item = soup.find_all("div", attrs={"class": "l-theme-card-box uf-theme-card-border uf-theme-card-margin-bottom"})[1]
    total_page = int(nav_item.find('div', {'class': 'ui2-pagination-pages'}).findAll('a')[-2].text)

    urls = []
    for i in range(total_page):
        page_url = '%s/%s' % (ali_url, i + 1)
        print page_url
        br.get(page_url)
        soup = BeautifulSoup(br.page_source)

        order = 1 if i == 0 else 0
        nav_item = soup.find_all("div", attrs={"class": "l-theme-card-box uf-theme-card-border uf-theme-card-margin-bottom"})[order]

        navs = nav_item.findAll('div', {'class': 'm-product-item'})
        for nav in navs:
            try:
                content = nav.find('div', {'class': 'item-content'})
                url = content.find('div', {'class': 'item-grid'}).find('div', {'class': 'item-sub'}).find('a', {'class': 'util-valign-ctn'}).get('href')
                urls.append(url[2:])
            except Exception, e:
                pass
    return urls


if __name__ == "__main__":
    crawl_all()
