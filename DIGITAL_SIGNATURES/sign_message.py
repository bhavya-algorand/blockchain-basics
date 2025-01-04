from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

# Load private key
with open("private.pem", "rb") as f:
    private_key = RSA.import_key(f.read())

# Message to be signed
message = b"Blockchain transactions are secure."

# Hash the message
message_hash = SHA256.new(message)

print("Message Hash:\n", message_hash.hexdigest())

# Sign the message
signature = pkcs1_15.new(private_key).sign(message_hash)

# Save the signature
with open("signature.bin", "wb") as f:
    f.write(signature)

print("Digital Signature:\n", signature.hex())
