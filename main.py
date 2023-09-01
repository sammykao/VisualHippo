import numpy as np
from flask import Flask, render_template, request
from captioning import caption
import os
from restaurant import Restaurant
from filterfood import search
from google.cloud import storage
from werkzeug.utils import secure_filename
#*** Backend operation
os.environ['REPLICATE_API_TOKEN'] = ''
app = Flask(__name__)
# WSGI Application
# Defining upload folder path
UPLOAD_FOLDER = os.path.join('static', 'uploads')
# # Define allowed files
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'humptydumpt'
client = storage.Client()
bucket_name = 'visualeats-userdata-uploads'
bucket = client.get_bucket(bucket_name)


@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/',  methods=("POST", "GET"))
def uploadFile():
    if request.method == 'POST':
        # Upload file flask
        img = request.files['uploaded-file']
        latitude = float(request.form.get("user-lat"))
        longitude = float(request.form.get("user-long"))
        safe_base_filename = secure_filename(img.filename)
        blob = bucket.blob(safe_base_filename)
        blob.upload_from_file(img)

        # Extracting uploaded data file name
        # Upload file to database (defined uploaded folder in static path)
        # Storing uploaded file path in flask session
        msg = caption(blob.public_url)
        restaurants = search(msg, latitude, longitude)
        return render_template('display.html', user_image=blob.public_url, msg=msg, restaurants=restaurants)
if __name__=='__main__':
    app.run(debug = True)