#!/usr/bin/env python
import sys, argparse

# Pigpen ASCII 
# Jhonathan Davi A.K.A jh00nbr - http://jhonathandavi.com.br
# Blog: lab.insightsecurity.com.br
# Github: github.com/jh00nbr
# Twitter @jh00nbr
# Reference: https://github.com/OHamm/Crypto/blob/8ad3eba89b68113df3271a0d3f443546f5091d3f/Pigpen.py

# -.| |- -| -.| |=| |.=| _| \/ |_ |- |-

key = {'a' : '_|', 'b' : '|_|', 'c' : '|_', 'd' : '=|', 'e' : '|=|', 'f' : '|=', 'g' : '-|', 'h' : '|-|', 'i' : '|-', 'j' : '_.|','k' : '|._|', 'l' : '|._','m' : '=.|', 'n' : '|.=|', 'o' : '|.=', 'p' : '-.|', 'q' : '|.-|', 'r' : '|.-', 's' : '\\/', 't' : '>', 'u' : '<', 'v' : '/\\', 'w' : '\\./', 'x' : '.>', 'y' : '<.', 'z' : '/.\\', ' ' : '   ', '{':'{', '}':'}', '$': '$', '(': '(', ',': ',', '0': '0', '1':'1', '2':'2', '3':'3', '4': '4', '5':'5', '6':'6', '7':'7',  '8': '8', '9':'9', '<': '<', '@': '@','|': '|','#': '#', "'": "'", '+': '+', '/': '/', ';': ';', '?': '?', '[': '[', '_': '_', '&': '&', '*': '*', '.': '.', '!':'!','-':'-',':':':',' ':' '}

key_decipher = dict(zip(key.values(),key.keys()))

def cipher(msg):
    result = []
    msg = msg.lower()
    for _ in msg:
        result.append(key[_])
    return result

def decipher(msg_cipher):
    result = []
    for _ in msg_cipher:
        result.append(key_decipher[_])
    return ''.join(result)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Pigpen cipher ASCII', prog='Pigpen_ascii', formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=100,width=200))
    parser.add_argument("-encrypt", "--encrypt", required=False)
    parser.add_argument("-decrypt", "--decrypt", required=False)
    args = parser.parse_args()

    cipher_v = args.encrypt
    decipher_v = args.decrypt

    try:
	if cipher_v:
	        print 'CIPHED:' ,' '.join(cipher(cipher_v))

    except Exception as f:
        print './pigpen_ascii.py --encrypt <message>',



