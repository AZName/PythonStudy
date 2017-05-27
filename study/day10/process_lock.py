#! /usr/bin/env python3
# encoding: utf-8
"""
    process_lock.py
Created by PythonStudy on 2017/5/27 下午5:30
Copyright 2017 azhen All rights reserved.
"""
from multiprocessing import Process, Lock


def f(l, i):
    l.acquire()
    try:
        print('hello world', i)
    finally:
        l.release()


if __name__ == '__main__':
    lock = Lock()

    for num in range(100):
        Process(target=f, args=(lock, num)).start()
