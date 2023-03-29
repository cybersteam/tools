#https://www.geeksforgeeks.org/working-images-python/
import os
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

# The directory that we are interested in
myPath = "."

# The min size of the file in Bytes
mySize = '50000'
#target = 
# All the file paths will be stored in this list
filesList= []

for path, subdirs, files in os.walk(myPath):
    for name in files:
        filesList.append(os.path.join(path, name))

for i in filesList:
    # Getting the size in a variable
    fileSize = os.path.getsize(str(i))

    # Print the files that meet the condition
    if int(fileSize) >= int(mySize):
        #print (f"The File: {str(i)} is: {str(fileSize)} Bytes")
        img = Image.open(str(i))
        width, height = img.size
        #print(width, height)
        img = img.resize((width//2, height//2))
        img.save(str(i))


