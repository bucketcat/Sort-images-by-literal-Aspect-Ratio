
import os
import subprocess

import shutil
import magic
import PIL
from PIL import Image

PIL.Image.MAX_IMAGE_PIXELS = 9000033120000
# Define the directory where the images are located
image_dir = "C:\\aaaa\\bbbb\\cccc\\dddd"

# Define the directory where the sorted images will be saved
output_dir = "D:\\AAAA\\BBBB"
# Define the aspect ratio ranges and corresponding folder names
mime = magic.Magic(mime=True)
for filename in os.listdir(image_dir):
    filepath = os.path.join(image_dir, filename)

    # Check if the current file is a file (not a directory)
    if os.path.isfile(filepath):
        try:
            # Get the file type based on its content
            file_type = mime.from_file(filepath)

            # Check if the file is an image (based on the MIME type)
            if file_type.startswith('image/'):
                # Use magick command to extract the aspect ratio
                cmd = ['magick', 'identify', '-format', '%[fx:w/h]', filepath]
                result = subprocess.run(cmd, capture_output=True, text=True)

                # Get the aspect ratio from the command output
                aspect_ratio = result.stdout.strip()

                # Create the folder name based on the aspect ratio
                folder_name = aspect_ratio.replace(':', '_')

                # Create the output folder if it doesn't exist
                folder_path = os.path.join(output_dir, folder_name)
                os.makedirs(folder_path, exist_ok=True)

                # Move the image to the corresponding folder
                new_filepath = os.path.join(folder_path, filename)
                shutil.move(filepath, new_filepath)
                print(f"Moved {filename} to {folder_name}")
            else:
                print(f"Skipping {filename} - not identified as an image")
        except Exception as e:
            print(f"Skipping {filename} - error while processing the file: {e}")

print("Sorting completed.")