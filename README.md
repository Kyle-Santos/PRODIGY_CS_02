# PRODIGY_CS_02

## Pixel Manipulation for Image Encryption Python Program | Prodigy InfoTech Internship

This Python script provides functionality to encrypt and decrypt images using pixel swapping technique. It allows you to securely encrypt an image with a random key and decrypt it later using the same key.

## Usage

To use this script, follow the instructions below:

1. Ensure you have Python and pillow installed on your system.

    ```
    pip install pillow
    ```

2. Run the script by executing the following command in your terminal:

    ```
    python ImageEncryption.py [encrypt/decrypt] image_path
    ```

    Replace `[encrypt/decrypt]` with your desired operation (`encrypt` or `decrypt`), and `image_path` with the path to the image file you want to encrypt or decrypt.

3. If you choose to encrypt an image, a random encryption key will be generated and saved to a text file named `encryptionKey.txt` in the same directory as the script.

4. After encryption, the encrypted image will be saved as `encryptedImage.png` in the same directory.

5. If you choose to decrypt an image, you will be prompted to enter the encryption key. Provide the correct key (generated during encryption) to decrypt the image.

6. After decryption, the decrypted image will be saved as `decryptedImage.png` in the same directory.

## Requirements

- Python 3.x
- PIL (Python Imaging Library)

## Important Notes

- Ensure that you remember the encryption key used during encryption. Losing the key will make it impossible to decrypt the image.

- Keep the encryption key secure and do not share it with unauthorized individuals.

- Always verify the integrity of the encrypted and decrypted images to ensure successful encryption and decryption.

