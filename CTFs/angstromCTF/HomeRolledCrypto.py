import binascii


class Cipher:
    BLOCK_SIZE = 16
    ROUNDS = 3

    def __init__(self, key):
        assert (len(key) == self.BLOCK_SIZE * self.ROUNDS)
        self.key = key

    def __block_encrypt(self, block):
        enc = int.from_bytes(block, "big")
        for i in range(self.ROUNDS):
            k = int.from_bytes(
                self.key[i * self.BLOCK_SIZE:(i + 1) * self.BLOCK_SIZE], "big")
            enc &= k
            enc ^= k
        return hex(enc)[2:].rjust(self.BLOCK_SIZE * 2, "0")

    def encrypt(self, msg):
        e = ""
        for i in range(0, len(m), self.BLOCK_SIZE):
            e += self.__block_encrypt(m[i:i + self.BLOCK_SIZE])
        return e.encode()