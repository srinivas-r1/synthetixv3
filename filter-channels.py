from PIL import Image
import os

def delete_images_with_invalid_channels(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            try:
                image = Image.open(file_path)
                num_channels = len(image.split())
                if num_channels !=3 :
                    os.remove(file_path)
                    print(f"Deleted {filename} due to invalid number of color channels.")
            except Exception as e:
                print(f"Error processing image {filename}: {str(e)}")

folder_path = 'Synthetix2-original\harmful'
delete_images_with_invalid_channels(folder_path)
