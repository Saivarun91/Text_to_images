import time
import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import uuid
import streamlit as st
from dotenv import load_dotenv
import os
import textwrap

# Load environment variables from .env file
load_dotenv()

# Load Hugging Face API Key from environment variable
huggingface_api_key = os.getenv("HUGGINGFACE_API_KEY")

# Check if the API key is set
if not huggingface_api_key:
    st.error("Hugging Face API key is not set. Please set the HUGGINGFACE_API_KEY environment variable in the .env file.")
    st.stop()  # Stop execution if the API key is missing

# Function to generate manga-style image using Hugging Face's API with retry mechanism
def generate_manga_image(text_prompt):
    api_url = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"
    headers = {"Authorization": f"Bearer {huggingface_api_key}"}
    payload = {"inputs": text_prompt}

    # Retry mechanism
    for _ in range(3):  # Retry up to 3 times
        try:
            response = requests.post(api_url, headers=headers, json=payload, timeout=30)  # Increased timeout to 30 seconds
            if response.status_code == 200:
                return BytesIO(response.content)
            else:
                raise Exception(f"Failed to generate image: {response.status_code}, {response.text}")
        except requests.exceptions.RequestException as e:
            st.warning(f"Error: {e}. Retrying...")
            time.sleep(5)  # Wait for 5 seconds before retrying

    raise Exception("Failed to generate image after multiple retries.")

# Function to add speech bubble

def add_speech_bubble(image, text):
    draw = ImageDraw.Draw(image)

    # Try loading a TrueType font
    try:
        font = ImageFont.truetype("arial.ttf", 24)  # Use any available TTF font
    except:
        font = ImageFont.load_default()

    # Define speech bubble position and size
    bubble_x, bubble_y = 30, 30
    bubble_w, bubble_h = 500, 140

    # Wrap the text into multiple lines
    wrapped_text = textwrap.fill(text, width=40)

    # Draw the speech bubble
    draw.rectangle(
        [bubble_x, bubble_y, bubble_x + bubble_w, bubble_y + bubble_h],
        fill="white",
        outline="black",
        width=3
    )

    # Draw text inside the bubble
    draw.text((bubble_x + 15, bubble_y + 15), wrapped_text, fill="black", font=font)

    return image


# Streamlit UI
st.title("🎨 Manga Story Generator")
user_input = st.text_area("Enter a scene description:")

if st.button("Generate Manga Panel"):
    if user_input:
        st.write("🔄 Generating manga-style illustration...")

        try:
            # Generate image from text
            image_data = generate_manga_image(user_input)
            img = Image.open(image_data)

            # Add speech bubble with user text
            img_with_text = add_speech_bubble(img, user_input[:50] + "...")

            # Show final manga panel
            st.image(img_with_text, caption="Generated Manga Panel", use_column_width=True)

            # Provide download option
            filename = f"manga_panel_{uuid.uuid4().hex}.png"
            img_with_text.save(filename)
            with open(filename, "rb") as file:
                st.download_button("📥 Download Manga Panel", file, filename, "image/png")
        except Exception as e:
            st.error(f"An error occurred: {e}")
