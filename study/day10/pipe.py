#! /usr/bin/env python3
# encoding: utf-8
"""
    pipe.py
Created by PythonStudy on 2017/5/27 下午4:48
Copyright 2017 azhen All rights reserved.
"""

from multiprocessing import Process, Pipe


def f(conn):
    conn.send([42, None, 'hello'])
    conn.close()


if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())  # prints "[42, None, 'hello']"
    p.join()