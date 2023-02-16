# Welcome to your awesome OCR Image-to-Text Converter!

This is a Python program that uses the Tesseract OCR library to extract text from an image file and save it to a text file.

To run this program, you will need to have Python 3 installed on your computer. You will also need to install the Tesseract OCR engine and the pytesseract library. You can install the Tesseract OCR engine by running the following commands in your terminal:

### On Ubuntu/Debian
sudo apt install tesseract-ocr

### On macOS (with Homebrew)
brew install tesseract

### On Windows
Download and install Tesseract OCR from https://github.com/UB-Mannheim/tesseract/wiki


## Vertual Machine
This repo does not contain a vertual machine, so be sure to install one before starting.

### On mac:
To install a venv:

pip install virtualenv

To create a machine for the file:

cd my-project/

virtualenv venv

To turn it on:

source venv/bin/activate

### On windows or Linux:
I will not provide the guidelines for these installations on windows at this moment.
If you know / can learn how to install and run a vertual machine on your system, you can do that, and then proceed to the next stages.

## Before running the program:

1. Install reqirements:

pip install -r requirements.txt

2. Import the image you want to convert into the project file.
3. Change the name of the image to:
    text_image.jpg

## Run the program :)
The program will extract any text from the image and save it to a file named output.txt in the same directory as the image.

You can also specify a different output file name by using the -o or --output flag, like this:

python converter.py path/to/image.jpg -o output.txt