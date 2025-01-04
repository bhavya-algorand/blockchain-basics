from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
# Load public key
with open("public.pem", "rb") as f:
    public_key = RSA.import_key(f.read())

# Verify the signature
try:
    # Load the message
    message = b"Blockchain transactions are secure."
    message_hash = SHA256.new(message)

    # Load the signature
    with open("signature.bin", "rb") as f:
        signature = f.read()
    
    pkcs1_15.new(public_key).verify(message_hash, signature)
    print("Signature is valid!")
except (ValueError, TypeError):
    print("Signature is invalid!")
