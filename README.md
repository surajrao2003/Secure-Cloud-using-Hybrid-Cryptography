# Secure Cloud Using Hybrid Cryptography

A user-friendly web application for secure file storage and retrieval using a hybrid cryptography model (AES + RSA). Protect your data with strong encryption before uploading to the cloud. AES ensures fast, secure file encryption, while RSA secures the AES keys for safe sharing and storage.

---

## Design & Implementation Plan

![Design Timeline](https://raw.githubusercontent.com/surajrao2003/Secure-Cloud-using-Hybrid-Cryptography/main/images/design_timeline.png)

*Figure: High-level design and implementation timeline for the hybrid cryptography cloud storage system.*

---

## Features
- **Hybrid Encryption**: Combines AES (for file encryption) and RSA (for securing AES keys).
- **Cloud Upload**: Encrypted files are uploaded to Cloudinary (or other cloud providers).
- **Web Interface**: Simple Flask web app for file selection, encryption, decryption, and upload.
- **Key Management**: AES keys are encrypted with RSA and provided to the user.
- **Security Best Practices**: No sensitive credentials in code; uses environment variables.

---

## Flowchart of the Hybrid Cryptographic Model

![Hybrid Cryptography Flowchart](https://raw.githubusercontent.com/surajrao2003/Secure-Cloud-using-Hybrid-Cryptography/main/images/hybrid_crypto_flowchart.png)

*Figure: Flowchart illustrating the design and implementation of the hybrid cryptography model using RSA and AES for secure file encryption and decryption.*

---

## How It Works
1. **Login**: User logs in using credentials.
2. **User Selects and Uploads File**
3. **Encryption Using AES/RSA**: File is encrypted using AES; AES key is encrypted with RSA.
4. **Assign Public Key**: Public key is assigned for encryption.
5. **Recombine and Download Files**: Encrypted file and key are recombined for download.
6. **User Authentication**: User authenticates to access and decrypt files.

---

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/surajrao2003/Secure-Cloud-using-Hybrid-Cryptography.git
   cd Secure-Cloud-using-Hybrid-Cryptography
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Cloudinary**
   - Set your Cloudinary credentials as environment variables:
     - `CLOUDINARY_CLOUD_NAME`
     - `CLOUDINARY_API_KEY`
     - `CLOUDINARY_API_SECRET`

   Example (Linux/macOS):
   ```bash
   export CLOUDINARY_CLOUD_NAME=your_cloud_name
   export CLOUDINARY_API_KEY=your_api_key
   export CLOUDINARY_API_SECRET=your_api_secret
   ```
   Example (Windows):
   ```powershell
   set CLOUDINARY_CLOUD_NAME=your_cloud_name
   set CLOUDINARY_API_KEY=your_api_key
   set CLOUDINARY_API_SECRET=your_api_secret
   ```

4. **Run the Application**
   ```bash
   python app.py
   # or
   python encrypt.py
   # or
   python decrypt.py
   ```

---

## Usage
- Use the web interface to select files for encryption or decryption.
- Download the encrypted/decrypted files and keep your private key safe.

---

## Security Notes
- **Never share your private RSA key.**
- AES keys are generated per file and never stored in plaintext.
- Cloudinary credentials must not be hardcoded; use environment variables.
- For production, use HTTPS and secure key storage.

---

## Project Structure
- `app.py`           - Main Flask app for uploads
- `encrypt.py`       - Flask app for encryption and upload
- `decrypt.py`       - Flask app for decryption
- `encryption.py`    - AES encryption/decryption utilities
- `rsa.py`           - RSA key generation and usage example
- `requirements.txt` - Python dependencies
- `README.md`        - Project documentation

---

## Documentation
- [Project Report](https://drive.google.com/file/d/1_TcTL2ojjeXs7WE53lcLIuncvuVWw6x3/view?usp=sharing)
- [Project Presentation](https://docs.google.com/presentation/d/1eQvdTLpK-OuQh_ZA8J9xKFe1jcbIl8li/edit?usp=sharing)

---

