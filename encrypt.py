from flask import Flask, render_template, request
import cloudinary
import cloudinary.uploader
from cryptography.fernet import Fernet
import io
app = Flask(__name__)

def keyRead():
    return b'CvmWpLYqG_3dCc8YrVWHV2M4-nG3lTsUjCsFtJt7j6M='


def encrypt(file):
    Key = keyRead()
    data = file.read()
    fernet = Fernet(Key)
    encrypted = fernet.encrypt(data)
    return encrypted

cloudinary.config(
  cloud_name = "darx4fbqo",
  api_key = "349765384248479",
  api_secret = "vGw7sREkXTDzcApraF0iHfOYc3Q"
)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        
        encrypted_data = encrypt(file)
        if file.filename.endswith('.txt'):
            response = cloudinary.uploader.upload(
                io.BytesIO(encrypted_data),public_id=file.filename,
                resource_type='raw'
            )
            return 'File uploaded to Cloudinary: ' + response['secure_url']
        else:
            return 'Please select a text file'
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
