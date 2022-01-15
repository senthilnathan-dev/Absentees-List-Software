import os

def rm_duplicate(obj):
    """
    Filter the duplicates and write in a temprorary file.
    """

    with open(os.getcwd()+"\\Src\\Temp\\rm_dupe.temp.txt",'w') as temp_file:
        temp_file.truncate(0)
        students= set()
        for student in obj:
            if student not in students:
                temp_file.write(student)
                students.add(student)

def st_attended(path):

    # Reading the given attendance 
    with open(path, 'r', encoding= 'UTF-8') as handle:
        n_students= handle.readlines()

    # To remove the first 3 unwanted lines in the txt file 
    for i in range(3):
        n_students.pop(0)

    # Store the sorted names(i.e. sorted by first names). 
    with open(os.getcwd()+"\\Src\\Temp\\sort_first_name.temp.txt", 'r+') as handle:
        handle.truncate(0)      # refer: https://www.delftstack.com/howto/python/python-clear-file/
        for line in n_students:
            if line == "\n":
                continue
            elif line != "Sorted by last name:\n":
                handle.write(line)
            else:
                break

    # To read the content in the temp file
    with open(os.getcwd()+"\\Src\\Temp\\sort_first_name.temp.txt", 'r+') as handle:
        present =handle.readlines()

    rm_duplicate(present)   # To remove the duplicate values in the text file.
