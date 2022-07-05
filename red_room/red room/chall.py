from Crypto.Cipher import AES 

ciphertext = bytes.fromhex("5b868c7920e83d924dca9c639cfbfabe026675f127f2aa958d63272e64fd8170")
decryption = AES.new(key=b"",mode=AES.MODE_CBC,iv=b"")
plaintext = decryption.decrypt(ciphertext).decode()

print(plaintext)