# ProCenter

ProCenter is a Python program that customizes your desktop wallpaper automatically at set intervals using a collection of images defined by the user. This program is designed for Windows operating systems.

## Features

- Automatically changes the desktop wallpaper at user-specified intervals.
- Uses images from a user-defined folder.
- Simple command-line interface for configuration.

## Requirements

- Python 3.x
- Windows operating system

## Installation

1. Ensure Python 3.x is installed on your Windows machine. You can download it from [python.org](https://www.python.org/downloads/).

2. Download or clone this repository to your local machine.

## Usage

1. Open a command prompt or terminal.

2. Navigate to the directory where `procenter.py` is located.

3. Run the program by typing:

   ```bash
   python procenter.py
   ```

4. When prompted, enter the full path to the folder containing your images.

5. Enter the interval in minutes at which you want the wallpaper to change.

## Example

```plaintext
Enter the path to your image folder: C:\Users\YourUsername\Pictures\Wallpapers
Enter the interval in minutes to change wallpaper: 10
```

This will change your desktop wallpaper every 10 minutes using images from the specified folder.

## Troubleshooting

- Ensure the path to the image folder is correct.
- Make sure you have read permissions for the folder and images.
- The program must be running continuously to keep changing wallpapers.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## Acknowledgments

- Inspired by the need to keep desktop environments fresh and engaging.