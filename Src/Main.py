import Filter as Ft
import absentees as ab
import sys
import os

__version__ = "2022.1.1"

doc_path= 'D:\\Python\\programs\\Projects\\Attendance-Project\\Data\\'

def workingdirectory(path):
    directory = path.split("\\")
    new_directory = ""
    
    for i in range(len(directory)-1):
        new_directory += directory[i]+'\\'
    new_directory +=directory[-1]

    return new_directory

def document(obj):
    if obj == "help":
        with open(doc_path+'help.txt','r') as h:
            doc = h.read()
        for i in doc:
            print(i,end="")

if __name__ =="__main__":
    ar1 = sys.argv[1]

    if ar1 in ["-v","--version"]:
        print(__version__)
    elif ar1 in ['-h','--help']:
        document('help')
    elif ar1 in ["-a", "--attendance"]:
        src= input("Paste the entire textfile location: ")
        Ft.st_attended(workingdirectory(src))
        ab.student_absent()