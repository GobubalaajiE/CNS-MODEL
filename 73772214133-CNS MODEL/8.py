from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

def aes_encrypt(pin, key):
    cipher = AES.new(key, AES.MODE_CBC)
    encrypted = cipher.encrypt(pad(pin.encode(), AES.block_size))
    return base64.b64encode(cipher.iv + encrypted).decode('utf-8')

def aes_decrypt(encrypted_pin, key):
    encrypted_pin = base64.b64decode(encrypted_pin)
    iv, encrypted = encrypted_pin[:16], encrypted_pin[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(encrypted), AES.block_size)
    return decrypted.decode('utf-8')

key = b'Sixteen byte key'  # Must be 16 bytes for AES-128
pin = input("Enter your PIN: ")
encrypted_pin = aes_encrypt(pin, key)
decrypted_pin = aes_decrypt(encrypted_pin, key)

print("Encrypted PIN:", encrypted_pin)
print("Decrypted PIN:", decrypted_pin)
