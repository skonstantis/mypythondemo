class Student:
    def __init__(self, fname, lname, address, telephone) :
        self.fname = fname
        self.lname = lname
        self.address = address
        self.telephone = telephone
    
class Registry:
    def __init__(self) :
        print("------------------------")
        print("WELCOME!")
        print("------------------------")
        stop = False 
        self.students = []
        
        while True:
            while True:
                userInput = input("\n------------------------\n0/Exit\n1/Add Student\n2/Remove Student\n3/Print Student\n4/Print Students\n\n")
                if userInput == "0":
                    stop = True
                    break
                elif userInput == "1":
                    student = self.readStudent()
                    self.addStudent(student)
                    break
                elif userInput == "2":
                    self.removeStudent()
                    break
                elif userInput == "3":
                    self.printStudent()
                    break
                elif userInput == "4":
                    self.printStudent(True)
                    break
            if stop:
                break

    def readStudent(self):
        fname = input("\nStudent First Name: ")
        lname = input("Student Last Name: ")     
        address = input("Student Address: ")
        telephone = input("Student Telephone: ")
        
        if(fname == "" and lname == "" and address == "" and telephone == ""):
            return None
        
        return (fname, lname, address, telephone)
            
    def addStudent(self, student):
        if(student == None):
            return
        self.students.append(student)
    
    def removeStudent(self):
        fname = input("\nStudent First Name: ")
        lname = input("Student Last Name: ")
        found = False
            
        for student in self.students :
            if student[0] == fname and student[1] == lname:
                self.students.remove(student)
                found = True
                break
        if not found:
            print("\nStudent Not Found")
    
    def printStudent(self, all = False):
        if all == True :
            if len(self.students) == 0:
                print("\nNo Students Found")
            else:
                print("\n")
                for student in self.students :
                    print(student)
        else :
            fname = input("\nStudent First Name: ")
            lname = input("Student Last Name: ")
            found = False
            
            for student in self.students :
                if student[0] == fname and student[1] == lname:
                    print("\n")
                    print(student)
                    found = True
                    break
            if not found:
                print("\nStudent Not Found")

Registry()