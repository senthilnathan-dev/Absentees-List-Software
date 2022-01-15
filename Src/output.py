import os
from datetime import datetime as d

date = d.now()

def op_terminal(subject,session,strength):

    with open(os.getcwd()+'\\Temp\\absentees.temp.txt','r') as h1:
        absent = h1.readlines()

    with open(os.getcwd()+'\\Data\\NameList.txt','r') as h2:
        usernames = h2.readlines()

    with open(os.getcwd()+'\\Data\\AIDS-Students.txt','r') as h3:
        students = h3.readlines()

    absentees = []
    for i in absent:
        if i in  usernames:
            absentees.append(usernames.index(i))

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
            # for i,name in enumerate(absent,start=1):
            #     print(i,name,end="")
            n = 1
            for i in range(len(absentees)):
                print(n,students[i],end="")
                n+=1
        
    except TypeError as e:
        print(e)

if __name__ == "__main__":
    op_terminal('v','fn',58)
