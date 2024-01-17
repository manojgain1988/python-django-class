
# class student:
#     def __init__(self,name,age,mobile,address):
#         self.name = name
#         self.age = age
#         self.phone = mobile
#         self.address = address
#     print()
#     def student_info(self):
#         print(f"Student Name is: {self.name}\nstudent age is: {self.age}\nstudent Phone number is: {self.phone}\nstudent address is: {self.address}")

#     def python(self, programming):
#         print(f"{programming}")


# s1 = student("Manoj Gain", "33", "01911715356", "Kotalipara")
# s1.student_info()
# print()

# s2 = student("Bithi Gain", "23", "01911715356", "Kotalipara")
# s2.student_info()


# =============================Practice========================

# class Student:
#     def __init__(self, name, Id):        # init default constractor/method
#         self.name = name                 # instance variable/property
#         self.id = Id                     # instance variable/property

#     def details(self):                   # instance method
#         print("Name:", self.name, "Id:", self.id)


# s1 = Student("Bob,", 11)
# s2 = Student("Carol,", 22)
# s1.id = 30
# s2.id = 40

# s1.details()
# s2.details()


# print(s1)
# print(s2)




# =============================Practice========================


# class House:
#     def __init__(self):          #init method
#         self.window = 4          #instance variable
#         self.door = 2            #instance variable

#     def view(self):              #instance method
#         print( self.window,"Windows" ,self.door,"Doors" )

# h1 = House()
# h2 = House()
# h1.window = 6
# h2.door = 3
# h1.view()
# h2.view()



# =============================Practice========================

class Car:
    def __init__(self,name,model, color):
        self.name = name
        self.model_year = model
        self.color = color
        self.wheel = 4
        
    def view(self):
        print("This model year car is",self.name, "and models",self.model_year )
        print("It is a",self.wheel,"wheel car" , "and color is",self.color)

print() 
c1 = Car("Corola","Cl24","Blue")
c2 = Car("NOYA","NY24","Black")

c1.wheel = 6
c2.wheel = 8

c1.view()
print()
c2.view()