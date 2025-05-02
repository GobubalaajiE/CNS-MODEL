ciphertext = input("Enter the ciphertext: ")
def caesar_cipher_decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            plaintext += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            plaintext += char
    return plaintext

for shift in range(26):
    decrypted_message = caesar_cipher_decrypt(ciphertext, shift)
    print(f"Shift {shift}: {decrypted_message}")

