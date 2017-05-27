#! /usr/bin/env python3
# encoding: utf-8
"""
    pool_process.py
Created by PythonStudy on 2017/5/27 下午5:41
Copyright 2017 azhen All rights reserved.
"""
from multiprocessing import Process, Pool
import time, os


def Foo(i):
    time.sleep(1)
    print(os.getpid(), f"\033[31;1m 这是第{i}个进程\033[0m")
    return i + 100


def Bar(arg):
    print('-->exec done:', arg, os.getpid())


pool = Pool(5)

for i in range(10):
    pool.apply_async(func=Foo, args=(i,), callback=Bar)
    # pool.apply(func=Foo, args=(i,))

print('end')
pool.close()
# pool.join()  # 进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭。
while True:
    time.sleep(1)
    print("---------")