def text_to_nums(text):
    return [ord(c.upper()) - 65 for c in text if c.isalpha()]

def nums_to_text(nums):
    return ''.join(chr(n + 65) for n in nums)

def mod_inverse(a, m=26):
    for x in range(m):
        if (a * x) % m == 1:
            return x
    raise ValueError("Key matrix is not invertible.")

def matrix_multiply(matrix, vector):
    return [(matrix[0][0] * vector[0] + matrix[0][1] * vector[1]) % 26,
            (matrix[1][0] * vector[0] + matrix[1][1] * vector[1]) % 26]

def hill_cipher(text, key, mode='encrypt'):
    key_matrix = [key[:2], key[2:]]
    if mode == 'decrypt':
        det = (key_matrix[0][0] * key_matrix[1][1] - key_matrix[0][1] * key_matrix[1][0]) % 26
        inv_det = mod_inverse(det)
        adj = [[key_matrix[1][1], -key_matrix[0][1]], [-key_matrix[1][0], key_matrix[0][0]]]
        key_matrix = [[(inv_det * adj[i][j]) % 26 for j in range(2)] for i in range(2)]
    nums = text_to_nums(text)
    result = []
    for i in range(0, len(nums), 2):
        vec = nums[i:i+2] if i+1 < len(nums) else [nums[i], 0]
        res = matrix_multiply(key_matrix, vec)
        result.extend(res)
    return nums_to_text(result)


while True:
    plaintext = input("Enter plaintext (letters only, e.g., HELP): ").strip()
    if plaintext and all(c.isalpha() for c in plaintext):
        break
    print("Error: Plaintext must contain only letters.")

while True:
    try:
        key_input = input("Enter 4 numbers for 2x2 key matrix (e.g., 3 3 2 5): ").strip()
        key = [int(x) for x in key_input.split()]
        if len(key) != 4:
            raise ValueError("Exactly 4 numbers required.")
        det = (key[0] * key[3] - key[1] * key[2]) % 26
        if det == 0 or mod_inverse(det) is None:
            raise ValueError("Key matrix is not invertible.")
        break
    except ValueError as e:
        print(f"Error: {e}")

ciphertext = hill_cipher(plaintext, key, 'encrypt')
print(f"Ciphertext: {ciphertext}")
decrypted = hill_cipher(ciphertext, key, 'decrypt')
print(f"Decrypted: {decrypted}")