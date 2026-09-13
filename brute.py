#!/bin/python3
print("""\033[35m
██████╗ ██████╗ ██╗   ██╗████████╗███████╗    ███████╗ ██████╗ ██████╗  ██████╗███████╗
██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝    ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝
██████╔╝██████╔╝██║   ██║   ██║   █████╗      █████╗  ██║   ██║██████╔╝██║     █████╗  
██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝      ██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝  
██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗    ██║     ╚██████╔╝██║  ██║╚██████╗███████╗
╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝    ╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝
      \033[0m""")

import argparse
import socket

parser = argparse.ArgumentParser()
parser.add_argument("alvo")
parser.add_argument("-d", '--diretorio')
parser.add_argument("-u", '--user')
parser.add_argument("-p", '--password')
parser.add_argument("-w", '--word_list')

args = parser.parse_args()

print(f'\nIP Alvo: {args.alvo}')
print(f'\ndiretorio: {args.diretorio}')
print(f'\nUser: {args.user}')
print(f'\nPassword: {args.password}\n')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(0.5)
print(client, '\n')
client.

