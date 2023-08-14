import cloudinary
import encryption
from cloudinary.uploader import upload
from pathlib import Path

cloudinary.config(
    cloud_name="darx4fbqo",
    api_key="349765384248479",
    api_secret="vGw7sREkXTDzcApraF0iHfOYc3Q",
)

url = cloudinary.utils.cloudinary_url(
    "CLOUDINARY_URL=cloudinary://349765384248479:vGw7sREkXTDzcApraF0iHfOYc3Q@darx4fbqo"
)

result = cloudinary.api.resources_by_tag("mytag", resource_type="raw")
