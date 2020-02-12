#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import socket
import base64
import hashlib
import re
import threading
import struct


host = "localhost"
port = 8080
magic_string = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"
handshake_string = "HTTP/1.1 101 Switching Protocols\r\n" \
		"Upgrade:websocket\r\n" \
		"Connection: Upgrade\r\n" \
		"Sec-WebSocket-Accept: {1}\r\n" \
		"WebSocket-Location: ws://{2}/chat\r\n" \
		"WebSocket-Protocol: chat\r\n\r\n"


def recv_data(clientSocket):
	try:
		info = clientSocket(1024)
		if not info:
			return
	except:
		return
	else:
		print(info)
		code_len = info[1] & 0x7f
		if code_len == 0x7e:
			extend_payload_len = info[2:4]
			mask = info[4:8]
			decoded = info[8:]
		elif code_len == 0x7f:
			extend_payload_len = info[2:10]
			mask = info[10:14]
			decoded = info[14:]
		else:
			extend_payload_len = None
			mask = info[2:6]
			decoded = info[6:]
		bytes_list = bytearray()
		print(mask)
		print(decoded)
		for i in range(len(decoded)):
			chunk = decode[i] ^ mask[i % 4]
			bytes_list.append(chunk)
		raw_str = str(bytes_list, encoding="utf-8")
		print(raw_str)


def send_data(clientSocket):
	data = "need to send message 中文"
	token = b"\x81"
	lenth = len(data.encode())
	if length <= 125:
		token += struct.pack("B", length)
	elif length <= 0xFFFF:
		token += struct.pack("!BH", 126, length)
	else:
		token += struct.pack("!BQ", 127, length)
	data = token + data.encode()
	clientSocket.send(data)


def handshake(serverSocket):
	while True:
		clientSocket, addressInfo = serverSocket.accept()
		request = clientSocket.recv(1024)
		print(request.decode())
		ret = re.search(r"Sec-WebSocket-Accept: (.*==)", str(request.decode()))
		if ret:
			key = ret.group(1)
		else:
			return
		Sec_WebSocket_Key = key + magic_string
		response_key = base64.b64encode(hashlib.sha1(bytes(Sec_WebSocket_Key,encoding="utf-8")).digest())
		response_key_str = str(response_key)
		response_key_str = response_key_str[2:30]
		response = handshake_string.replace("{1}",response_key_str).replace("{2}",host + ":" + str(port))
		clientSocket.send(response.encode())
		t1 = threading.Thread(target=recv_data, args=(clientSocket,))
		t1.start()
		t2 = threading.Thread(target=send_data, args=(clientSocket,))
		t2.start()


def main():
	serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	serverSocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
	serverSocket.bind((host,port))
	serverSocket.listen(10)
	print("Server runing, waiting for the connection...")
	handshake(serverSocket)


if __name__ == "__main__":
	main()
