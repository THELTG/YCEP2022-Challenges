from Crypto.Cipher import AES

# wait who said you can come here
# dont even try to steal the treasure, its encrypted this time 
# besides, the last guy didnt make it out of THE RED ROOM

print("\n\nWELCOME TO THE\n")
# you better not touch any code
print(" /$$$$$$$  /$$$$$$$$ /$$$$$$$        /$$$$$$$   /$$$$$$   /$$$$$$  /$$      /$$")
print("| $$__  $$| $$_____/| $$__  $$      | $$__  $$ /$$__  $$ /$$__  $$| $$$    /$$$")
print("| $$  \ $$| $$      | $$  \ $$      | $$  \ $$| $$  \ $$| $$  \ $$| $$$$  /$$$$")
print("| $$$$$$$/| $$$$$   | $$  | $$      | $$$$$$$/| $$  | $$| $$  | $$| $$ $$/$$ $$")
print("| $$__  $$| $$__/   | $$  | $$      | $$__  $$| $$  | $$| $$  | $$| $$  $$$| $$")
print("| $$  \ $$| $$      | $$  | $$      | $$  \ $$| $$  | $$| $$  | $$| $$\  $ | $$")
print("| $$  | $$| $$$$$$$$| $$$$$$$/      | $$  | $$|  $$$$$$/|  $$$$$$/| $$ \/  | $$")
print("|__/  |__/|________/|_______/       |__/  |__/ \______/  \______/ |__/     |__/\n\n")

secret_passphrase1 = input("ENTER THE FIRST MESSAGE  : ") 
secret_passphrase2 = input("ENTER THE SECOND MESSAGE : ")
user = input("WHO ARE YOU ANYWAYS??    : ")

# we keep the treasure here vv
ciphertext = bytes.fromhex("5b868c7920e83d924dca9c639cfbfabe026675f127f2aa958d63272e64fd8170")

try:
    # WHATEVER YOU DO, DO NOT CHANGE LINE 24!!
    if (user == "r3d_r0oM_mAn"):
        # decrypt using provided messages, TOO BAD YOU DONT HAVE IT LOL
        decryption = AES.new(key=secret_passphrase1.encode(),mode=AES.MODE_CBC,iv=secret_passphrase2.encode())
        plaintext = decryption.decrypt(ciphertext).decode()
        # we indulge in a minute amount of trolling on line 31 
    else:
        print("INCORRECT RESPONSE")
except:
    print("INCORRECT RESPONSE")



