import socket
"""
客户端就是一个简单的程序，获取本地的主机名，并且连接到主机
通过input函数向主机发送字符串，并且等到主机的回应
整个过程是在while循环中完成的
"""
c = socket.socket()

hostname = socket.gethostname() #获取本地主机名
port = 12346

c.connect((hostname,port))
data = c.recv(1024)
print('接收消息：',data.decode(encoding='utf-8'))
while True:
    str = input('please input the string:')
    if str == '':
        break
    c.send(str.encode())
    data = c.recv(1024)
    print('client接收内容：', data.decode()) 
c.close()