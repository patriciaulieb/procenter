import os
import ctypes
import time
from datetime import datetime
from pathlib import Path

class ProCenter:
    def __init__(self, image_folder, interval_minutes):
        self.image_folder = Path(image_folder)
        self.interval = interval_minutes * 60  # Convert minutes to seconds
        self.image_files = list(self.image_folder.glob('*.*'))
        self.current_index = 0

    def set_wallpaper(self, image_path):
        ctypes.windll.user32.SystemParametersInfoW(20, 0, str(image_path), 3)

    def run(self):
        if not self.image_files:
            print("No images found in the specified folder.")
            return

        while True:
            try:
                current_image = self.image_files[self.current_index]
                print(f"Setting wallpaper to: {current_image}")
                self.set_wallpaper(current_image)

                self.current_index = (self.current_index + 1) % len(self.image_files)

                time.sleep(self.interval)
            except KeyboardInterrupt:
                print("\nProCenter stopped.")
                break
            except Exception as e:
                print(f"An error occurred: {e}")
                break

if __name__ == "__main__":
    image_folder = input("Enter the path to your image folder: ")
    interval_minutes = int(input("Enter the interval in minutes to change wallpaper: "))

    pro_center = ProCenter(image_folder, interval_minutes)
    pro_center.run()