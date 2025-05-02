def create_playfair_matrix(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key = ''.join(sorted(set(key), key=lambda x: key.index(x)))  
    matrix = []
    
    for char in key:
        if char not in matrix and char in alphabet:
            matrix.append(char)
    
    for char in alphabet:
        if char not in matrix:
            matrix.append(char)

    matrix = [matrix[i:i+5] for i in range(0, len(matrix), 5)]  
    return matrix

def prepare_message(message):
    message = message.replace("J", "I").replace(" ", "").upper()
    if len(message) % 2 != 0:
        message += "X"
    
    prepared_message = []
    for i in range(0, len(message), 2):
        if message[i] == message[i + 1]:
            prepared_message.append(message[i] + "X")
        else:
            prepared_message.append(message[i] + message[i + 1])
    
    return prepared_message

def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col

def encrypt_message(message, matrix):
    encrypted_message = []
    for digraph in message:
        row1, col1 = find_position(matrix, digraph[0])
        row2, col2 = find_position(matrix, digraph[1])

        if row1 == row2:
            encrypted_message.append(matrix[row1][(col1 + 1) % 5])
            encrypted_message.append(matrix[row2][(col2 + 1) % 5])
        elif col1 == col2:
            encrypted_message.append(matrix[(row1 + 1) % 5][col1])
            encrypted_message.append(matrix[(row2 + 1) % 5][col2])
        else:
            encrypted_message.append(matrix[row1][col2])
            encrypted_message.append(matrix[row2][col1])

    return ''.join(encrypted_message)

key = input("Enter key (e.g., SECURITY): ").upper()
message = input("Enter message (e.g., Financial report): ")

matrix = create_playfair_matrix(key
