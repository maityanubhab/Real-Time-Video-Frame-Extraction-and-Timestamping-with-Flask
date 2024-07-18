# Real-Time Video Frame Extraction and Timestamping with Flask

This project is a web application built using Flask that allows users to upload videos, processes the videos by extracting frames and timestamping them, and then displays the processed video back to the user. The application also shows the processing progress and allows users to download the processed video.

## Features

- Upload videos for processing.
- Extracts frames from the uploaded video.
- Adds real-time timestamps to each frame.
- Reassembles the frames into a processed video.
- Displays the processing progress.
- Allows users to download and view the processed video.

## Prerequisites

- Python 3.7+
- pip (Python package installer)

## Installation

1. **Clone the repository**:

    ```sh
    git clone https://github.com/maityanubhab/Real-Time-Video-Frame-Extraction-and-Timestamping-with-Flask.git
    cd your-repo-name
    ```

2. **Create and activate a virtual environment**:

    ```sh
    python -m venv .venv
    .venv\Scripts\activate  # On Windows
    source .venv/bin/activate  # On MacOS/Linux
    ```

3. **Install the required dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Flask application**:

    ```sh
    python app.py
    ```

2. **Open your web browser and navigate to** `http://127.0.0.1:5000`.

3. **Upload a video file** and wait for the processing to complete.

4. Once the processing is complete, the processed video with timestamps will be displayed and available for download.

## Creating an Executable

To create a standalone executable from the Flask application using PyInstaller:

1. **Install PyInstaller**:

    ```sh
    pip install pyinstaller
    ```

2. **Generate the executable**:

    ```sh
    pyinstaller --name=flask_app --onefile --add-data "templates;templates" --add-data "uploads;uploads" app.py
    ```

3. The executable will be created in the `dist` directory.

## File Structure

```plaintext
your-repo-name/
│
├── app.py               # Main Flask application file
├── requirements.txt     # Python dependencies
├── templates/           # HTML templates
│   └── index.html       # Main HTML file for the web interface
├── uploads/             # Directory for uploaded and processed videos
└── README.md            # This README file
