#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente UDP que abre un socket a un servidor
"""

import socket
import sys

# Constantes. Dirección IP del servidor y contenido a enviar
try:
	IP = sys.argv[1]
	PORT = int(sys.argv[2])
	#LINE = ' '.join(sys.argv[3:])
	REGISTER = sys.argv[3]
	USER = sys.argv[4]
	EXPIRES = int(sys.argv[5])
except:
	sys.exit("Usage: client.py ip puerto register sip_address expires_value")


# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((IP, PORT))

    if REGISTER == 'register':
        LINE = 'REGISTER sip: ' + str(USER) + ' ' + 'SIP/2.0\r\nExpire: ' + str(EXPIRES)

    print(LINE)
    my_socket.send(bytes(LINE, 'utf-8'))
    data = my_socket.recv(1024)
    print(data.decode('utf-8'))

print("Socket terminado.")