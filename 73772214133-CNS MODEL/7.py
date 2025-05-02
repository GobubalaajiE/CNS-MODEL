def rsa_encrypt(m, e, n):
    return pow(m, e, n)

def rsa_decrypt(c, d, n):
    return pow(c, d, n)

p = 19
q = 41
n = p * q
e = 7
phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)  # Modular inverse of e

m = 9
cipher = rsa_encrypt(m, e, n)
plain = rsa_decrypt(cipher, d, n)

print(f"Encrypted: {cipher}")
print(f"Decrypted: {plain}")
