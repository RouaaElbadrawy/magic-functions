class Student():
    def __init__(self,name,grade=8):
        self.name=name
        self.grade=grade
    
    def __str__(self):
        return "Student:" + str(self.name) + " , grade:" + str(self.grade)
    
    def __eq__(self, other):
        return self.grade == other.grade
    
    def __lt__(self, other):
        return self.grade < other.grade
    
    def __le__(self , other):
        return self.grade <= other.grade
        
    def __gt__(self,other):
        return self.grade > other.grade
    
    def __ge__(self,other):
        return self.grade >= other.grade
    
    def __add__(self,other):
        return Student(self.name + ' & ' + other.name, self.grade + other.grade)
    
    def __sub__(self , other):
        return Student(self.name + ' & ' + other.name, self.grade - other.grade)
 


s1 = Student("Ahmed", 90)
s2 = Student("Nada", 98)
print(str(s1))
print(str(s2))

print(s1==s2)
print(s1<s2)
print(s1<=s2)
print(s1>s2)
print(s1>=s2)
s3 = s1+s2
print(s3)
s4 = s1-s2
print(s4)






