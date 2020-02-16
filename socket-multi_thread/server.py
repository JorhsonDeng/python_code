#!/usr/bin/python
# -*- coding: UTF-8 -*-
import socket
import threading
"""
这个程序用到了多线程中间的知识
首先绑定特定的主机和端口，进入listen()状态，再进入recv的阻塞状态
当返回连接的socket套接字的时候，直接将这个套接字传入到线程对象中进行处理
调用多线程进行处理与客户端之间的通信状态
当有多个客户端进行连接的时候，会创建多个线程进行处理
"""
class serverThread(threading.Thread):
    def __init__(self,socket,addr):
        threading.Thread.__init__(self)
        self._socket = socket
        self.addr = addr
    def run(self):
        print('建立连接：',addr)
        sendstr = '已经建立连接！'
        self._socket.send(sendstr.encode())
        self.clienthandle()
    def clienthandle(self):
        while True:
            data = self._socket.recv(1024).decode(encoding='utf-8')
            if not data:
                break
            print('Server 接收消息：',data)
            data = 'Server端已经收到消息：' + data
            self._socket.send(data.encode())
        self._socket.close()    #关闭server端的socket对象
        print('关闭socket server连接：',addr)

        
if __name__ == '__main__':
    s = socket.socket()     #创建新的socket对象
    hostname = socket.gethostname() #获取本地地址
    port = 12346

    s.bind((hostname,port))     #绑定特定的地址
    s.listen(5)                 #开始监听

    while True:
        ss,addr = s.accept()
        socketobj = serverThread(ss,addr)   #创建socket线程对象
        socketobj.start()
        

        

