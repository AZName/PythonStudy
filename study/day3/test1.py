#! /usr/bin/env python3
# encoding: utf-8
"""
    test1.py
Created by PythonItem on 2017/5/19 上午9:51
Copyright 2017 azhen All rights reserved.
"""

# 生成器只有在访问的时候才生成响应的数据
# 只记住当前的位置

from collections import Iterator

isinstance()
c = (i * 3 for i in range(2000))


def fib(max_):
    n, a, b = 0, 0, 1
    while n < max_:
        yield b
        a, b = b, a + b
        n += 1
    return "结束了"


def consumer(name):
    print(name)
    while True:
        baozi = yield
        print(f"{name}开始吃包子，吃的{baozi}馅的包子")


def producer(name):
    c = consumer("A")
    c2 = consumer("B")
    c.__next__()
    c2.__next__()
    print("开始做包子了")
    for i in range(10):
        print("这是个工厂做包子的")
        c.send(i)
        c2.send(i)

producer("阿振")
# try:
#     pass
#
# except StopIteration as a:
#
#     pass
