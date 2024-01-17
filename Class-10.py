
class student:
    def __init__(self,name,age,mobile,address):
        self.name = name
        self.age = age
        self.phone = mobile
        self.address = address
    print()
    def student_info(self):
        print(f"Student Name is: {self.name}\nstudent age is: {self.age}\nstudent Phone number is: {self.phone}\nstudent address is: {self.address}")
        
    def python(self, programming):
        print(f"{programming}")
        
        
s1 = student("Manoj Gain", "33", "01911715356", "Kotalipara")
s1.student_info()
print()

s2 = student("Bithi Gain", "23", "01911715356", "Kotalipara")
s2.student_info()




