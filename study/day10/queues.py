#! /usr/bin/env python3
# encoding: utf-8
"""
    queues.py
Created by PythonStudy on 2017/5/27 下午4:06
Copyright 2017 azhen All rights reserved.
"""
#
# from multiprocessing import Process, Queue
#
#
# def f(name):
#     print(name)
#     q.put("hello")
#
#
# q = Queue()
# p = Process(target=f, args=("xiancheng",))
# p.start()
# q.get()

from multiprocessing import Process, Queue


def f(q):
    q.put([42, None, 'hello'])


q = Queue()
p = Process(target=f, args=(q,))
p.start()
print(q.get())  # prints "[42, None, 'hello']"
p.join()
