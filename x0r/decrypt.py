# it is known that the key used was "password"
flag = "41 34 54 35 69 93 9 28 64 51 44 16 70 31 26 87 2 62 26 87 40 94 28 16 68 19 64 0 35 94 28 3 13"
plaintext = "dummytextdummytextdummytextdummytextdummytextdummytextdummytextdummytext"
key = "password"

# encryption function
def encrypt(plaintext,key):
    ciphertext = ""
    while len(plaintext) > len(key):
        key += "password"

    for character in range(len(plaintext)):
        ciphertext += str(ord(plaintext[character]) ^ ord(key[character])) + " "
    ciphertext = ciphertext[:-1]
    return ciphertext

# decryption function
def decrypt(ciphertext,key):
    plaintext = ""
    ciphertext = ciphertext.split(" ")

    while len(ciphertext) > len(key):
        key += "password"

    for character in range(len(ciphertext)):
        plaintext += chr(int(ciphertext[character]) ^ ord(key[character]))

    print(plaintext)

decrypt(flag,"password")