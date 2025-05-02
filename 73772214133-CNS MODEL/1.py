def create_matrix(key):
    key = ''.join(dict.fromkeys(key.upper().replace('J', 'I')))
    matrix = []
    for c in key + ''.join(c for c in 'ABCDEFGHIKLMNOPQRSTUVWXYZ' if c not in key):
        if len(matrix) == 0 or len(matrix[-1]) == 5: matrix.append([])
        matrix[-1].append(c)
    return matrix

def prepare_text(text):
    text = text.upper().replace('J', 'I').replace(' ', '')
    digraphs = []
    i = 0
    while i < len(text):
        a, b = text[i], text[i+1] if i+1 < len(text) else 'X'
        digraphs.append(a + ('X' if a == b else b))
        i += 1 if a == b else 2
    return digraphs

def playfair(text, key, mode='encrypt'):
    matrix, result, shift = create_matrix(key), '', 1 if mode == 'encrypt' else -1
    for a, b in prepare_text(text):
        r1, c1 = next((i, j) for i, row in enumerate(matrix) for j, c in enumerate(row) if c == a)
        r2, c2 = next((i, j) for i, row in enumerate(matrix) for j, c in enumerate(row) if c == b)
        if r1 == r2: result += matrix[r1][(c1 + shift) % 5] + matrix[r2][(c2 + shift) % 5]
        elif c1 == c2: result += matrix[(r1 + shift) % 5][c1] + matrix[(r2 + shift) % 5][c2]
        else: result += matrix[r1][c2] + matrix[r2][c1]
    return result

key = input("Enter key (e.g., SECURITY): ")
msg = input("Enter message (e.g., ATTACK TONIGHT): ")
cipher = playfair(msg, key, 'encrypt')
print(f"Ciphertext: {cipher}")
print(f"Decrypted: {playfair(cipher, key, 'decrypt')}")