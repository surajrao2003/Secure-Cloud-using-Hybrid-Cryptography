import time
from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()

# Encrypt a file and measure time taken
def encrypt_file(infile, outfile, key):
    f = Fernet(key)
    with open(infile, "rb") as fin:
        data = fin.read()
    start_time = time.time()
    encrypted_data = f.encrypt(data)
    end_time = time.time()
    with open(outfile, "wb") as fout:
        fout.write(encrypted_data)
    return end_time - start_time

# Decrypt a file and measure time taken
def decrypt_file(infile, outfile, key):
    f = Fernet(key)
    with open(infile, "rb") as fin:
        encrypted_data = fin.read()
    start_time = time.time()
    decrypted_data = f.decrypt(encrypted_data)
    end_time = time.time()
    with open(outfile, "wb") as fout:
        fout.write(decrypted_data)
    return end_time - start_time

# Encrypt and decrypt a file and measure time taken
encryption_time = encrypt_file("btpsem6.txt", "encrypted.bin", key)
print(f"Encryption time: {encryption_time} seconds")
decryption_time = decrypt_file("encrypted.bin", "decrypted.txt", key)
print(f"Decryption time: {decryption_time} seconds")
