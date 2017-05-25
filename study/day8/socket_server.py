#! /usr/bin/env python3
# encoding: utf-8
"""
    socket_server.py
Created by PythonStudy on 2017/5/25 下午2:02
Copyright 2017 azhen All rights reserved.
"""

import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        while True:
            self.data = self.request.recv(1024).strip()
            print(f"这是 data {self.data}")
            print("{} wrote:".format(self.client_address[0]))
            print(self.data)
            if not self.data:
                print("链接断开")
                break
            # just send back the same data, but upper-cased
            self.request.sendall(self.data.upper())
            # try:
            #     self.data = self.request.recv(1024).strip()
            #     print(f"这是 data {self.data}")
            #     print("{} wrote:".format(self.client_address[0]))
            #     print(self.data)
            #     # just send back the same data, but upper-cased
            #     self.request.sendall(self.data.upper())
            # except ConnectionResetError as e:
            #     print(e)
            #     break



if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    # server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)
    server = socketserver.ForkingTCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()