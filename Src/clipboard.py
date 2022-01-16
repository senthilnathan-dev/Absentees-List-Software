import os
from datetime import datetime as date
import pyperclip as pc
from Student_DB import db 

date = date.now()

def copied(subject,session,strength):

    with open(os.getcwd()+'\\Temp\\absentees.temp.txt','r') as h1:
        absent = h1.readlines()

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
    for i,name in enumerate(absentees,start=1):
        a= a+f'{i}. {name}'
    
    try:
        pc.copy(a)
    except:
        print('Error occurred while copying text!!')
    else:
        print("<<Text was copied successfully>>")

if __name__ == '__main__':
    copied(subject='verbal',session='fn',strength=58)