#! /usr/bin/env python3
# encoding: utf-8
"""
    manages.py
Created by PythonStudy on 2017/5/27 下午4:52
Copyright 2017 azhen All rights reserved.
"""

from multiprocessing import Process, Manager
import os


def f(d, l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.append(os.getpid())
    print(l)


if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()

        l = manager.list(range(5))
        p_list = []
        for i in range(10):
            p = Process(target=f, args=(d, l))
            p.start()
            p_list.append(p)
        for res in p_list:
            res.join()

        print(d)
        print(l)