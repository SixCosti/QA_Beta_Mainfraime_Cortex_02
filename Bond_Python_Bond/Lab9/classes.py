from statistics import mean


class Student:

    def __init__(self, namevar, agevar, classroomvar):
        self.name = namevar
        self.age = int(agevar)
        self.classroom = classroomvar

    def studentinfo(self):
        return self.age, self.classroom

    def grades(self, sarcasm101var, devopsvar, ghostbustersvar):
        self.sarcasm101 = sarcasm101var
        self.devops = devopsvar
        self.ghostbusters = ghostbustersvar
        meany = mean([self.sarcasm101, self.devops, self.ghostbusters])
        return meany
        
         
tom = Student("Thomas Angelo", 28, "Sarcasm 101")
paulie = Student("Paulie Salieri", 35, "SpecOps")
tom.grades(80,100,65)
print("Tom has the average grade :", tom.grades(80,100,65))

tom.studentinfo()
paulie.studentinfo()

print(tom.studentinfo())
print(paulie.studentinfo())
