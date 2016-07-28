#!/usr/bin/python
#coding:UTF-8

import threading

import common


if __name__ == "__main__":
    common.crawl_all('../devision_product/textiles.txt', 'contact_txt/textiles_phone.txt')
