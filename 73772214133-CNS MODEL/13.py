from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import base64

def des_encrypt(data, key):
    cipher = DES.new(key, DES.MODE_CBC)
    encrypted = cipher.encrypt(pad(data.encode(), DES.block_size))
    return base64.b64encode(cipher.iv + encrypted).decode('utf-8')

def des_decrypt(encrypted_data, key):
    encrypted_data = base64.b64decode(encrypted_data)
    iv, encrypted = encrypted_data[:8], encrypted_data[8:]
    cipher = DES.new(key, DES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(encrypted), DES.block_size)
    return decrypted.decode('utf-8')

key = b'8bytekey'
employee_data = input("Enter employee data: ")
encrypted_data = des_encrypt(employee_data, key)
decrypted_data = des_decrypt(encrypted_data, key)

print("Encrypted Employee Data:", encrypted_data)
print("Decrypted Employee Data:", decrypted_data)
