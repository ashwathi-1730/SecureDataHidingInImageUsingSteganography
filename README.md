# SecureDataHidingInImageUsingSteganography

## Overview
This project is an **Secure Data Hiding in Image Using Steganography** that allows users to **securely hide and retrieve messages** within image files using **Least Significant Bit (LSB) encoding**. It provides an easy-to-use GUI built with Tkinter and includes **password protection** to ensure that only authorized users can access the hidden message.

## Features
- **Image Encryption & Decryption**: Embed and extract secret messages in images.
- **Password Protection**: Ensures that only users with the correct password can decrypt the message.
- **User-Friendly GUI**: Built with Tkinter for easy navigation.
- **Error Handling**: Prevents encoding if the message is too large or an incorrect password is entered.
- **Supports Multiple Image Formats**: Works with `.jpg`, `.jpeg`, and `.png` files.

## Technologies Used
- **Programming Language**: Python
- **Libraries**:
  - `cv2 (OpenCV)`: Image processing
  - `os`: File handling and system operations
  - `tkinter`: GUI development
  - `filedialog`: File selection through GUI
  - `messagebox`: User notifications
- **Steganography Technique**: Least Significant Bit (LSB) Encoding
- **Platform**: Windows (adaptable for other OS)

## Installation
### Prerequisites
Ensure you have Python installed on your system. You also need the required dependencies.
pip install opencv-python

### Clone the Repository

git clone https://github.com/ashwathi-1730/SecureDataHidingInImageUsingSteganography.git
cd image-steganography

## Usage
### Running the Encryption Tool
1. Open a terminal in the project directory and run:
   python encryptor.py
2. Select an image using the GUI.
3. Enter the secret message and a password.
4. Click **Encrypt**, and the message will be hidden inside the image.
5. The encrypted image will be saved as `encryptedImage.png`, and the password will be stored in `passcode.txt`.

### Running the Decryption Tool
1. Open a terminal in the project directory and run:
   python decryptor.py
2. Select the encrypted image using the GUI.
3. Enter the correct password.
4. Click **Decrypt**, and the hidden message will be displayed.



## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



