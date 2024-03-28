import os
import random

from bitarray._bitarray import bitarray
from bitarray.util import *


def bytestring_to_bitarray(input):
    bits_input_string = bitarray()
    for char in input:
        aa = ''.join(['0'] * (8 - len(bin(char)[2:])))
        bits_input_string += aa + bin(char)[2:]
    return bits_input_string


def function(left, key):
    return left << 9 ^ (~(key >> 11 & left))


def get_round_key(K, i):
    return (K << i * 8)[:32]


def encrypt(plaintext, key, n):
    for i in range(n):
        res = bitarray()
        k_i = get_round_key(key, i)
        for index_of_block in range(len(plaintext) // 64):
            block = plaintext[64 * index_of_block: 64 * (index_of_block + 1)]
            left = block[0:32]
            right = block[32:64]
            if index_of_block == 0:
                temp = function(left, k_i) ^ right
            else:
                temp = right
            if i == n - 1:
                new_block = left + temp
            else:
                new_block = temp + left
            res += new_block
        plaintext = res
    return plaintext


def decrypt(plaintext, key, n):
    for i in range(n):
        res = bitarray()
        k_i = get_round_key(key, n - i - 1)
        for index_of_block in range(len(plaintext) // 64):
            block = plaintext[64 * index_of_block: 64 * (index_of_block + 1)]
            left = block[0:32]
            right = block[32:64]
            if index_of_block == 0:
                temp = function(left, k_i) ^ right
            else:
                temp = right
            if i == n - 1:
                new_block = left + temp
            else:
                new_block = temp + left
            res += new_block
        plaintext = res
    return plaintext


if __name__ == '__main__':
    input_string = b'This is random string'
    input_string = bytes([0] * (8 - len(input_string) % 8)) + input_string
    binput_string = bytestring_to_bitarray(input_string)
    key = bytearray(os.urandom(8))
    bkey = bytestring_to_bitarray(key)
    n = random.randrange(2, 12)

    en_string = encrypt(binput_string, bkey, n)
    print('Исходный текст:', input_string)
    print('Зашифрованный текст:', en_string)
    print('Расшифрованный текст:', ba2int(decrypt(en_string, bkey, n)).to_bytes(21, 'big').decode())
