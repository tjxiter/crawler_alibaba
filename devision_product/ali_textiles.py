#!/usr/bin/python
#coding:UTF-8

import threading

import common


if __name__ == "__main__":
    cids = ['CID405', 'CID423', 'CID100000941', 'CID408', 'CID100000948', 'CID415', 'CID100000938', 'CID100000936']
    lens = len(cids)

    for i in range(lens):
        t = threading.Thread(target=common.crawl_all, args=('textiles.txt', [cids[i]],))
        t.start()
