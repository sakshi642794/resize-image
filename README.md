# Image Resizer Tool

This Python script allows you to batch resize and convert images from one folder to another using the `Pillow` library.

## Features

* Batch processes all images in a given input folder
* Resizes images to fixed dimensions (default: 800x600)
* Converts all images to a specified format (default: JPEG)
* Automatically creates an output folder if it doesn't exist

## Requirements

* Python 3.x
* Pillow library

Install Pillow if not already installed:

```bash
pip install Pillow
```

## Usage

1. Place all images you want to resize in the `input_images/` folder.
2. Run the script:

```bash
python image_resizer.py
```

3. Resized images will be saved in the `resized_images/` folder.

## Configuration

You can modify the following variables in the script to suit your needs:

```python
input_folder = 'input_images'          # Source images folder
output_folder = 'resized_images'       # Destination folder
resize_dimensions = (800, 600)         # Output dimensions (width, height)
output_format = 'JPEG'                 # Output format
```

## Supported Formats

The script supports the following input image formats:

* .png
* .jpg
* .jpeg

Output format can be changed to any format supported by Pillow (e.g., PNG, BMP).

## Example Output

```
Resized and saved: resized_images/image1.jpeg
Resized and saved: resized_images/photo2.jpeg
```

