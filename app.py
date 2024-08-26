import streamlit as st
from PIL import Image
import google.generativeai as genai

# Configure your API key for Google GenAI
genai.configure(api_key='AIzaSyDpjh32y-OvQX5cBYE2BWIArHKfGh3x4yc')  # Replace with your actual Google API key

def main():
    st.title("Image Identifier Using GenAI")

    # File uploader for image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Load the uploaded image using PIL
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)

        # Process the image with the Gemini model
        st.write("Processing the image...")

        # Convert the image to the format expected by the API (PIL.Image.Image)
        model = genai.GenerativeModel('models/gemini-1.5-pro-latest')

        # Assuming the API expects the PIL image directly
        response = model.generate_content(image)  # Pass the image directly

        # Display the response text
        st.write(response.text)

if __name__ == "__main__":
    main()
