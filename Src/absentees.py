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


def student_absent():
    """
    Return a list of absentees list.
    """
    # Reading the list of students from file(note: this file contains filetered list of dupliicates).
    with open("Temp\\rm_dupe.temp.txt") as handle:
        present = handle.readlines()

    # Reading the list of students which will be the source list for finding absentees.
    with open("Data\\NameList.txt") as handle2:
        name_list = handle2.readlines()

    absentees = []
    for i in name_list:
        presence= isthere(present, i)   # Calling the function to find the presence of particular student.
        if presence == False:
            absentees.append(i)
    
    # Temp Test code.
    for i in absentees:
        print(i,end="")
    print("No: of absentees:",len(absentees))


if __name__ == "__main__":
    student_absent()
