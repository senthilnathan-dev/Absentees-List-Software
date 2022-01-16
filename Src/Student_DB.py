# This module stores the Canvas username and the student names in a linked list fashion. 
# Inorder to gain the correct name of the student using their Canvas usernames.

import os

class Node:

    def __init__(self,user_name, student_name):
        
        self.user_name = user_name
        self.student_name = student_name
        self.next = None

    def SetNext(self,pointer):
        self.next = pointer

    def get_student_name(self):
        return [self.user_name,self.student_name]
    
    def getNext(self):
        return self.next

class Student:
    """
    Stores the Canvas usernames and the student names.
    """
    def __init__(self) -> None:
        self.head = None

    def add(self,username_name,student_name):
        temp = Node(username_name, student_name)
        temp.SetNext(self.head)
        self.head = temp
    
    def search(self,user_name):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_student_name()[0] == user_name:
                return current.get_student_name()[1]
                found= True 
            else:
                current= current.getNext()
        return found
    
    def size(self):
        current= self.head
        count = 0
        while current!= None:
            count+= 1
            current = current.getNext()
        return count 
    
    def getAllData(self):
        current= self.head
        elements= []
        while current:
            elements.append(current.get_student_name())
            current= current.getNext()
        return elements
    
db = Student()

# Accessing the students namelist and Canvas user namelist
with open(os.getcwd()+'\\Data\\AIDS-Students.txt','r') as h1:
    Students = h1.readlines()
with open(os.getcwd()+'\\Data\\NameList.txt','r') as h2:
    Users = h2.readlines()

# Adding both usernames with respect to their names to the Linked list.
for i in range(len(Students)):
    db.add(Users[i],Students[i])



if __name__ == '__main__':
    # Searching the student name based on their Canvas user name.
    for i,name in enumerate(Users,start=1):
        print(i,db.search(name),end="")