def command():
    while (True):
        command = (input("#")).lower()
        if   command == "show": show()
        elif command == "search": search(inputsid())
        elif command == "changescore": changeScore(inputsid())
        elif command == "add": add(inputsid())
        elif command == "searchgrade": searchGrade()
        elif command == "remove": remove(inputsid())
        elif command == "quit": quit()
        elif command == "q": break
            
def inputsid(): return (input("Student ID: ")).lower()

def grading (avg):
    if   avg >= 90: grade = "A"
    elif avg >= 80: grade = "B"
    elif avg >= 70: grade = "C"
    elif avg >= 60: grade = "D"
    else: 
        grade ="F"
    return grade

def show():
    row_labels = ['Student','Name','Midterm','Final','Average','Grade']
    print(" {0:9} {1:>15}   {2:^7}   {3:^5}   {4:^7}   {5:^4}".format(*row_labels))
    print("-"*62)
    for k, v in sorted(students.items(), key=lambda item: item[1]["Average"], reverse = True):
        print(k, end='\t')
        printer(k)

def search(sid):
    if sid not in students:
        print("NO SUCH PERSON.")
    else:
        printer(sid)

def changeScore(sid):
    if sid not in students:
        print("NO SUCH PERSON.")
    else:
        mORf = (input("Mid/Final? ")).lower()
        if mORf != "mid" and mORf != "final": return
        newScore = int(input("Input new score: "))
        if newScore > 100 or newScore < 0: print("score not exist");return
        printer(sid)
        if mORf == "mid":     students[sid]["Midterm"] = newScore 
        elif mORf == "final": students[sid]["Final"]   = newScore 
        add_avgrade()
        print("Score Changed")
        printer(sid)        
        
def searchGrade():
    targetGrade = input("Grade to search: ")
    if targetGrade in "ABCDF":
        for sid in students:
            if students[sid]["Grade"] == targetGrade: 
                printer(sid)
        
def add(newID):
    if newID in students:
        print("ALREADY EXIST")
    else:
        name = input("Name: ")
        mid = int(input("Midterm Score: "))
        final = int(input("Final Score: "))
        students[newID] = {"Name" : name, "Midterm": mid, "Final" : final} 
        add_avgrade()
        print("Student added")

def remove(sid):
    if sid not in students:
        print("NO SUCH PERSON.")
    else:
        del students[sid]
        print("Student removed")

def quit():
    yORn = input("Save data?[yes/no]").lower()
    if yORn == "yes":
        fname = input("File name: ")
        data = ""
        for sid in sorted(students.items(), key=lambda item: item[1]["Average"], reverse = True):
            data += sid[0] + "\t"
            for key, value in sid[1].items():
                sid[1][key] = str(value)
            data += '\t'.join(sid[1].values()) + "\n"
        print(data)
        f_write = open(fname, "w")
        f_write.write(data)
        f_write.close()

def printer(sid):
    for values in students[sid].values():
        print(values, end="\t")
    print()

def add_avgrade():
    for sid in students:
        students[sid]["Average"] = (students[sid]["Midterm"] + students[sid]["Final"])/2
        students[sid]["Grade"] = grading(students[sid]["Average"])

import sys
f = open(sys.argv[1], "r")
students = {}
for s in f.readlines():
    s2 = s.rstrip().split()
    students[s2[0]] = {"Name" : " ".join(s2[1:3]), "Midterm": int(s2[3]), "Final" : int(s2[4])}
add_avgrade()
command()
