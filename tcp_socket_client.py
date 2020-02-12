#!/user/bin/env python3

import socket
import base64


# 客户端

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# s.connect(("www.sina.com.cn", 80))
# s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# buffer = []
# while True:
# 	d = s.recv(1024)
# 	if d:
# 		buffer.append(d)
# 	else:
# 		break

# data = b''.join(buffer)
# s.close()

# header, html = data.split(b'\r\n\r\n',1)
# print(header.decode('utf-8'))
# with open('sina.html','wb') as f:
# 	f.write(html)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 9999))
# 接收欢迎消息:
print(s.recv(1024).decode('utf-8'))
for data in [b'Lennon', b'Tracy', b'Sarah',b"abc",b"ABC"]:
    # 发送数据:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()

