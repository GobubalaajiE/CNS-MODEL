def left_rotate(n, b):
    return ((n << b) | (n >> (32 - b))) & 0xffffffff

def sha1(message):
    h0, h1, h2, h3, h4 = 0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0
    msg = bytearray(message.encode())
    ml = len(msg) * 8
    msg.append(0x80)
    while (len(msg) * 8) % 512 != 448:
        msg.append(0)
    msg += ml.to_bytes(8, 'big')
    
    for i in range(0, len(msg), 64):
        w = [0] * 80
        for j in range(16):
            w[j] = int.from_bytes(msg[i + j*4:i + j*4 + 4], 'big')
        for j in range(16, 80):
            w[j] = left_rotate(w[j-3] ^ w[j-8] ^ w[j-14] ^ w[j-16], 1)
        
        a, b, c, d, e = h0, h1, h2, h3, h4
        for j in range(80):
            if 0 <= j <= 19:
                f = (b & c) | (~b & d)
                k = 0x5A827999
            elif 20 <= j <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= j <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            else:
                f = b ^ c ^ d
                k = 0xCA62C1D6
            temp = (left_rotate(a, 5) + f + e + k + w[j]) & 0xffffffff
            e, d, c, b, a = d, c, left_rotate(b, 30), a, temp
        
        h0 = (h0 + a) & 0xffffffff
        h1 = (h1 + b) & 0xffffffff
        h2 = (h2 + c) & 0xffffffff
        h3 = (h3 + d) & 0xffffffff
        h4 = (h4 + e) & 0xffffffff
    
    return f"{h0:08x}{h1:08x}{h2:08x}{h3:08x}{h4:08x}"

def mod_exp(base, exp, mod):
    result = 1
    base %= mod
    while exp > 0:
        if exp & 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp >>= 1
    return result

def sign_document(doc, d, n):
    hash_val = int(sha1(doc), 16) % n
    return mod_exp(hash_val, d, n)

def verify_document(doc, signature, e, n):
    hash_val = int(sha1(doc), 16) % n
    decrypted_hash = mod_exp(signature, e, n)
    return hash_val == decrypted_hash

# User input
doc = input("Enter consent form content (e.g., I agree to participate): ").strip()
d = int(input("Enter private key d (e.g., 7): "))
e = int(input("Enter public key e (e.g., 3): "))
n = int(input("Enter modulus n (e.g., 33): "))

# Sign and verify
signature = sign_document(doc, d, n)
print(f"Signature: {signature}")
is_valid = verify_document(doc, signature, e, n)
print(f"Signature valid: {is_valid}")