OCR Image to Text Converter

This script extracts text from an image using Tesseract OCR and Python.
Requirements

    Python Libraries:
        pytesseract
        Pillow (PIL)

    Tesseract OCR:
        Install Tesseract OCR from here and note the installation path.

Setup

    Install dependencies:

    bash

pip install pytesseract pillow

Update the path to your Tesseract installation in the script:

python

    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

    Place the image you want to extract text from in the same directory and name it img.jpg, or update the script with your file path.

Usage

Run the script:

bash

python app.py

The extracted text will be printed in the console.