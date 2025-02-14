import cv2
import numpy as np

def decrypt_message(image_path):
    img = cv2.imread(image_path)

    if img is None:
        print("Error: Image not found!")
        return
    
    c = {i: chr(i) for i in range(256)}

    n, m, z = 0, 0, 0
    decrypted_message = ""

    while True:
        char = c[img[n, m, z]]
        if char == chr(0):  # Stop reading at the null terminator
            break
        decrypted_message += char
        z = (z + 1) % 3
        if z == 0:
            m += 1
            if m >= img.shape[1]:
                m = 0
                n += 1
                if n >= img.shape[0]:
                    break

    # Extract password and message
    if ":" in decrypted_message:
        stored_pass, message = decrypted_message.split(":", 1)
    else:
        print("Corrupted Data")
        return

    entered_pass = input("Enter passcode for decryption: ")

    if entered_pass == stored_pass:
        print("Decrypted message:", message)
    else:
        print("YOU ARE NOT AUTHORIZED!")

if __name__ == "__main__":
    encrypted_img_path = "encryptedImage.png"  # Read from PNG
    decrypt_message(encrypted_img_path)
