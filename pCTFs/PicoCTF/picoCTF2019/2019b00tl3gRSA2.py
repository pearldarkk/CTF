from pwn import *
from Crypto.Util.number import *
import owiener

def attack():
    p = remote('2019shell1.picoctf.com', 5027)

    p.readuntil(': ')
    c = int(p.readuntil('\n'))

    p.readuntil(': ')
    n = int(p.readuntil('\n'))

    p.readuntil(': ')
    e = int(p.readuntil('\n'))

    log.info('c = {}'.format(c))
    log.info('n = {}'.format(n))
    log.info('e = {}'.format(e))

    d = owiener.attack(e, n)

    if d is None:
        log.info("Failed")
    else:
        log.info("Hacked d = {}".format(d))

    m = pow(c, d, n)
    log.info('Decrypted m = {}'.format(m))
    log.info('Flag is {}'.format(long_to_bytes(m)))

if __name__ == '__main__':
    attack()
