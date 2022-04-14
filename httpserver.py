# coding=utf-8


import socket

# Address
HOST = ''
PORT = 8000                                              #端口设为8000，通过浏览器访问127.0.0.1：8000即可看到网页

# Prepare HTTP response
text_content = b'''HTTP/1.x 200 OK                       #通过b将字符串变成字节
Content-Type: text/html

<head>
<title>WOW</title>
</head>
<html>
<p>Wow, Python Server</p>
<IMG src="test.jpg"/>
</html>
'''

# Read picture, put into HTTP format
f = open('test.jpg','rb')
pic_content = b'''                                       #通过b将字符串变成字节
HTTP/1.x 200 OK  
Content-Type: image/jpg

'''
pic_content = pic_content + f.read()
f.close()

# Configure socket
s    = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))


# infinite loop, server forever
while True:
    # 3: maximum number of requests waiting
    s.listen(5)
    conn, addr = s.accept()
    request    = conn.recv(1024).decode("UTF-8")                #将浏览器发来的request信息解码为UTF-8格式
    method    = request.split(' ')[0]
    src            = request.split(' ')[1]


    # deal with GET method
    if method == 'GET':
        # ULR
        if src == '/test.jpg':
            content = pic_content
        else: content = text_content


        print ('Connected by', addr)
        print ('Request is:', request)
        conn.sendall(content)
    # close connection
    conn.close()