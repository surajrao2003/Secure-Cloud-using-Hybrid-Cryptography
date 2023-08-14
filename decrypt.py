from cryptography.fernet import Fernet
from flask import Flask, render_template, request, send_file

# The Fernet key used to encrypt and decrypt the file
KEY = b'CvmWpLYqG_3dCc8YrVWHV2M4-nG3lTsUjCsFtJt7j6M='

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/decrypt', methods=['POST'])
def decrypt():
    filename = request.form['filename']
    # Read the encrypted data from the file
    with open(f'encrypt/{filename}', 'rb') as f:
        encrypted_data = f.read()

    # Decrypt the data using the Fernet key
    fernet = Fernet(KEY)
    decrypted_data = fernet.decrypt(encrypted_data)

    # Write the decrypted data to a new file in the Downloads directory
    with open(f'Downloads/{filename}', 'wb') as f:
        f.write(decrypted_data)

    # Send the decrypted file to the user
    return send_file(f'Downloads/{filename}', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
