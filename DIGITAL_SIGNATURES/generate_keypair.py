from Crypto.PublicKey import RSA
# pip install pycryptodome

# Generate RSA key pair
key = RSA.generate(2048)

# Export private key
private_key = key.export_key()
with open("private.pem", "wb") as f:
    f.write(private_key)

# Export public key
public_key = key.publickey().export_key()
with open("public.pem", "wb") as f:
    f.write(public_key)

print("Keys generated and saved as 'private.pem' and 'public.pem'")
