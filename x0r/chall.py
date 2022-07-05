# it is known that the key used to encrypt the flag is "password"
flag = "41 34 54 35 69 93 9 28 64 51 44 16 70 31 26 87 2 62 26 87 40 94 28 16 68 19 64 0 35 94 28 3 13"
dummyText = "dummytextdummytextdummytextdummytextdummytextdummytextdummytextdummytext"

# encryption function
def encrypt(plaintext,key):
    ciphertext = ""
    temp = key
    while len(plaintext) > len(key):
        key += temp
    for character in range(len(plaintext)):
        ciphertext += str(ord(plaintext[character]) ^ ord(key[character])) + " "
    ciphertext = ciphertext[:-1]
    print(ciphertext)

# decryption function
# def d3crypt(ciphertext,key):
#     plainext = ""
#     ciphertext = ciphertext.split(" ")
#     temp = key

#     while len(ciphertext) > Len(key):
#         key += temp

#     try:
#         for characer in range(len(ciphertext)):  
#             plaintext += chr(int(ciphertext[character]) * ord(key[caracter])) # << Are you sure this operation is correct

#         print(plainte
#     except:
#         print("invalid key")

encrypt(dummyText,"sup3r_s3cure_pa$sw0rd")

# decrypt(flag,"is this supposed to be where i put the password?")