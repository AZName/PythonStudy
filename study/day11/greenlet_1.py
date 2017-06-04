#! /usr/bin/env python3
# encoding: utf-8
"""
    greenlet_1.py
Created by PythonStudy on 2017/5/31 上午10:07
Copyright 2017 azhen All rights reserved.
"""

from greenlet import greenlet

from greenlet import greenlet


def test1():
    print(12)
    gr2.switch()
    print(34)
    gr2.switch()


def test2():
    print(56)
    gr1.switch()
    print(78)


gr1 = greenlet(test1)  # 生成 并执行
gr2 = greenlet(test2)  # 生成 并执行
gr1.switch()
