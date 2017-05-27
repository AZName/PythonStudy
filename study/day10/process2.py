#! /usr/bin/env python3
# encoding: utf-8
"""
    process2.py
Created by PythonStudy on 2017/5/27 下午4:01
Copyright 2017 azhen All rights reserved.
"""

from multiprocessing import Process
import os


def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())
    print("\n\n")


def f(name):
    info('\033[31;1mfunction f\033[0m')
    print('hello', name)


if __name__ == '__main__':
    info('\033[33;1mmain process line\033[0m')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()

