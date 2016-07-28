#!/usr/bin/python
#coding:UTF-8

import threading

import common


if __name__ == "__main__":
    cids = ['CID33904', 'CID33905', 'CID32801', 'CID33913', 'CID32212', 'CID324']
    lens = len(cids)

    for i in range(lens):
        t = threading.Thread(target=common.crawl_all, args=('fashion.txt', [cids[i]],))
        t.start()
