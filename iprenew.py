import socket
import os

ip = socket.gethostbyname(socket.gethostname())
if ip[:3] == '169':
	os.system("ipconfig /release")
	os.system("ipconfig /renew")
