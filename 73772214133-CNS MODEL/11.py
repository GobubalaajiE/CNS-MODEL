from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import base64

def des_encrypt(password, key):
    cipher = DES.new(key, DES.MODE_CBC)
    encrypted = cipher.encrypt(pad(password.encode(), DES.block_size))
    return base64.b64encode(cipher.iv + encrypted).decode('utf-8')

def des_decrypt(encrypted_password, key):
    encrypted_password = base64.b64decode(encrypted_password)
    iv, encrypted = encrypted_password[:8], encrypted_password[8:]
    cipher = DES.new(key, DES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(encrypted), DES.block_size)
    return decrypted.decode('utf-8')

key = b'8bytekey'  # DES requires 8-byte key
password = input("Enter password: ")
encrypted_password = des_encrypt(password, key)
decrypted_password = des_decrypt(encrypted_password, key)

print("Encrypted Password:", encrypted_password)
print("Decrypted Password:", decrypted_password)
