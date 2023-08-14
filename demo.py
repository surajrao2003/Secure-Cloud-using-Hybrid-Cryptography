import cloudinary
import encryption
from cloudinary.uploader import upload
from pathlib import Path

cloudinary.config(
  cloud_name = "darx4fbqo",
  api_key = "349765384248479",
  api_secret = "vGw7sREkXTDzcApraF0iHfOYc3Q"
)

file_path = Path("C:/Users/Manoj Reddy/Desktop/btp/u1.txt")
public_id = file_path.stem
response = upload(str(file_path), public_id=public_id,resource_type='raw')

print(response)
