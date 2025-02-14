import cv2
import numpy as np

def encrypt_message(image_path, output_path, message, password):
    img = cv2.imread(image_path)

    if img is None:
        print("Error: Image not found!")
        return
    
    msg = password + ":" + message  # Store passcode along with message
    msg += chr(0)  # Null terminator to mark the end of the message

    d = {chr(i): i for i in range(256)}  # Ensure full ASCII range

    n, m, z = 0, 0, 0

    for char in msg:
        img[n, m, z] = d[char]  
        z = (z + 1) % 3
        if z == 0:
            m += 1
            if m >= img.shape[1]:  # Move to the next row if needed
                m = 0
                n += 1
                if n >= img.shape[0]:  # Stop if out of image space
                    print("Message too long for the image!")
                    return

    cv2.imwrite(output_path, img, [cv2.IMWRITE_PNG_COMPRESSION, 0])  # Save as PNG
    print(f"Message encrypted and saved as {output_path}")

if __name__ == "__main__":
    img_path = "mypic.jpg"  # Replace with the correct image path
    output_img = "encryptedImage.png"  # Use PNG to avoid compression issues
    secret_message = input("Enter secret message: ")
    passcode = input("Enter a passcode: ")

    encrypt_message(img_path, output_img, secret_message, passcode)
