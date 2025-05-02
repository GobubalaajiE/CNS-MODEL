import hashlib
password = input("Enter your password: ")
sha1_hash = hashlib.sha1(password.encode()).hexdigest()
print(f"The resulting SHA-1 message digest for the password is: {sha1_hash}")
