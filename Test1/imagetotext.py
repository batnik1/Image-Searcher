from PIL import Image
import pytesseract
import os

def imtxt(path):
    text = pytesseract.image_to_string(Image.open(path), lang="eng")
    return text

def folders(path,word):
    # Search all files ending with .png or .jpg in the path
    returning=[]
    for file in os.listdir(path):
        print("Not",file)
        if file.endswith(".png") or file.endswith(".jpg"):
            all_text=imtxt(path + file)
            # search for the word in the text string search expression
            if word in all_text:
                # append name of file to list
                returning.append(file)
                
    return returning

print(folders("/home/batnik/Music/Pictures/","sle"))

