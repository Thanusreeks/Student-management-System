import json

student_file = 'students.json'

def load_students():
    try:
        with open(student_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_students(students):
    with open(student_file, 'w') as f:
        json.dump(students, f)

student = load_students()


def addstudent():
    id=int(input("Enter the roll no.:"))
    name=input("Enter the name:")
    dept=input("Enter the department:")
    mark=int(input("Enter the mark:"))
    phn=int(input("Enter the phone no.:"))
    student.append([id,name,dept,mark,phn])
    save_students(student)
    print("Student Registered Successfully")

def updatestudent():
    id = int(input("Enter the id:"))
    for i in student:
        if i[0] == id:
            print("Select a field to update")
            print("1.Name")
            print("2.Department")
            print("3.Mark")
            print("4.Phone no")
            print("5.Exit")
            field = input("Enter your choice:")
            if field=='1':
                i[1]=input("Enter new name:")
            elif field =='2':
                i[2]=input("Enter new department")
            elif field == '3':
                i[3]=int(input("Enter new mark:"))
            elif field == '4':
                i[4]=int(input("Enter new Phone no:"))
            elif field=='5':
                break
            save_students(student)
            print("Student Details Updated")
        else:
            print("Student not found")
def removestudent():
    id=int(input("Enter the roll no:"))
    for i in student:
        if i[0]==id:
            student.remove(i)
            save_students(student)
    print("Student Removed Successfully")

def search():
    id = int(input("Enter the roll no:"))
    for i in student:
        if i[0] == id:
            print("Name of the student:",i[1])
            print("Department:",i[2])
            print("Mark:", i[3])
            print("Phone No:", i[4])
        else:
            print('Student not found')
def display():
    for i in student:
        print(i)

def main():
    while True:
        print("Student Management System")
        print("1.Student Registration")
        print("2.Update Student Details")
        print("3.Delete Student Details")
        print("4.Search Student ")
        print("5.Display All Student Details")
        print("6.Exit")
        choice = int(input("Enter your choice:"))
        if choice == 1:
            addstudent()
        elif choice == 2:
            updatestudent()
        elif choice == 3:
            removestudent()
        elif choice == 4:
            search()
        elif choice==5:
            display()
        elif choice==6:
            break
        else:
            print("Invalid choice")
main()

