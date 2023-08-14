from cryptography.fernet import Fernet
import eel
import io

@eel.expose
def keyGen():
    key = Fernet.generate_key()
    file = open('Keys/key.key', 'wb')
    file.write(key)
    file.close()
    print("\nKey Created.\n")

def keyRead():
    try:
        file = open('Keys/key.key', 'rb')
        key = file.read()
        file.close()
        return key
    except FileNotFoundError:
        print("No Key exists, a new one has just been created.")
        keyGen()
        keyRead()

@eel.expose
def encrypt(fileName):
    Key = keyRead()
    with open("Files/"+ fileName, "rb") as f:
        data = f.read()
    fernet = Fernet(Key)
    encrypted = fernet.encrypt(data)
    with open("encrypt/"+ fileName, "wb") as f:
        f.write(encrypted)

@eel.expose
def decrypt(fileName):
    Key = keyRead()
    with open("encrypt/"+ fileName, "rb") as f:
        data = f.read()
    fernet = Fernet(Key)
    decrypted = fernet.decrypt(data)
    with open("Downloads/"+ fileName, "wb") as f:
        f.write(decrypted)
encrypt('u1.txt')
print("encrypted succesful")
import cloudinary
from cloudinary.uploader import upload
from pathlib import Path

cloudinary.config(
  cloud_name = "darx4fbqo",
  api_key = "349765384248479",
  api_secret = "vGw7sREkXTDzcApraF0iHfOYc3Q"
)


file_path = Path("C:/Users/Manoj Reddy/Desktop/btp/encrypt/u1.txt")
public_id = file_path.stem
response = upload(str(file_path), public_id=public_id,resource_type='raw')

print(response)