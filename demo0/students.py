class Student:
    def __init__(self, ID, years):
        self.ID = ID
        self.years = years
    def exists(ID):
        for i in students:
            if i.ID == ID:
                return True
        return False

def sortFunc(e):
    return e.years

students = []

while 1:
    try:
        normalDuration = int(input("Normal Duration: "))
        if normalDuration <= 0 :
            raise Exception("Enter a positive number")
        break
    except Exception as e:
        print(str(e))
        
while 1:
    try:
        studentSampleSize = int(input("Student Sample Size: "))
        if studentSampleSize <= 0 :
            raise Exception("Enter a positive number")
        break
    except Exception as e:
        print(str(e))
i = 0
while i < studentSampleSize :   
    while 1:
        try:
            string = "Student " + str(i + 1) + " ID and years?: "
            studentIDandYears = input(string).split()
            if len(studentIDandYears) != 2:
                raise Exception("Enter 2 arguments")
            studentID = int(studentIDandYears[0])
            if studentID < 0 or Student.exists(studentID):
                raise Exception("Wrong ID")
            studentYears = int(studentIDandYears[1])
            if studentYears < 0 or studentYears < normalDuration or studentYears > normalDuration * 2:
                raise Exception("Invalid years")
            students.append(Student(int(studentIDandYears[0]), int(studentIDandYears[1])))
            break
        except Exception as e:
            print(str(e))
    i += 1

students.sort(key=sortFunc)
onTime = 0
totalLengthofStudy = 0
for i in students:
    if i.years == normalDuration:
        onTime += 1
    totalLengthofStudy += i.years

print(onTime, " students finished on time {:.2f}".format(onTime / studentSampleSize * 100), "%")
print("Average length of study: ", totalLengthofStudy / studentSampleSize)
print("Median length of study: ", students[(int(studentSampleSize / 2))].years)