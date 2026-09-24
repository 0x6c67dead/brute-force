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
from pathlib import Path

parser = argparse.ArgumentParser()

parser.add_argument(
    "target",
    help="Target host or IP address."
)

parser.add_argument(
    "-p", "--port",
    type=int,
    required=True,
    help="Target TCP port."
)

parser.add_argument(
    "-d", "--path",
    required=True,
    help="Path of the endpoint that will receive the requests. Example: /login, /admin, etc."
)

parser.add_argument(
    "-u", "--user",
    required=True,
    help="The username to use in the brute-force attempts. Example: admin, admin@example.com, etc."
)

parser.add_argument(
    "-w", "--word-list",
    required=True,
    help="Path to the wordlist containing the passwords to try. Example: /usr/share/wordlists/rockyou.txt"
)

parser.add_argument(
    "--user-field",
    default="username",
    help="Name of the form field used for the username. Example: user, username, email, etc."
)

parser.add_argument(
    "--password-field",
    default="password",
    help="Name of the form field used for the password. Example: pass, password, passwd, etc."
)

args = parser.parse_args()

print(f'\nTarget: {args.target}')
print(f'TCP port: {args.port}')
print(f'Path: {args.path}')
print(f'User: {args.user}')
print(f'Word list: {args.word_list}')
print(f'User field: {args.user_field}')
print(f'Password field: {args.password_field}\n')


path = Path(args.word_list)

if not path.exists():
    print('Invalid path: file does not exist.')
    exit(1)

if path.is_dir():
    print('Invalid path: expected a file, but got a directory.')
    exit(1)

print(f'"{path}" is a valid file!\n')

with open(path, 'r') as file:
    index = 1 
    for line in file:
        print(f'{index}º attempt: {args.user_field}:{args.user}&{args.password_field}:{line.strip()}')
        index += 1

target_ip = socket.gethostbyname(args.target)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(0.5)

client.connect((target_ip, args.port))
print('\n', client, '\n')


