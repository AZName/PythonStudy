#! /usr/bin/env python3
# encoding: utf-8
"""
    pachong.py
Created by PythonStudy on 2017/5/31 上午11:02
Copyright 2017 azhen All rights reserved.
"""

from gevent import monkey

monkey.patch_all()
import gevent
from urllib.request import urlopen


def f(url):
    print('GET: %s' % url)
    resp = urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))


gevent.joinall([
    gevent.spawn(f, 'https://www.python.org/'),
    gevent.spawn(f, 'https://www.yahoo.com/'),
    gevent.spawn(f, 'https://github.com/'),
])
