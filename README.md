# 🔐 Encryption-Decryption
Secure Data Hiding in Images Using Steganography

## 📌 Overview  
This project implements **secure data hiding in images** using **steganography** techniques with **OpenCV**. It enables **encryption and decryption of hidden messages** inside images.  

## 🚀 Features  
✅ **Image-based encryption & decryption**  
✅ **Uses OpenCV for image processing**  
✅ **LSB Steganography for hiding text inside images**  
✅ **Supports multiple image formats (JPG, PNG, BMP, etc.)**  
✅ **Fast and efficient pixel-based encryption**  

## 🛠️ Technologies Used  
- **Python** 🐍  
- **OpenCV** 🖼️  
- **NumPy** 🔢  

## 📝 How It Works  
### 🔹 Encryption Process  
1️⃣ Load the image using **OpenCV**.  
2️⃣ Convert text message into **binary format**.  
3️⃣ Modify the **least significant bits (LSB)** of pixel values to embed the message.  
4️⃣ Save the encrypted image.  

### 🔹 Decryption Process  
1️⃣ Load the **encrypted image**.  
2️⃣ Extract the **least significant bits** from pixel values.  
3️⃣ Convert binary data back into text.  
4️⃣ Display the **hidden message**.  

## 📂 Project Structure  
📦 Encryption-Decryption
┣ 📜 encryption.py # Encrypts text into an image
┣ 📜 decryption.py # Extracts hidden text from an image
┣ 🖼️ encryptedImage.png # Example encrypted image
┣ 📜 README.md # Project Documentation
┣ 📜 stegno.pptx # Presentation on steganography

**##📢 Contributing**
Want to improve this project? Feel free to fork, create a pull request, or open an issue.

**##📷 Example Output**
🔒 Before Encryption:

🔓 After Encryption (Data Hidden Inside)
