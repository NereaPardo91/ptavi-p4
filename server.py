#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver    #importamos el modulo
import sys


class EchoHandler(socketserver.DatagramRequestHandler): #unica clase que maneja las peticiones
    """
    Echo server class
    """

    def handle(self):   #metodo que se ejcuta cada vez que recibimos una peticion 
        self.wfile.write(b"Hemos recibido tu peticion")
        for line in self.rfile:
            print("El cliente nos manda ", line.decode('utf-8'))
            print("IP:", self.client_address[0])
            print("Puerto:", self.client_address[1])
            
if __name__ == "__main__":
    serv = socketserver.UDPServer(('', 5060), EchoHandler)
    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
