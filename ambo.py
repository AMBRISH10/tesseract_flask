from flask import Flask, render_template, request
from PIL import Image
import pytesseract

app = Flask(__name__)

# Set the path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = 'path_to_tesseract_executable' # Provide the path to your Tesseract executable

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return render_template('index.html', message='No file part')
    
    file = request.files['file']
    if file.filename == '':
        return render_template('index.html', message='No selected file')
    
    if file:
        image = Image.open(file)
        text = pytesseract.image_to_string(image)
        return render_template('result.html', text=text)

if __name__ == '__main__':
    app.run(debug=True)
