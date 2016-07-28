#!/usr/bin/python
#coding:UTF-8

import threading

import common


if __name__ == "__main__":
    cids = [
        'CID100003244', 'CID100003109', 'CID328', 'CID301', 'CID100003070', 'CID100003241',
        'CID100003199', 'CID100005786', 'CID100005769', 'CID100003234',
    ]
    lens = len(cids)

    for i in range(lens):
        t = threading.Thread(target=common.crawl_all, args=('apparel.txt', [cids[i]],))
        t.start()
