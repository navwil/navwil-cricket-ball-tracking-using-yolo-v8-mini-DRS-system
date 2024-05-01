
from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
import cv2
from multiprocessing import Process
from main import split_video_last_frame, detect_and_track, color_pixels_last_frame

app = Flask(__name__)

# Configure upload folder and allowed extensions
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'mp4'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# Function to check if the file extension is allowed
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Route for home page
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        # If user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            # Create the uploads directory if it doesn't exist
            if not os.path.exists(app.config['UPLOAD_FOLDER']):
                os.makedirs(app.config['UPLOAD_FOLDER'])
            # Save uploaded video
            filename = secure_filename(file.filename)
            video_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(video_path)
            # Start processing the video
            p1 = Process(target=detect_and_track, args=(video_path, filename[:-4] + '_coordinates.txt'))
            p2 = Process(target=split_video_last_frame, args=(video_path, os.path.join('static', 'last_frame.jpg')))
            p1.start()
            p2.start()
            p1.join()
            p2.join()
            # Process the colored last frame
            colored_last_frame = color_pixels_last_frame(os.path.join('static', 'last_frame.jpg'),
                                                          filename[:-4] + '_coordinates.txt')
            cv2.imwrite(os.path.join('static', 'colored_last_frame.jpg'), colored_last_frame)
            return render_template('result.html', result_image='colored_last_frame.jpg')
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
