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
print(f'\nPath: {args.path}')
print(f'\nUser: {args.user}')
print(f'\nWord list: {args.word_list}')
print(f'\nUser field: {args.user_field}')
print(f'\nPassword field: {args.password_field}\n')


path = Path(args.word_list)

if not path.exists():
    print('Invalid path: file does not exist.')
    exit(1)

if path.is_dir():
    print('Invalid path: expected a file, but got a directory.')
    exit(1)

print(f'"{path}" is a valid file!\n')

with open(path, 'r') as file:
    for line in file:
        print(line.strip())

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(0.5)
print(client, '\n')


