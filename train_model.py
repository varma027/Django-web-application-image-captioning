from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import requests
from io import BytesIO
import torch

def generate_caption(image_path):
    """
    Generate a caption for the provided image.

    Args:
        image_path (str): Path to the image file or URL.

    Returns:
        str: Generated caption or error message.
    """
    try:
        # Load the image from a file or URL
        if image_path.startswith("http"):
            response = requests.get(image_path, stream=True)
            response.raise_for_status()  # Ensure the request was successful
            image = Image.open(BytesIO(response.content))
        else:
            image = Image.open(image_path)

        # Ensure the image is in a valid format
        image.verify()  # Check if it's a valid image
        image = Image.open(image_path)  # Reopen after verification

        # Process the image
        inputs = processor(images=image, return_tensors="pt")
        outputs = model.generate(**inputs)

        # Decode the generated output
        caption = processor.decode(outputs[0], skip_special_tokens=True)
        return caption

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    # Load the BLIP model and processor
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

    # Input from the user
    image_path = input("Enter the path or URL of the image: ").strip()

    # Generate and display the caption
    caption = generate_caption(image_path)
    print(f"Generated Caption: {caption}")
