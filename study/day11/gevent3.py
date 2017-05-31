#! /usr/bin/env python3
# encoding: utf-8
"""
    gevent3.py
Created by PythonStudy on 2017/5/31 上午10:47
Copyright 2017 azhen All rights reserved.
"""

import gevent


def task(pid):
    """
    Some non-deterministic task
    """
    gevent.sleep(0.5)
    print('Task %s done' % pid)


def synchronous():
    for i in range(1, 10):
        task(i)


def asynchronous():
    threads = [gevent.spawn(task, i) for i in range(10)]
    gevent.joinall(threads)


print('Synchronous:')
synchronous()

print('Asynchronous:')
asynchronous()
