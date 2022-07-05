from Crypto.Cipher import AES 

# pycryptodome
# 16 bytes 
# the key is h0wd1dTh15hApp3n
# the iv  is iW4nTt0GoHom3n0W

ciphertext = bytes.fromhex("5b868c7920e83d924dca9c639cfbfabe026675f127f2aa958d63272e64fd8170")
decryption = AES.new(key=b"h0wd1dTh15hApp3n",mode=AES.MODE_CBC,iv=b"iW4nTt0GoHom3n0W")
plaintext = decryption.decrypt(ciphertext).decode()

print(plaintext)