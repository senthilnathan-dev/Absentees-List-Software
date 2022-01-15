import os
from datetime import datetime as d

from Student_DB import db
date = d.now()

def op(subject,session,strength):


    with open(os.getcwd()+'\\Temp\\absentees.temp.txt','r') as h1:
        absent = h1.readlines()

    with open(os.getcwd()+'\\Data\\NameList.txt','r') as h2:
        usernames = h2.readlines()

    with open(os.getcwd()+'\\Data\\AIDS-Students.txt','r') as h3:
        students = h3.readlines()

        absentees = []        
        for i in range(len(absent)):
            absentees.append(db.search(absent[i]))
        a= f"""\
Date: {date.day}-{date.month}-{date.year}
Subject: {subject.capitalize()}
Session: {session}
Total Strength : {strength}
Present: {strength-len(absent)}
Absent : {len(absent)}

Absentees:
----------\n"""
    try:
        print(a)
        
        for i,name in enumerate(absentees,start=1):
            print(i,name,end="")
            
    except TypeError as e:
        print(e)

    def clip_to_board():
    
        with open(os.getcwd()+'\\Temp\\clip.temp.txt','w') as h0:
            h0.truncate(0)
            h0.writelines(a)
            for i,name in enumerate(absentees,start=1):
                h0.write(f"{i}.{name}")

    clip_to_board()
if __name__ == "__main__":
    op('v','fn',58)
    # with open(os.getcwd()+'\\Temp\\absentees.temp.txt','r') as h1:
        # absent = h1.readlines()
    # print(len(absent))