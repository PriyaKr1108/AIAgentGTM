import os
from flask import Flask, request, jsonify, render_template
from pdf_handler import extract_text_from_pdfs

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'pdfs' not in request.files:
        return jsonify({'error': 'No files uploaded'}), 400

    files = request.files.getlist('pdfs')
    texts = []
    for file in files:
        if file.filename.endswith('.pdf'):
            text = extract_text_from_pdfs(file)
            texts.append(text)

    return jsonify({'texts': texts})

if __name__ == '__main__':
    app.run(debug=True)
