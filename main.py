import os
from fastapi import FastAPI, Form, HTTPException
from typing import List

app = FastAPI()

# Path to the letter_images folder
letter_images_path = os.path.join(os.path.dirname(__file__), "letter_images")

# Define an array containing image filenames for each letter of the alphabet
letter_image_filenames = [f"{chr(i + ord('A'))}.PNG" for i in range(26)]

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Sign Language Generation API!"}

@app.post("/generate_sign_language/")
async def generate_sign_language(text: str = Form(...)) -> List[bytes]:
    # Convert the input text to uppercase
    text = text.upper()

    # Initialize a set to store the letters used in the input text
    used_letters = set()

    # Iterate over each character in the input text
    for char in text:
        # Check if the character is an alphabet letter
        if char.isalpha():
            # Add the uppercase version of the character to the set
            used_letters.add(char.upper())

    # Initialize a list to store the bytes of the generated images
    image_bytes_list = []

    # Iterate over each letter in the set of used letters
    for letter in used_letters:
        # Check if the letter is in the array of letter image filenames
        if f"{letter}.PNG" in letter_image_filenames:
            # Generate the image path for the letter
            image_path = os.path.join(letter_images_path, f"{letter}.PNG")

            # Open the image file in binary mode and read its bytes
            with open(image_path, "rb") as image_file:
                image_bytes = image_file.read()

            # Append the image bytes to the list
            image_bytes_list.append(image_bytes)

    return image_bytes_list
