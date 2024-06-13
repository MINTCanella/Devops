from flask import Flask, render_template, send_file
import os
import random

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get_image", methods=["GET"])
def get_image():
    image_path = os.path.join(app.root_path, "templates/memes")
    image_files = [
        f for f in os.listdir(image_path) if os.path.isfile(os.path.join(image_path, f))
    ]
    random_image = random.choice(image_files)
    return send_file(os.path.join(image_path, random_image))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2000)
