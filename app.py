from flask import Flask, request, render_template, send_from_directory, jsonify, url_for
import os
import cv2
import imageio
import datetime

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        processed_filename = 'processed_' + file.filename
        process_video(filepath, processed_filename)
        return jsonify({'video_url': url_for('uploaded_file', filename=processed_filename)})

def process_video(filepath, filename):
    # Create directory for frames
    frames_dir = os.path.join(app.config['UPLOAD_FOLDER'], 'frames')
    os.makedirs(frames_dir, exist_ok=True)

    # Capture video
    video = cv2.VideoCapture(filepath)
    fps = int(video.get(cv2.CAP_PROP_FPS))
    success, image = video.read()
    count = 0
    frame_files = []

    while success:
        timestamp = str(datetime.timedelta(seconds=count // fps)).replace(':', '-')
        frame_name = f"{frames_dir}/frame_{count}_{timestamp}.jpg"
        cv2.putText(image, timestamp, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.imwrite(frame_name, image)
        frame_files.append(frame_name)
        success, image = video.read()
        count += 1

    # Merge frames into video using imageio
    processed_video_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    writer = imageio.get_writer(processed_video_path, fps=fps)
    for frame_file in frame_files:
        frame = imageio.imread(frame_file)
        writer.append_data(frame)
    writer.close()

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
