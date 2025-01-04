import hashlib
# pip install hashlib
input_data = input("Enter a string to hash: ")
input_bytes = input_data.encode('utf-8')
sha256_hash = hashlib.sha256(input_bytes)
print(f"SHA256 Hash: {sha256_hash.hexdigest()}")
