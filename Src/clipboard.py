import os 
import pyperclip as pc

clip_path = os.getcwd()+'\\Temp\\clip.temp.txt'

with open(clip_path,'r') as h1:
    content = h1.read()
def copied():
    try:
        pc.copy(content)
    except :
        print("Error ocurred while copying!")
    else:
        print("<Content copied to clip board successfully>")

if __name__ =='__main__':
    copied()