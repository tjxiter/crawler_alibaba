#!/usr/bin/python
#coding:UTF-8

import sys
sys.path.append('.')
sys.path.append('../')
reload(sys)
sys.setdefaultencoding("utf-8")
import time
import urllib2
import re
import json

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from openpyxl import Workbook


all_items = ["City", "Fax", "Country/Region", "name", "Zip", "Telephone", "Mobile Phone", "Address", "Province/State"]

def crawl_all(source_file, destination_file, continue_file):

    f = open(source_file, 'r')
    ffprofile = webdriver.FirefoxProfile('/Users/tjx/Library/Application Support/Firefox/Profiles/tiffgp2i.default')
    driver = webdriver.Firefox(firefox_profile=ffprofile)
    driver.set_page_load_timeout(20)
    driver.get('http://www.alibaba.com')

    cc = None
    # get continue point
    fc = open(continue_file, 'r')
    for one in fc.readlines():
        cc = one
        break
    fc.close()

    go = False # True：才开始爬联系方式
    # 第一次需要手动输入密码
    cnt = 1

    conss = []
    for one in f.readlines():
        if go == False:
            if not cc:
                go = True
            elif one == cc:
                go = True
            else:
                continue

        if go:
            cons = crawl_ali_contact(driver, one)
            print cnt
            if cnt == 1:
                time.sleep(20)
            else:
                time.sleep(5)

            cnt += 1
            if cons is not None:
                conss.append(cons)

                f = open(destination_file, 'a')
                f.write('''%s\n''' % json.dumps(cons))

                if len(one) > 20:
                    fc = open(continue_file, 'w')
                    fc.write(one)
        '''
        # 保存为csv
        # create_csv(conss)

        #保存文件
        text = ''
        for one in conss:
            text = '%s\n%s' % (text, one)

        f = open(destination_file, 'a')
        f.write(text)
        '''
    f.close()
    fc.close()


def crawl_ali_contact(driver, url):

    t1 = time.time()
    print url
    try:
        driver.get(url)
        page = driver.page_source

        t2 = time.time()
        print 't2-t1: %s' % (t2-t1)

        soup = BeautifulSoup(page, "lxml")

        t3 = time.time()
        print 't3-t2: %s' % (t3-t2)

        contact_url = soup.find('td', {'class': 'action-contact'}).a.get('href')
        print 'contact_url: %s' % contact_url

        cons = get_contact(driver, contact_url)
        return cons

    except TimeoutException:
        print 'timeout..............'
        return None
    except Exception, e:
        print e
        return None


def get_contact(driver, con_url):

    if con_url is None:
        return None
    try:
        driver.get(con_url)
        soup = BeautifulSoup(driver.page_source, "lxml")
        info = {}
        overview = soup.find('div', {'class': 'contact-overview'}).find('div', {'class': 'contact-info'})

        info["name"] = str(overview.h1.text.strip())
        details = soup.find('div', {'class': 'contact-detail'})

        k = details.findAll('dt')
        v = details.findAll('dd')
        for i in range(len(k)):
            info[str(k[i].text[:-1])] = str(v[i].text) if v[i].text else "None"

        # phone_url 要经常换，因为会过期
        #phone_url = 'https://lihuacarbide.en.alibaba.com/event/app/contactPerson/showContactInfo.htm?encryptAccountId=IDX12JoLPO9gXWrs-0IDjwFAvxh3XcYTygWawT_n8hNyJZnTi-8dA257Qr3QEDh6QXcA'
        phone_url = 'https://oshenda.en.alibaba.com/event/app/contactPerson/showContactInfo.htm?encryptAccountId=IDX1kJ0WNSgFGJue6gJ-5303DPpwNhyB9J1sDv0A063jt8IwOjUmlISmHU5CGPq0krvX'
        driver.get(phone_url)

        soupp = BeautifulSoup(driver.page_source, "lxml")
        soup_dict = json.loads(soupp.find('pre').text)

        info["Telephone"] = str(soup_dict['contactInfo']['accountPhone'])
        info["Fax"] = str(soup_dict['contactInfo']['accountFax'])
        info["Mobile Phone"] = str(soup_dict['contactInfo']['accountMobileNo'])

        global all_items
        for one in all_items:
            if one not in info:
                info[one] = "None"
    except TimeoutException:
        return None

    print info
    return info


def create_csv(data, file_name="tmp.csv"):

    wb = Workbook()
    ws = wb.active

    ws.append(all_items)

    for one in data:
        r = []
        for k, v in one.items():
            r.append(v)
        ws.append(r)

    ws.column_dimensions['D'].width = 80
    wb.save(file_name)


if __name__ == "__main__":
    crawl_all('sample.txt')
