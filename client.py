#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente UDP que abre un socket a un servidor
"""

import socket  	#importacion del modulo socket
import sys

# Constantes. Dirección IP del servidor y contenido a enviar

IP = sys.argv[1]
PORT = int(sys.argv[2])
#LINE = ' '.join(sys.argv[3:])
REGISTER = sys.argv[3]
USER = sys.argv[4]

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((IP, PORT))	#nos conectamos a un servidor

    if REGISTER == 'register':
        LINE = 'REGISTER sip:' + USER + ' ' + 'SIP/2.0\r\n'

    print(LINE)
    my_socket.send(bytes(LINE, 'utf-8'))	#enviamos una secuencia de bytes por el socket
    data = my_socket.recv(1024)	#leemos del socket
    print(data.decode('utf-8'))

print("Socket terminado.")