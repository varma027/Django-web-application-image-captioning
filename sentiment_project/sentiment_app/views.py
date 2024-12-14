from django.shortcuts import render
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

# Load the BLIP model and processor
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Function to generate captions for an image
def generate_caption(image):
    inputs = processor(images=image, return_tensors="pt")
    outputs = model.generate(**inputs)
    caption = processor.decode(outputs[0], skip_special_tokens=True)
    return caption

# Home view for uploading images
def home_view(request):
    if request.method == 'POST' and request.FILES.get('image'):
        # Get the uploaded image
        image_file = request.FILES['image']
        image = Image.open(image_file)

        # Generate the caption
        caption = generate_caption(image)

        # Return the result to the result template
        return render(request, 'result.html', {'caption': caption})

    # Render the home page template with the form
    return render(request, 'home.html')
from django.shortcuts import render

def result_view(request):
    # Your view logic here
    return render(request, 'result.html')  # Example: rendering a template
