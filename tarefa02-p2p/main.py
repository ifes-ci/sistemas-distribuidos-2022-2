#!/usr/sbin/python3
# -*- coding: utf-8 -*-
import socket
import _thread
import json
import sys
import os


class Node:
    def __init__(self, ip):
        self.ip = ip
        self.id = hash(f"{ip}+rafael")
        self.porta = 12345
        self.sucessor = None
        self.antecessor = None


def servidor_p2p(udp, node):
    print(f"=> Iniciando servidor P2P (ip={node.ip}, porta={node.porta})")
    orig = ("", node.porta)
    udp.bind(orig)
    while True:
        msg, cliente = udp.recvfrom(1024)


def interface(node):
    while True:
        os.system("clear")
        print("######################################")
        print("# 1 - Criar uma nova rede P2P        #")
        print("# 2 - Entrar em uma rede P2P         #")
        print("# 3 - Sair da rede P2P               #")
        print("# 4 - Imprimir informações do nó     #")
        print("# 9 - Sair do programa               #")
        print("######################################")
        opc = int(input("=> "))
        if opc == 1:
            node.sucessor = {"id": node.id, "ip": node.ip}
            node.antecessor = {"id": node.id, "ip": node.ip}
            print("Rede P2P Inicializada!")
            input("Pressione ENTER para continuar")
        elif opc == 2:
            pass
        elif opc == 3:
            pass
        elif opc == 4:
            os.system("clear")
            print("#      Informações do Nó       #")
            print(f"# ID: {node.id}")
            print(f"# IP: {node.ip}")
            print(f"# Sucessor: {node.sucessor}")
            print(f"# Antecessor: {node.antecessor}")
            print("#------------------------------#")
            input("Pressione ENTER para continuar")
        elif opc == 9:
            sys.exit(0)


def main():
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    node = Node(ip=sys.argv[1])
    _thread.start_new_thread(servidor_p2p, (udp, node))
    interface(node)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main()
    else:
        print("Modo de utilização: python3 main.py <ENDEREÇO_IP>")
        sys.exit(0)
