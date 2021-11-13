from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os

load_dotenv()

Key = os.getenv("Key", "")

def encryptText(s):
    f = Fernet(Key.encode())
    return f.encrypt(s.encode())

def encryptImage(request):
    f = Fernet(Key.encode())
    
    path = upload_image(filename)
    f1 = open(path, 'rb') 
    
    image = f1.read() 
    f1.close() 
        
    image1 = bytearray(image) 
    
    for index, values in enumerate(image1): 
        image1[index] = values ^ f 
    
    f2 = open(path, 'wb') 
    
    f2.write(image1) 
    f2.close()
    

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
    

