from pwn import *  # pip install pwntools
import json
from base64 import b64decode
from binascii import unhexlify
import codecs

def decode(t, dat):
    if t == 'base64':
        return b64decode(dat).decode('utf-8')
    elif t == 'hex':
        return unhexlify(dat).decode('utf-8')
    elif t == 'bigint':
        return unhexlify(dat.replace('0x', '')).decode('utf-8')
    elif t == 'rot13':
        return codecs.encode(dat, 'rot_13')
    elif t == 'utf-8':
        return "".join(chr(o) for o in dat)


r = remote('socket.cryptohack.org', 13377, level='debug')


def json_recv():
    line = r.recvline()
    return json.loads(line.decode())


def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

while True:
    received = json_recv()

    if "flag" in received:
        print("Flag: ", received['flag'])
        exit()

    to_send = {"decoded": decode(received['type'], received['encoded'])}
    json_send(to_send)

