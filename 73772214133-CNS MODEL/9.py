from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

def aes_encrypt(data, key):
    cipher = AES.new(key, AES.MODE_CBC)
    encrypted = cipher.encrypt(pad(data.encode(), AES.block_size))
    return base64.b64encode(cipher.iv + encrypted).decode('utf-8')

def aes_decrypt(encrypted_data, key):
    encrypted_data = base64.b64decode(encrypted_data)
    iv, encrypted = encrypted_data[:16], encrypted_data[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(encrypted), AES.block_size)
    return decrypted.decode('utf-8')

key = b'Sixteen byte key for AES256'
id_record = input("Enter your National ID: ")
encrypted_id = aes_encrypt(id_record, key)
decrypted_id = aes_decrypt(encrypted_id, key)

print("Encrypted ID:", encrypted_id)
print("Decrypted ID:", decrypted_id)
