from PIL import Image
import sys
import random

# Encryption function with pixel swapping
def encryptImage(imagePath, key):
    # Open the image
    img = Image.open(imagePath)
    width, height = img.size
    
    # Convert the image to RGB mode
    imgRgb = img.convert("RGB")
    
    # Get the pixel data
    pixels = imgRgb.load()
    
    permutationOrder = list(range(width * height))
    permutationOrder.sort(key=lambda x: (key * x) % (width * height))  # Use key to generate permutation order
    
    # Create a new image for the encrypted pixels
    encryptedImg = Image.new("RGB", (width, height))
    encryptedPixels = encryptedImg.load()
    
    # Iterate over each pixel and perform encryption with pixel swapping
    for i in range(width * height):
        x1, y1 = i % width, i // width  # Current pixel position
        x2, y2 = permutationOrder[i] % width, permutationOrder[i] // width  # New pixel position
        
        # Swap pixel colors
        encryptedPixels[x2, y2] = pixels[x1, y1]
    
    # Save the encrypted image
    encryptedImagePath = "encryptedImage.png"
    encryptedImg.save(encryptedImagePath)
    print("Image encrypted successfully.")
    return encryptedImagePath


# Decryption function with pixel swapping
def decryptImage(encryptedImagePath, key):
    # Open the encrypted image
    encryptedImg = Image.open(encryptedImagePath)
    width, height = encryptedImg.size
    
    # Get the pixel data
    encryptedPixels = encryptedImg.load()
    
    # Generate the inverse permutation order based on the key
    inversePermutationOrder = list(range(width * height))
    inversePermutationOrder.sort(key=lambda x: (key * x) % (width * height))  # Use key to generate permutation order
    
    # Create a new image for the decrypted pixels
    decryptedImg = Image.new("RGB", (width, height))
    decryptedPixels = decryptedImg.load()
    
    # Iterate over each pixel and perform decryption with pixel swapping
    for i in range(width * height):
        x1, y1 = i % width, i // width  # Current pixel position
        x2, y2 = inversePermutationOrder[i] % width, inversePermutationOrder[i] // width  # Original pixel position
        
        # Swap pixel colors
        decryptedPixels[x1, y1] = encryptedPixels[x2, y2]
    
    # Save the decrypted image
    decrypted_image_path = "decryptedImage.png"
    decryptedImg.save(decrypted_image_path)
    print("Image decrypted successfully.")
    return decrypted_image_path

def generateRandomKey():
    # Generate a random key
    key = random.randint(100, 999999)
    return key

def saveKeyToFile(key, filename):
    # Save the key to a text file
    with open(filename, 'w') as file:
        file.write(str(key))

def main():
    if len(sys.argv) != 3:
        print("usage: Python ImageEncryption [encrypt/decrypt] image_path")
        return

    option = sys.argv[1].lower()
    imagePath = sys.argv[2]

    if option == "encrypt":
        # generate a random key
        encryptionKey = generateRandomKey()
        saveKeyToFile(encryptionKey, "encryptionKey.txt")

        # Encrypt the image with pixel swapping
        encryptImage(imagePath, encryptionKey)
    elif option == "decrypt":
        key = int(input("Enter key: "))
        # Decrypt the image with pixel swapping
        decryptImage(imagePath, key)
    else:
        print("usage: Python ImageEncryption [encrypt/decrypt] image_path")

if __name__ == "__main__":
    main()
