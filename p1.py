import numpy as np
from util import mod_inv


def decode(cipher, key):
    #TODO
    '''
    Decode cipher with public key.

    Arguments:
        cipher: str, cipher text
        key: str, public key

    Return:
        plain: str, plain text
    '''
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.,?!'
    key = [int(k) for k in key.split()]
    public_key = np.reshape(key, (3, 3))
    private_key = mod_inv(public_key)
    cipher = [letters.index(i) for i in cipher]
    if len(cipher) % 3 == 2:
        cipher.append(cipher[len(cipher) - 1])
    elif len(cipher) % 3 == 1:
        cipher.append(cipher[len(cipher) - 1])
        cipher.append(cipher[len(cipher) - 1])
    cipher = np.reshape(cipher, (-1, 3)).T
    plain_num = np.dot(private_key, cipher)
    plain_num = np.mod(plain_num, 31)
    plain = []
    for p in plain_num.T.flatten():
        plain.append(letters[p])
    return ''.join(plain)

