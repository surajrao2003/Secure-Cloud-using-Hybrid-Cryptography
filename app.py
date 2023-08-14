import cloudinary.uploader
from flask import Flask, render_template, request

app = Flask(__name__)

cloudinary.config(
    cloud_name="darx4fbqo",
    api_key="349765384248479",
    api_secret="vGw7sREkXTDzcApraF0iHfOYc3Q",
)


@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files["file"]

        if file.filename.endswith(".txt"):
            response = cloudinary.uploader.upload(file, resource_type="raw")
            return "File uploaded to Cloudinary: " + response["secure_url"]
        else:
            return "Please select a text file"
    return render_template("upload.html")


if __name__ == "__main__":
    app.run(debug=True)
