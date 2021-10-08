#!/usr/bin/env python3

from Crypto.Util import number
from Crypto.Cipher import AES
import os, sys, random


def keygen():
    iv, key = [os.urandom(16) for _ in '01']
    return iv, key


def encrypt(msg, iv, key):
    aes = AES.new(key, AES.MODE_CBC, iv)
    return aes.encrypt(msg)


def decrypt(enc, iv, key):
    aes = AES.new(key, AES.MODE_CBC, iv)
    return aes.decrypt(enc)


def die(*args):
    pr(*args)
    quit()


def main():
    iv, key = keygen()
    # flag_enc = encrypt(flag, iv, key).hex()

    while True:
        print("| Options: \n|\t[G]et the encrypted flag \n|\t[T]est the encryption \n|\t[Q]uit")
        ans = input().lower()
        # pr("| encrypt(flag) =", flag_enc)
        if ans == 't':
            print("| Please send your 32 bytes message to encrypt: ")
            msg_inp = input()
            if len(msg_inp) == 32:
                enc = encrypt(msg_inp, iv, key).hex()
                r = random.randint(0, 4)
                s = 4 - r
                mask_key = key[:-2].hex() + '*' * 4
                mask_enc = enc[:r] + '*' * 28 + enc[32 - s:]
                print("| enc =", mask_enc)
                print("| key =", mask_key)
            else:
                die("| SEND 32 BYTES MESSAGE :X")
        elif ans == 'q':
            die("Quitting ...")
        else:
            die("Bye ...")


if __name__ == '__main__':
    main()
