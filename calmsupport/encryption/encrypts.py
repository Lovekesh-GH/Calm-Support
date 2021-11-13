from cryptography.fernet import Fernet
from PIL import Image
from dotenv import load_dotenv
import os

load_dotenv()

Key = os.getenv("Key", "")

def encryptText(s):
    f = Fernet(Key.encode())
    return f.encrypt(s.encode())

def encryptImage(path):
    f = 34

    image = Image.open(path).tobytes()

    image1 = bytearray(image) 

    for index, values in enumerate(image1): 
        image1[index] = values ^ f 

    return image1
    

def encryptAudio(filename, key):

    f = Fernet(key)
    path = upload_audio(filename)
    with open(path, "rb") as file:
        # read all file data
        file_data = file.read()
    
    encrypted_data = f.encrypt(file_data)

    with open(path, "wb") as file:
         file.write(encrypted_data)

def encryptVideo(filename, key):

    f = Fernet(key)
    path = upload_video(filename)
    with open(path, "rb") as file:
        # read all file data
        file_data = file.read()
    
    encrypted_data = f.encrypt(file_data)

    with open(path, "wb") as file:
         file.write(encrypted_data)
    

