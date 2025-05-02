def rail_fence_encrypt(message, rails):
    fence = [['' for _ in range(len(message))] for _ in range(rails)]
    direction = 1
    row, col = 0, 0

    for char in message:
        fence[row][col] = char
        col += 1
        row += direction

        if row == 0 or row == rails - 1:
            direction = -direction

    return ''.join(''.join(row) for row in fence)

def rail_fence_decrypt(ciphertext, rails):
    fence = [['' for _ in range(len(ciphertext))] for _ in range(rails)]
    direction = 1
    row, col = 0, 0

    for i in range(len(ciphertext)):
        fence[row][col] = '*'
        col += 1
        row += direction
        if row == 0 or row == rails - 1:
            direction = -direction

    idx = 0
    for i in range(rails):
        for j in range(len(ciphertext)):
            if fence[i][j] == '*':
                fence[i][j] = ciphertext[idx]
                idx += 1

    result = []
    row, col = 0, 0
    for i in range(len(ciphertext)):
        result.append(fence[row][col])
        col += 1
        row += direction
        if row == 0 or row == rails - 1:
            direction = -direction
    return ''.join(result)

message = input("Enter the message: ")
rails = int(input("Enter the number of rails: "))

encrypted = rail_fence_encrypt(message, rails)
decrypted = rail_fence_decrypt(encrypted, rails)

print("Encrypted Message:", encrypted)
print("Decrypted Message:", decrypted)
