import os
from datetime import datetime as d
from Student_DB import db

date = d.now()


def op(subject,session,strength):

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
    try:
        print(a)
        
        for i,name in enumerate(absentees,start=1):
            print(i,name,end="")
            
    except TypeError as e:
        print(e)

if __name__ == "__main__":
    op('v','fn',58)
