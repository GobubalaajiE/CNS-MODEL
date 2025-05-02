def vigenere_encrypt(plaintext, keyword):
    ciphertext = []
    keyword_repeated = (keyword * (len(plaintext) // len(keyword))) + keyword[:len(plaintext) % len(keyword)]
    
    for p, k in zip(plaintext.upper(), keyword_repeated.upper()):
        if p.isalpha():
            shift = ord(k) - 65
            encrypted_char = chr((ord(p) - 65 + shift) % 26 + 65)
            ciphertext.append(encrypted_char)
        else:
            ciphertext.append(p)
    return ''.join(ciphertext)

def vigenere_decrypt(ciphertext, keyword):
    plaintext = []
    keyword_repeated = (keyword * (len(ciphertext) // len(keyword))) + keyword[:len(ciphertext) % len(keyword)]
    
    for c, k in zip(ciphertext.upper(), keyword_repeated.upper()):
        if c.isalpha():
            shift = ord(k) - 65
            decrypted_char = chr((ord(c) - 65 - shift) % 26 + 65)
            plaintext.append(decrypted_char)
        else:
            plaintext.append(c)
    return ''.join(plaintext)

message = input("Enter the message: ")
keyword = input("Enter the keyword: ")

encrypted_message = vigenere_encrypt(message, keyword)
decrypted_message = vigenere_decrypt(encrypted_message, keyword)

print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)
