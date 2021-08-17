import numpy as np
from util import mod_inv


def get_key(cipher, plain):
    #TODO
    '''
    Calculate public key with cipher text and plain text.

    Arguments:
        cipher: str, cipher text
        plain: str, plain text

    Return:
        key: str, public key
    '''
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.,?!'
    cipher = [letters.index(i) for i in cipher]
    plain = [letters.index(i) for i in plain]
    if len(cipher) % 3 == 2:
        cipher.append(cipher[len(cipher) - 1])
    elif len(cipher) % 3 == 1:
        cipher.append(cipher[len(cipher) - 1])
        cipher.append(cipher[len(cipher) - 1])
    if len(plain) % 3 == 2:
        plain.append(plain[len(plain) - 1])
    elif len(plain) % 3 == 1:
        plain.append(plain[len(plain) - 1])
        plain.append(plain[len(plain) - 1])
    cipher = np.reshape(cipher, (-1, 3)).T
    plain = np.reshape(plain, (-1, 3)).T
    public_key = np.dot(cipher, mod_inv(plain))
    public_key = np.mod(public_key, 31)
    key = ' '.join(str(i) for i in public_key.flatten())
    return key

