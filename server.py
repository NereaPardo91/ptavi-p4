#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver    
import sys
import time
import json

P = int(sys.argv[1])

class SIPRegisterHandler(socketserver.DatagramRequestHandler):

    list_users = {}

    """
    SIPRegister server class
    """

    def handle(self):

        """
        Registro
        """

        lista_datos = []
        Message = self.rfile.read().decode('utf-8').split()
        Direccion_IP = self.client_address[0]
        Direccion_SIP = Message[2]
        hora_act = time.time()
        hora_expiracion = hora_act + int(Message[-1])
        hora = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(hora_expiracion))
        self.list_users[Direccion_SIP] = Direccion_IP + ' ' + hora

        if int(Message[-1]) == 0:
            del self.list_users[Direccion_SIP]
			

        print(self.list_users)
        self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")
        fichjson = self.register2json()

    def register2json(self):
        """
        Creacion fichero json
        """
        json.dump(self.list_users, open('registered.json', 'w'))

    def registered(self):
        """
        Comprobacion existencia fichero json
        """
        try:
            with open("registered.json") as jsonFile:
                sel.list_users = json.load(jsonFile)
        except:
            pass

            
if __name__ == "__main__":
    serv = socketserver.UDPServer(('', P), SIPRegisterHandler)
    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
