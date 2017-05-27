#! /usr/bin/env python3
# encoding: utf-8
"""
    process.py
Created by PythonStudy on 2017/5/27 下午3:47
Copyright 2017 azhen All rights reserved.
"""

import multiprocessing
import time, threading


def fe(name):

    time.sleep(2)
    print(name, threading.active_count())


for i in range(10):

    p = multiprocessing.Process(target=fe, args=("线程",))
    p.start()