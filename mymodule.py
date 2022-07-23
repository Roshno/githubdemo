
class Student:
    marks = []
    def getData(self, rn, name, m1, m2, m3, m4, m5):
        Student.rn = rn
        Student.name = name
        Student.marks.append(m1)
        Student.marks.append(m2)
        Student.marks.append(m3)
        Student.marks.append(m4)
        Student.marks.append(m5)
        
    def displayData(self):
        print ("Roll Number is: ", Student.rn)
        print ("Name is: ", Student.name)
        #print ("Marks in subject 1: ", Student.marks[0])
        #print ("Marks in subject 2: ", Student.marks[1])
        #print ("Marks in subject 3: ", Student.marks[2])
        #print ("Marks in subject 4: ", Student.marks[3])
        #print ("Marks in subject 5: ", Student.marks[4])
        print ("Marks are: ", Student.marks)
        
    
r = int (input("Enter the roll number: "))
name = input("Enter the name: ")
m1 = int (input("Enter the marks in the maths subject: "))
m2 = int (input("Enter the marks in the physics subject: "))
m3 = int (input("Enter the marks in the chemistry subject: "))
m4 = int (input("Enter the marks in the english subject: "))
m5 = int (input("Enter the marks in the programming subject: "))

s1 = Student()
s1.getData(r, name, m1, m2, m3, m4, m5)
s1.displayData()