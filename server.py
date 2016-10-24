#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver    
import sys

P = int(sys.argv[1])

class SIPRegisterHandler(socketserver.DatagramRequestHandler):

    list_users = {}

    """
    Echo server class
    """

    def handle(self):
        Message = self.rfile.read().decode('utf-8').split()
        Direccion_IP = self.client_address[0]
        Direccion_SIP = Message[2]
        self.list_users[Direccion_SIP] = Direccion_IP

        if int(Message[-1]) == 0:
            del self.list_users[Direccion_SIP]

        print(self.list_users)
        self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")

            
if __name__ == "__main__":
    serv = socketserver.UDPServer(('', P), SIPRegisterHandler)
    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
