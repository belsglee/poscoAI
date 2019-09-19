# grading function

def grading (avg):
    if   avg >= 90: grade = "A"
    elif avg >= 80: grade = "B"
    elif avg >= 70: grade = "C"
    elif avg >= 60: grade = "D"
    else: 
        grade ="F"
    return grade

def search():
    sid = input("Student ID: ")
    printer(sid)

def add():
    newID = input("Student ID: ")
    if (newID in students.keys()):
        print("ALREADY EXIST")
    else:
        name = input("Name: ")
        mid = int(input("Midterm Score: "))
        final = int(input("Final Score: "))
        students[newID] = {"Name" : name, "Midterm": mid, "Final" : final} 
        add_avgrade()
        print("Student added")

def searchGrade():
    targetGrade = input("Grade to search: ")
    gradeset = "ABCDF"
    if targetGrade in gradeset:
        for sid in students:
            if students[sid]["Grade"] == targetGrade: 
                printer(sid)

def remove():
    sid = input("Student ID: ")

    if sid not in students:
        print("NO SUCH PERSON.")
    else:
        del students[sid]
        print("Student removed")

def quit():
    yORn = input("Save data?[yes/no]")
    if yORn == "yes":
        fname = input("File name: ")
        f_write = open(fname, "w")
        f_write.write(show())

def printer(sid):
    for values in students[sid].values():
        print(values, end="\t")
    print()

def command():
    while (True):
        command = input("Please input your command: ")
        if   command == "show": show()
        elif command == "search": search()
        elif command == "changescore": changeScore()
        elif command == "add": add()
        elif command == "searchgrade": searchGrade()
        elif command == "remove": remove()
        elif command == "quit": quit()
        elif command == "q": break

def changeScore():
    sid = input("Student ID: ")
 
    if sid in range(5):
        print("NO SUCH PERSON.")
    else:
        mORf = input("Mid/Final? ")
        if mORf != "mid" and mORf != "final": return
        newScore = int(input("Input new score: "))
        if newScore > 100 or newScore < 0: print("score not exist");return
        printer(sid)
        if mORf == "mid":     students[sid]["Midterm"] = newScore 
        elif mORf == "final": students[sid]["Final"] = newScore 

        add_avgrade()
        print("Score Changed")
        printer(sid)

def add_avgrade():
    for sid in students:
        students[sid]["Average"] = (students[sid]["Midterm"] + students[sid]["Final"])/2
        students[sid]["Grade"] = grading(students[sid]["Average"])

def show():

    columns = "Student\t\tName\t\tMidterm\tFinal\tAverage\tGrade"
    lines = "-------------------------------------------------------------"
    print(columns+"\n"+lines)
    
    for key, value in sorted(students.items(), key=lambda item: item[1]["Average"], reverse=True):
        print(key, end="\t")
        printer(key)

import sys
f = open(sys.argv[1], "r")
students = {}

for s in f.readlines():
    s2 = s.rstrip().split()
    students[s2[0]] = {"Name" : " ".join(s2[1:3]), "Midterm": int(s2[3]), "Final" : int(s2[4])}

add_avgrade()
command()

    
#sort()
#printers()
