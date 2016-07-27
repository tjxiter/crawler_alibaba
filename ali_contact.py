#!/usr/bin/python
#coding:UTF-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import time
import urllib2
import re

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException


def crawl_all():

    f = open('sample.txt', 'r')
    ffprofile = webdriver.FirefoxProfile('/Users/tjx/Library/Application Support/Firefox/Profiles/tiffgp2i.default')
    driver = webdriver.Firefox(firefox_profile=ffprofile)
    driver.get('http://www.alibaba.com')

    # 第一次需要手动输入密码
    cnt = 1

    conss = []
    for one in f.readlines():
        cons = crawl_ali_contact(driver, one)
        print cnt
        if cnt == 1:
            time.sleep(15)
            cnt += 1
        else:
            time.sleep(5)
        conss.append(cons)

    text = ''
    for one in conss:
        text = '%s\n%s' % (text, one)

    f = open('contact_infos.txt', 'w')
    f.write(text)


def crawl_ali_contact(driver, url):

    t1 = time.time()
    print url
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "html.parser")

    t2 = time.time()
    print 't2-t1: %s' % (t2-t1)

    try:
        #import pdb; pdb.set_trace()
        contact_url = soup.find('td', {'class': 'action-contact'}).a.get('href')
        print 'contact_url: %s' % contact_url

        t3 = time.time()
        print 't3-t2: %s' % (t3-t2)

        cons = get_contact(driver, contact_url)

        t4 = time.time()
        print 't4-t3: %s' % (t4-t3)
        return cons
    except Exception, e:
        print e


def get_contact(driver, con_url):

    if con_url is None:
        return

    driver.get(con_url)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    info = {}
    overview = soup.find('div', {'class': 'contact-overview'}).find('div', {'class': 'contact-info'})

    info['name'] = overview.h1.text.strip()
    details = soup.find('div', {'class': 'contact-detail'})

    k = details.findAll('dt')
    v = details.findAll('dd')
    for i in range(len(k)):
        info[k[i].text[:-1]] = v[i].text

    #import pdb; pdb.set_trace()
    print info
    return info

if __name__ == "__main__":
    crawl_all()
