import ctypes
import os
import time

# List of image file paths
image_paths = [
    r"C:\Users\lothart.IMPERIAL\OneDrive - DP World\Desktop\wallaper\4172586.jpg",
    r"C:\Users\lothart.IMPERIAL\OneDrive - DP World\Desktop\wallaper\2052375.jpg",
]

# Check if the files exist
if not all(os.path.exists(path) for path in image_paths):
    print("Image file not found.")
    exit(1)

SPI_SETDESKWALLPAPER = 0x0014

# Initialize an index to track the current image
current_image_index = 0

while True:
    # Get the path of the current image
    current_image_path = image_paths[current_image_index]

    # Set the wallpaper
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, current_image_path, 3)

    print(f"Wallpaper changed to: {current_image_path}")

    # Increment the index to move to the next image
    current_image_index = (current_image_index + 1) % len(image_paths)

    # Wait for 5 seconds
    time.sleep(5)
