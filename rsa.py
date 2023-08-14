from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# User 1 generates an RSA key pair
private_key_1 = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key_1 = private_key_1.public_key()

# User 2 generates an RSA key pair
private_key_2 = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key_2 = private_key_2.public_key()

# User 1 encrypts a message using User 2's public key
message = b"CvmWpLYqG_3dCc8YrVWHV2M4-nG3lTsUjCsFtJt7j6M="
encrypted = public_key_2.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# User 2 decrypts the message using their private key
decrypted = private_key_2.decrypt(
    encrypted,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("\nOriginal message:", message)
print("\nEncrypted message:", encrypted)
print("\n\nDecrypted message:", decrypted,"\n\n")
