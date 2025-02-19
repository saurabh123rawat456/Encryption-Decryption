Encryption-Decryption 🛡️🔒
Secure Data Hiding in Images Using Steganography

📌 Overview
This project implements image steganography using encryption and decryption techniques. It enables secure data hiding within images using OpenCV.

🚀 Features
✅ Encrypt messages inside images 📷
✅ Decrypt hidden messages from images 🔍
✅ Uses OpenCV for image processing 🖼️
✅ Simple and efficient Python implementation

🛠️ Technologies Used
Python 🐍
OpenCV 🖼️
NumPy 🔢
🔧 Installation
1️⃣ Clone this repository:

sh
Copy
Edit
git clone https://github.com/saurabh123rawat456/Encryption-Decryption.git
cd Encryption-Decryption
2️⃣ Install dependencies:

sh
Copy
Edit
pip install opencv-python numpy
📝 Usage
🔹 Encryption
Run the script to hide a message inside an image:

sh
Copy
Edit
python encryption.py
Provide the image and secret message as input.

🔹 Decryption
Extract the hidden message from the image:

sh
Copy
Edit
python decryption.py
Enter the encrypted image file name.

📷 Example Output
🔒 Before Encryption:

🔓 After Encryption (Data Hidden Inside)

📂 File Structure
pgsql
Copy
Edit
📂 Encryption-Decryption  
 ├── encryption.py       # Encrypts message into image  
 ├── decryption.py       # Extracts message from image  
 ├── encryptedImage.png  # Sample encrypted image  
 ├── mypic.jpg           # Sample image  
 ├── stegno.pptx         # Presentation on steganography  
 ├── README.md           # Project documentation  
💡 Future Improvements
🔹 Support for different image formats
🔹 Improved encryption algorithms
🔹 GUI for ease of use

📢 Contributing
Want to improve this project? Feel free to fork, create a pull request, or open an issue.
