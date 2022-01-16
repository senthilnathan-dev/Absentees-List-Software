import sys,os

import absentees as ab
import Filter as Ft
import output as op
import clipboard as cb

__version__ = "2022.1.2"

# Paths to access the Temp and Data directories. 
doc_path= os.getcwd()+'\\Data\\help.txt'
RM_dupe_path= os.getcwd()+'\\Temp\\rm_dupe.temp.txt'
NameList_Path = os.getcwd()+"\\Data\\NameList.txt"
absentees_path = os.getcwd()+'\\Temp\\absentees.temp.txt'

def workingdirectory(path):
    """
    Convert a given path into actual workable path inside the ALS(Absentees-List-Software).
    """
    directory = path.split("\\")
    new_directory = ""
    for i in range(len(directory)-1):
        new_directory += directory[i]+'\\'
    new_directory +=directory[-1]

    return new_directory

def document(obj):
    """
    Prin the content in the 'obj'(Document) in the terminal
    """
    if obj == "help":
        with open(doc_path,'r') as h:
            doc = h.read()
        for i in doc:
            print(i,end="")

if __name__ =="__main__":
    print("\nAbsentees-List-Software:\nVersion:",__version__)   # Print the version of ALS.
    ar1 = input("Options: ")

    if ar1 in ['-h','--help']:
        document('help')

    elif ar1 in ["-a", "--attendance"]:
        src= input("Paste the entire textfile location: ")
        
        Ft.st_attended(workingdirectory(src))       # Stores the Students present in the session.
        ab.student_absent(Source1=NameList_Path,source2=RM_dupe_path,destination=absentees_path)    # Stores the Students(AIDS Dept.) absent in the session.

        sub = input("Enter the subject name: ")
        session = input("Enter the timings of the session: ")
        op.op(subject= sub, session= session, strength= 58)    # Prints the absentees details in the terminal

        clip = input("\nCopy to clipboard [Y/N]:")
        if clip in ['y','Y']:
            cb.copied(subject=sub, session=session,strength=58)
        else:
            pass

    elif ar1 in ['-q','--quit']:
        pass
    elif ar1 in ['-as','--allsource']:
        print("\nThis feature is currently under dvelopment")
    else:
        print("\nSomething went wrong plz try again!!")

    input("\n\npress any key to exit... ")
    