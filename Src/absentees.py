import os,sys

def isthere(students,student):
    """
    Return boolean based on whether student is present or not using Binary search algorithm.
    """
    first = 0
    last = len(students)-1
    students.sort()
    while first<=last:
        mid = (first+last)//2
        if students[mid] == student:
            return True
        elif students[mid]<student:
            first = mid+1
        elif students[mid]>student:
            last = mid-1
    return False


def student_absent(Source1,source2,destination):
    """
    Write absentees list(absentees) to a text file by comparing the name list(source1) and the present list(source2). 
    """
    try:

        # Reading the list of students which will be the source list for finding absentees.
        with open(Source1,'r') as handle2:
            name_list = handle2.readlines()

        # Reading the list of students from file(note: this file contains filetered list of dupliicates).
        with open(source2,'r') as handle:
            present = handle.readlines()
        
        with open(destination,'r+') as handle3:
            handle3.truncate(0)
            for i in name_list:
                presence= isthere(present, i)   # Calling the function to find the presence of particular student.
                if presence == False:
                    handle3.write(i)

    except FileNotFoundError as e1:
        print("Some File/Files not found, Error occurred in absentees.py",e1,sep="\n",end="\n")
         
    except UnboundLocalError as e2:
        print("Error occurred in absentees.py", e2,sep="\n",end="\n")
