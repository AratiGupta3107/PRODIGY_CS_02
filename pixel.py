from PIL import Image
import random

def encrypt_image(image_path, output_path, key):
    # Open the image
    image = Image.open(image_path)
    pixels = list(image.getdata())
    width, height = image.size
    
    # Set the random seed
    random.seed(key)
    
    # Perform pixel manipulation (swapping and adding)
    for i in range(len(pixels)):
        # Swap pixels randomly
        j = random.randint(0, len(pixels) - 1)
        pixels[i], pixels[j] = pixels[j], pixels[i]
        
        # Apply a simple mathematical operation to each pixel (e.g., adding 50 to RGB values)
        pixels[i] = tuple((value + 50) % 256 for value in pixels[i])
    
    # Create a new image from the manipulated pixels
    encrypted_image = Image.new(image.mode, image.size)
    encrypted_image.putdata(pixels)
    encrypted_image.save(output_path)
    print(f"Image encrypted and saved as {output_path}")

def decrypt_image(image_path, output_path, key):
    # Open the image
    image = Image.open(image_path)
    pixels = list(image.getdata())
    width, height = image.size
    
    # Set the random seed
    random.seed(key)
    
    # Reverse pixel manipulation (subtracting and swapping)
    for i in range(len(pixels)):
        # Reverse the mathematical operation
        pixels[i] = tuple((value - 50) % 256 for value in pixels[i])
    
    # Reverse the pixel swapping
    for i in range(len(pixels) - 1, -1, -1):
        j = random.randint(0, len(pixels) - 1)
        pixels[i], pixels[j] = pixels[j], pixels[i]
    
    # Create a new image from the manipulated pixels
    decrypted_image = Image.new(image.mode, image.size)
    decrypted_image.putdata(pixels)
    decrypted_image.save(output_path)
    print(f"Image decrypted and saved as {output_path}")

# Example usage:
image_path = "input_image.png"  # Replace with your input image path
encrypted_image_path = "encrypted_image.png"
decrypted_image_path = "decrypted_image.png"
encryption_key = 1234  # Replace with your desired key

# Encrypt the image
encrypt_image(image_path, encrypted_image_path, encryption_key)

# Decrypt the image
decrypt_image(encrypted_image_path, decrypted_image_path, encryption_key)
