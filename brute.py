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
parser.add_argument(
    "-d", "--directory",
    required=True,
    help="The directory that will receive the requests. Example: /login, /admin, etc."
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
print(f'\nDirectory: {args.directory}')
print(f'\nUser: {args.user}')
print(f'\nWord list: {args.word_list}')
print(f'\nUser field: {args.user_field}')
print(f'\nPassword field: {args.password_field}\n')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(0.5)
print(client, '\n')


