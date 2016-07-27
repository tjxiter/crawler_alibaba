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

def crawl_all(filename, cids):

    br = webdriver.Firefox()

    all_urls = []
    for cid in cids:
        print cid
        urls = crawl_ali_contact(br, cid)
        all_urls.extend(urls)

    f = open(filename, 'a')
    text = ''
    for one in all_urls:
        text = '%s\nhttp://%s' % (text, one)
    f.write(text)


def crawl_ali_contact(br, cid):

    ali_url = 'https://www.alibaba.com/catalogs/products/%s' % cid
    br.get(ali_url)
    soup = BeautifulSoup(br.page_source, "html.parser")
    nav_item = soup.find_all("div", attrs={"class": "l-theme-card-box uf-theme-card-border uf-theme-card-margin-bottom"})[1]
    total_page = int(nav_item.find('div', {'class': 'ui2-pagination-pages'}).findAll('a')[-2].text)

    urls = []
    for i in range(total_page):
        page_url = '%s/%s' % (ali_url, i + 1)
        print page_url
        br.get(page_url)
        soup = BeautifulSoup(br.page_source, "html.parser")

        try:
            order = 1 if i == 0 else 0
            try:
                nav_item = soup.find_all("div", attrs={"class": "l-theme-card-box uf-theme-card-border uf-theme-card-margin-bottom"})[order]
            except Exception, e:
                print e
                print 1^order
                nav_item = soup.find_all("div", attrs={"class": "l-theme-card-box uf-theme-card-border uf-theme-card-margin-bottom"})[1^order]

        except Exception, e:
            pass

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
    pass
    #crawl_all()
