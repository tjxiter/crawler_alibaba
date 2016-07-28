#!/usr/bin/pyhon
#coding:UTF-8

import threading

import common


if __name__ == "__main__":
    cids = ['CID1509', 'CID1511', 'CID1512', 'CID1528']
    lens = len(cids)

    for i in range(lens):
        t = threading.Thread(target=common.crawl_all, args=('timepieces.txt', [cids[i]],))
        t.start()
