#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- mode: python -*-
# vi: set ft=python :

# + /
convert_tbl = {
    '111110': '+',
    '111111': '/',
}

# A-Z
for i in range(26):
    k = f'{i:06b}'
    v = chr(i+ord('A'))
    convert_tbl[k] = v

# a-z
for i in range(26):
    k = f'{i+26:06b}'
    v = chr(i+ord('a'))
    convert_tbl[k] = v

# 0-9
for i in range(10):
    k = f'{i+26*2:06b}'
    v = chr(i+ord('0'))
    convert_tbl[k] = v

# for decode use
reverse_tbl = {v: k for k, v in convert_tbl.items()}
reverse_tbl['='] = '0' * 6


def base64_encode(bs, with_padding=True):
    '''
        receive bytes-like, return bytes-like
    '''
    s = bs.decode()
    b64 = ''
    for c in s:
        b64 += format(ord(c), '08b')
    remainer = (len(b64) // 8) % 3
    if remainer:
        padding_len = 3 - remainer
    else:
        padding_len = 0
    b64 += '0' * 8 * padding_len
    o = ''
    while b64:
        k = b64[:6]
        b64 = b64[6:]
        o += convert_tbl[k]
    o = o[:-padding_len] if padding_len else o
    if with_padding:
        o += '=' * padding_len
    return o.encode()

def base64_decode(b64):
    padding_len = b64.count('=')
    binary_str = ''
    for c in b64:
        binary_str += reverse_tbl[c]
    o = ''
    while binary_str:
        byte = binary_str[:8]
        binary_str = binary_str[8:]
        decimal = int(byte, 2)
        o += chr(decimal)
    o = o[:-padding_len] if padding_len else o
    return o.encode()

