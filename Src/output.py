import os
from datetime import datetime as d

date = d.now()

def op_terminal(subject,session,strength):

    with open(os.getcwd()+'\\Temp\\absentees.temp.txt','r') as h1:
        absent = h1.readlines()
        # h1.truncate(1)
    try:
            print(
            f"""
Date: {date.day}-{date.month}-{date.year}
Subject: {subject.capitalize()}
Session: {session}
Total Strength : {strength}
Present: {strength-len(absent)}
Absent : {len(absent)}

Absentees:
----------\
            """
            )
            for i,name in enumerate(absent,start=1):
                print(i,name,end="")
    except TypeError as e:
        print(e)