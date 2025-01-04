import hashlib
# pip install hashlib

# Example input string
input_data = "1105800dc"

# Convert input data to bytes
input_bytes = input_data.encode('utf-8')

# Hash the data using SHA256
sha256_hash = hashlib.sha256(input_bytes)

# Get the hexadecimal representation of the hash
hex_hash = sha256_hash.hexdigest()

print("Input Data: ", input_data)
print("SHA256 Hash: ", hex_hash)
