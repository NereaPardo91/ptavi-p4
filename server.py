#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver    #importamos el modulo
import sys

P = int(sys.argv[1])

class SIPRegisterHandler(socketserver.DatagramRequestHandler): #unica clase que maneja las peticiones

    list_users = {}
    """
    Echo server class
    """

    def handle(self):   #metodo que se ejcuta cada vez que recibimos una peticion 
        #self.wfile.write(b"Hemos recibido tu peticion")
        Message = self.rfile.read().decode('utf-8')
        print("REGISTER recibido " + Message)
        Direccion_IP = self.client_address[0]
        Direccion_SIP = Message.split(':')[1].split(' ')[0]
        #print("traza: " + Direccion_SIP)
        #print("traza: " + Direccion_IP)
        self.list_users[Direccion_SIP] = Direccion_IP
        print(self.list_users)
        self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")

            
if __name__ == "__main__":
    serv = socketserver.UDPServer(('', P), SIPRegisterHandler)
    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
