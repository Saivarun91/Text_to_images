# Manga Story Generator

This project allows you to generate manga-style images based on text descriptions using the Hugging Face API. The application takes a scene description as input and generates a manga-style image with a speech bubble containing part of the input text.

## Features
- Generate manga-style images using text descriptions.
- Add speech bubbles to the generated manga panels.
- Provide a download link for the generated manga image.

## Requirements
Before running the application, ensure that you have the following dependencies installed:

- Python 3.6 or higher
- Streamlit
- Requests
- Pillow
- Python-dotenv

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/manga-story-generator.git
    cd manga-story-generator
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # For macOS/Linux
    venv\Scripts\activate     # For Windows
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory and add your **Hugging Face API Key**:

    ```bash
    HUGGINGFACE_API_KEY=your_huggingface_api_key
    ```

    You can get your API key from your Hugging Face account at: [Hugging Face Tokens](https://huggingface.co/settings/tokens).

## Usage

1. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

2. Open the application in your browser. You should see an input box to enter a scene description. Upon clicking "Generate Manga Panel," the application will create a manga-style image with the scene description and a speech bubble containing part of the input text.

3. You can download the generated manga panel by clicking the **Download Manga Panel** button.

## How It Works

1. The app takes user input via a text area (scene description).
2. The text is sent to Hugging Face's **Stable Diffusion** model via an API request to generate a manga-style image.
3. Once the image is generated, a speech bubble is added with a part of the user’s input.
4. The final manga image is displayed, and a download link is provided.

## Troubleshooting

- **API Key Issues:** If you receive errors related to the API key, ensure your Hugging Face key is valid and correctly added to the `.env` file.
- **503 Service Unavailable:** If you encounter a 503 error, it may indicate that Hugging Face's servers are temporarily unavailable. You can try again later or implement retries in your code.
- **Time Out:** If the API takes too long to respond, increase the timeout setting in the request headers.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
