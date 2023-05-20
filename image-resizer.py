import os
from PIL import Image

def resize_images_in_folder(folder_path, output_folder):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        output_path = os.path.join(output_folder, filename)
        if os.path.isfile(file_path):
            try:
                image = Image.open(file_path)
                resized_image = image.resize((256, 256), Image.ANTIALIAS)
                resized_image.save(output_path)
            except Exception as e:
                print(f"Error resizing image {filename}: {str(e)}")

input_folder_path = r'Synthetix2\test'
output_folder_path = r'Synthetix2\test-resized'
resize_images_in_folder(input_folder_path, output_folder_path)
