import os

def encrypt(filename, crypto, blocksize=16):

    with open(filename, 'r+b') as f:
        try:
            plaintext = f.read()
            ciphertext = crypto(plaintext)
            # while plaintext:
            #     ciphertext = crypto(plaintext)
            #     if len(plaintext) != len(ciphertext):
            #         raise ValueError('''Ciphertext({})is not of the same length of the Plaintext({}).
            #         Not a stream cipher.'''.format(len(ciphertext), len(plaintext)))
            #
            f.seek(-len(plaintext), 1) # return to same point before the read
            f.write(ciphertext)
        except:
            pass
        # plaintext = f.read(blocksize)
