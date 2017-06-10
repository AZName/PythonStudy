#! /usr/bin/env python3
# encoding: utf-8
"""
    s2.py
Created by PythonStudy on 2017/6/9 下午4:22
Copyright 2017 azhen All rights reserved.
"""
from wsgiref.simple_server import make_server


def RunServer(environ, start_response):
    print(environ)
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [bytes('<h1>Hello, web!</h1>', encoding='utf-8'), ]


if __name__ == '__main__':
    httpd = make_server('', 8000, RunServer)
    print("Serving HTTP on port 8000...")
    httpd.serve_forever()