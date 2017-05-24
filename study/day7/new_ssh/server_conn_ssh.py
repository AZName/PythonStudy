#! /usr/bin/env python3
# encoding: utf-8
"""
    server_conn_ssh.py
Created by PythonStudy on 2017/5/24 下午5:34
Copyright 2017 azhen All rights reserved.
"""

import socket, os

server_ssh = socket.socket()

server_ssh.bind(("localhost", 20000))

server_ssh.listen()

while True:

    conn, addr = server_ssh.accept()

    print("开始接收数据", addr)

    while True:
        data = conn.recv(1024)
        print(data.decode())
        if not data:
            print("客户端已断开")
            break
        else:
            pass
        cmd_res = os.popen(data.decode()).read()

        if not cmd_res:
            cmd_res = "输入命令有误"

        cmd_res = cmd_res.encode("utf-8")
        data_size = str(len(cmd_res)).encode("utf-8")
        print("返回数据大小", data_size)
        conn.send(data_size)
        conn.recv(1024)
        conn.send(cmd_res)
        print("发送结束", cmd_res)
    else:
        pass
else:
    pass

server_ssh.close()