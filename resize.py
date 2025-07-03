import os
from PIL import Image

input_folder = 'input_images'  # Folder with original images
output_folder = 'resized_images'  # Folder to save resized images
resize_dimensions = (800, 600)  # New dimensions (width, height)
output_format = 'JPEG'  

# Creating output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Process each image in the input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        input_path = os.path.join(input_folder, filename)
        try:
            with Image.open(input_path) as img:
                img_resized = img.resize(resize_dimensions)
                base_name = os.path.splitext(filename)[0]
                output_path = os.path.join(output_folder, base_name + '.' + output_format.lower())
                
                img_resized.save(output_path, output_format)
                print(f"Resized and saved: {output_path}")
              
        except Exception as e:
            print(f"Failed to process {filename}: {e}")
