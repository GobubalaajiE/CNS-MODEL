def rsa_encrypt(m, e, n):
    return pow(m, e, n)

p = 13
q = 19
n = p * q
e = 11
phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)  # Modular inverse of e

m = 2  # Candidate choice (vote)
encrypted_vote = rsa_encrypt(m, e, n)

print(f"Encrypted Vote: {encrypted_vote}")
