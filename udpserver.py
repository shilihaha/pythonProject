# coding=utf-8


import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serversocket.bind(('192.168.206.1', 8000))

 # 与TCP不同的是UDP连接不需要建立连接

while True:
    clientsocket, addr = serversocket.recvfrom(1024)
    print('Received from %s:%s.' % addr)

    serversocket.sendto( ('Hello, %s!' % clientsocket.decode() ).encode(), addr)
