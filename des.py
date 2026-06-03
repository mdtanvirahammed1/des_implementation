from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad


key = input("Enter 8 character key: ").encode()


plaintext = input("Enter text: ")


cipher = DES.new(key, DES.MODE_ECB)


ciphertext = cipher.encrypt(pad(plaintext.encode(), DES.block_size))

print("\nOriginal Text :", plaintext)
print("Encrypted Hex :", ciphertext.hex())

decipher = DES.new(key, DES.MODE_ECB)
decrypted_text = unpad(decipher.decrypt(ciphertext), DES.block_size)

print("Decrypted Text:", decrypted_text.decode())