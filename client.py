#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente UDP que abre un socket a un servidor
"""

import socket  	#importacion del modulo socket

# Constantes. Dirección IP del servidor y contenido a enviar
SERVER = 'localhost'		#variables constantes
PORT = 6001
LINE = '¡Hola mundo!'

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((SERVER, PORT))	#nos conectamos a un servidor
    print("Enviando:", LINE)
    my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')	#enviamos una secuencia de bytes por el socket
    data = my_socket.recv(1024)	#leemos del socket
    print('Recibido -- ', data.decode('utf-8'))

print("Socket terminado.")
