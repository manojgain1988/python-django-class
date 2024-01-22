
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

# class Car:
#     def __init__(self,name,model, color):
#         self.name = name
#         self.model_year = model
#         self.color = color
#         self.wheel = 4

#     def view(self):
#         print("This model year car is",self.name, "and models",self.model_year )
#         print("It is a",self.wheel,"wheel car" , "and color is",self.color)

# print()
# c1 = Car("Corola","Cl24","Blue")        # Object
# c2 = Car("NOYA","NY24","Black")         # Object

# c1.wheel = 6
# c2.wheel = 8

# c1.view()
# print()
# c2.view()


# =============================Practice========================

# class Book:

#     def __init__(self, name, author):
#         self.name = name
#         self.author = author
#         self.price = 400

#     def set_price(self, price):
#         self.price = price

#     def get_price(self):
#         return self.price

#     def details(self):
#         print("Book Name :", self.name,
#               "\nAuthor:", self.author,
#               "\nPrice:", self.price, "Taka")


# b1 = Book("Talk True", "Manoj Gain.", )         # Object
# b2 = Book("Not Be Layer", "Manoj Gain.", )      # Object

# print()
# b1.set_price(350)
# b1.details()

# print()
# b2.set_price(330)
# b2.details()


# ============Singal===Inheritance======================
# class Animal:

#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print(self.name, "is eating")


# class Dog(Animal):

#     def bark(self):
#         print(self.name, "is barking")


# a1 = Animal("jack")
# d1 = Dog("Rover")
# a1.eat()
# d1.eat()
# d1.bark()


# #isinstance(object,ClassName)
# print(isinstance(a1,Animal))
# #issubclass(Class , ClassName)
# print(issubclass(Dog, Animal))


# ==========Hierarchical===Inheritance=======================
# class Student:
#     def __init__(self,name,Id):
#         self.name = name
#         self.id = Id

#     def details(self):
#         print("Name:",self.name,"ID:",self.id)


# class CSEStudent(Student):
#     def __init__(self,name, Id,labs):
#         super().__init__(name,Id)
#         self.no_of_labs = labs

#     def cry(self):
#         print("CSE student are always crying becouse of they has per day",self.no_of_labs,"labs class")


# class BBAStudent(Student):

#     def party(self):
#         print("Thet are always Party")


# print()
# s1 = CSEStudent("Manoj Gain ,",420,3)
# s2= BBAStudent("Bithi ,",220)

# s1.details()
# s2.details()
# s1.cry()
# s2.party()


# =================Multilevel===Inheritance==================

# class Student:                           #grand parent class
#     def __init__(self,name ,Id):
#         self.name = name
#         self.id = Id

#     def details(self):
#         print("Name:",self.name, "ID:", self.id)


#            #=========================
# class CSEStudent(Student):                #parent class
#     def __init__(self,name,Id,labs):
#         super().__init__(name,Id)
#         self.no_of_labs = labs

#     def cry(self):
#         print(self.name ,"They are always crying they has per day", self.no_of_labs, "labs class")


#         #===========================
# class CSEFresher(CSEStudent):            #child class

#     def enroll_CSE110(self):
#         print(self.name,"Enrolled in CSE100")

#     def party(self):
#         print("They are always Happy")


#       #=============================
# print()
# s1 = CSEStudent("Manoj Gain,", 420, 3)
# s2 = CSEFresher("Bithi,",220, 2)
# s1.details()
# s2.details()
# s1.cry()
# s2.party()
# # s1.enroll_CSE110()
# s2.enroll_CSE110()


# =================Multiple===Inheritance==================

# class A:
#     def __init__(self):
#         print("__init__of class A")

#     def method1(self):
#         print("Method1 od class A")

#     #================================
# class B:
#     def __init__(self):
#         print("__init__of class B")

#     def method1(self):
#         print("Method1 od class B")

#     #================================
# class C(A,B):
#     def __init__(self):
#         print("__init__of class C")

#     def method2(self):
#         print("Method2 od class C")

#     #================================


# c1 = C()
# c1.method1()


# =================__str__==================
# class Student:

#     def __init__(self, name, Id):
#         self.name = name
#         self.id = Id
#         # print(self)

#     def __str__(self):
#         return "My name is "+ self.name

# print()
# s1 = Student("Manoj Gain", 33)
# s2 = Student("Bithi Gain", 23)
# print(s1)
# print(s2)


# ================composition has a relation=====================

# class Engine:                        #parent class
#     def __init__(self ,cc):
#         self.capacity = cc

#     def start(self):
#         print("Engine is Started")

#     def stop(self):
#         print("Engine is stopped")

#     #================================
# class Car(Engine):                 #child class
#     def __init__(self, name, cc):
#         self.engine = Engine(cc)
#         self.name = name

#     def run(self):
#         self.engine.start()
#         print("Car is Running")

#     #================================
# print()
# c1 = Car("Toyota", 2500)
# c1.run()







# ===================abstract class & method================

# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass

#     def eat(self):
#         print("I am eatting")

#     # =================================


# class Dog(Animal):
#     def make_sound(self):
#         print("Dog is Barking.")

#     # =================================


# class Cat(Animal):
#     def make_sound(self):
#         print("Cat is Meow Meow.")

#     # =================================


# class Snake(Animal):
#     def make_sound(self):
#         print("Snake is Hiss Hiss.")

#     # =================================


# print()
# d1 = Dog()
# d1.eat()
# d1.make_sound()

# print()
# c1 = Cat()
# c1.eat()
# c1.make_sound()

# print()
# s1 = Snake()
# s1.eat()
# s1.make_sound()
