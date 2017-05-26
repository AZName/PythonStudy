#! /usr/bin/env python3
# encoding: utf-8
"""
    thread.py
Created by PythonStudy on 2017/5/26 下午4:17
Copyright 2017 azhen All rights reserved.
"""

import threading
import time


# def sayhi(num):  # 定义每个线程要运行的函数
#
#     print("running on number:%s" % num)
#
#     time.sleep(3)
#
#
# if __name__ == '__main__':
#     t1 = threading.Thread(target=sayhi, args=(1,))  # 生成一个线程实例
#     t2 = threading.Thread(target=sayhi, args=(2,))  # 生成另一个线程实例
#
#     t1.start()  # 启动线程
#     t2.start()  # 启动另一个线程
#
#     print(t1.getName())  # 获取线程名


class MyThread(threading.Thread):
    def __init__(self, n):
        super(MyThread, self).__init__()
        self.n = n

    def run(self):
        print(self.n)


th = MyThread("1")

th.start()  
