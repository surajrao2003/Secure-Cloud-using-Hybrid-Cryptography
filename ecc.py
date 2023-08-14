from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

# Generate elliptic curve parameters
curve = ec.SECP256R1()
backend = default_backend()

# User 1 generates a private key and public key
private_key_1 = ec.generate_private_key(curve, backend)
public_key_1 = private_key_1.public_key()

# User 2 generates a private key and public key
private_key_2 = ec.generate_private_key(curve, backend)
public_key_2 = private_key_2.public_key()

# User 1 encrypts a message using User 2's public key
message = b"the key for encryption is CvmWpLYqG_3dCc8YrVWHV2M4-nG3lTsUjCsFtJt7j6M="
ephemeral_private_key = ec.generate_private_key(curve, backend)
ephemeral_public_key = ephemeral_private_key.public_key()

shared_key = private_key_2.exchange(ec.ECDH(), ephemeral_public_key)
hkdf = HKDF(
    algorithm=hashes.SHA256(),
    length=32,
    salt=None,
    info=b'handshake data',
    backend=backend
)
key = hkdf.derive(shared_key)
# Unique value for each encryption
import os
nonce = os.urandom(16)
cipher = Cipher(algorithms.AES(key), modes.CTR(nonce), backend=backend)
encryptor = cipher.encryptor()
ciphertext = encryptor.update(message) + encryptor.finalize()

encrypted = ephemeral_public_key.public_bytes(
    encoding=serialization.Encoding.DER,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
) + ciphertext

# User 2 decrypts the message using their private key
ephemeral_public_key_bytes, ciphertext = encrypted[:91], encrypted[91:]
ephemeral_public_key = serialization.load_der_public_key(
    ephemeral_public_key_bytes,
    backend=default_backend()
)

shared_key = private_key_2.exchange(ec.ECDH(), ephemeral_public_key)
hkdf = HKDF(
    algorithm=hashes.SHA256(),
    length=32,
    salt=None,
    info=b'handshake data',
    backend=backend
)
key = hkdf.derive(shared_key)

cipher = Cipher(algorithms.AES(key), modes.CTR(nonce), backend=backend)
decryptor = cipher.decryptor()
decrypted = decryptor.update(ciphertext) + decryptor.finalize()

print("Original message:", message)
print("\n\nEncrypted message which is sent to user b is :", encrypted)
print("\n\nDecrypted message:", decrypted)
