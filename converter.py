import pytesseract
from PIL import Image

# Load the image
image_file = 'text_image.jpg'
image = Image.open(image_file)

# Convert the image to grayscale
image = image.convert('L')

# Use Tesseract to extract text from the image
text = pytesseract.image_to_string(image)

# Save text into a txt.file
with open('output.txt', 'w') as file:
    file.write(text)