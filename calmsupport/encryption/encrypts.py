from cryptography.fernet import Fernet
from .key import Key

def encryptText(s):
    f = Fernet(Key.encode())
    return f.encrypt(s.encode())
# key = Fernet.generate_key()
# print(key)

def encryptImage(request):
    f = Fernet(Key.encode())
    # path = os.path.join(Settings.BASEDIR,“ /media/images”)
    f1 = open(request, 'rb') 
    # storing image data in image variable 
    image = f1.read() 
    f1.close() 
        
    # converting image into byte array to 
    # perform encryption on it's data 
    image1 = bytearray(image) 
    # perform XOR operation on each value of bytearray 
    for index, values in enumerate(image1): 
        image1[index] = values ^ f 
   
    f2 = open(request, 'wb') 
    
    f2.write(image1) 
    f2.close()

# def encryptAudio(request):
#     if request.method == 'POST':
#         form = UploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             instance = UploadForm(docfile=request.FILES['audio'])
#             f = Fernet(Key.encode())
#             with open('audio', 'rb') as file:
#                  original = file.read()
        
#             # encrypting the file
#             encrypted = f.encrypt(original)
            
#             # opening the file in write mode and 
#             # writing the encrypted data
#             with open('audio', 'wb') as encrypted_file:
#                 encrypted_file.write(encrypted)
            
#             instance.save()

# def encrypt(filename, key):

#     f = Fernet(key)

#     with open(filename, "rb") as file:
#         # read all file data
#         file_data = file.read()
    
#     encrypted_data = f.encrypt(file_data)

#     with open(filename, "wb") as file:
#         file.write(encrypted_data)
