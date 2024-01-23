
# ===============Python function===========

# Function 2 types
# 1.Built in Function
# 2. User define Function


# 1.Built in Function
# for x in range(1,21):
#     print(f"{x}. Manoj Gain")


# var = 0
# while var <21:
#     print(f"{var}. Manoj Gain")
#     var +=1
# print()

# print(),len(),range(),enumerate()


# 2. User define Function

# def informations(name,number,email):
#     print(f"your name is: {name}")
#     print(f"your number is: {number}")
#     print(f"your email is: {email}")

# informations("Manoj Gain","01911715356","manojgain@gmail.com")

# OR


# def informations(name,number,email):
#     print(f"your name is: {name}")
#     print(f"your number is: {number}")
#     print(f"your email is: {email}")
#     print()


# while True:
#     name = str(input("Enter your name :"))
#     number = str(input("Enter your number :"))
#     email = str(input("Enter your email :"))
#     informations(name,number,email)
#     print()


# default arguments:

# def informations(name="Manoj Gain", number="01911715356",email="manoj@gmail.com"):
#     print()
#     print(f"Your Name is: {name}")
#     print(f"Your Number is: {number}")
#     print(f"Your Email is: {email}")

# informations()


#  possitional arguments
# def informations(name, number,email="manoj@gmail.com"):
#     print()
#     print(f"Your Name is: {name}")
#     print(f"Your Number is: {number}")
#     print(f"Your Email is: {email}")

# informations("Manoj Gain", "01911715356", )


#  keyword arguments:
# def informations(name, number,email):
#     print()
#     print(f"Your Name is: {name}")
#     print(f"Your Number is: {number}")
#     print(f"Your Email is: {email}")

# informations(name = "Manoj Gain", number="01911715356",  email="manoj@gmail.com")



#====================================
#  length arguments:
# def informations(*name):
#     for x in name:
#         print(x)
# informations("Manoj Gain", "Bithi",  "Juthi" )

            #======OR==========
            
# def add(a,*b):
#     print(a)
#     print(b)
#     c=a 
#     for x in b:
#         c=c+x
#     print(c)
        
# add(5,10,15,20)


            #======OR==========

# def my_function(child3, child2, child1):
#   print("The youngest child is " + child3)
# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


#====================================
# def my_function(*kids):
#     print("The youngest child is " + kids[2])
# my_function("Emil", "Tobias", "Linus")


# #  keywords length arguments:
# def informations(**name):
#     for x in name:
#         print(x)
# informations("Manoj", "Gain", "Bithi",  "Juthi" )


# def my_function(**kid):
#     print("His last name is " + kid["lname"])
# my_function(fname = "Tobias", lname = "Refsnes")


# def largest():
#     x=120
#     y=100

#     if x > y:
#         print(f"largest number is {x}")
#     else:
#         print(f"lower number is {y}")
# largest()


# x=1200
# def largest():
#     global x            #global variable
#     y=100               #local variable

#     if x > y:
#         print(f"largest number is {x}")
#     else:
#         print(f"lower number is {y}")


#     def sumation():
#         print(x+y)
#     sumation()

# largest()


# x=int(input("enter your number :"))
# def largest():
#     global x                                  #global variable
#     y=int(input("enter your number :"))       #local variable

#     if x > y:
#         print(f"largest number is {x}")
#     else:
#         print(f"lower number is {y}")

#     def sumation():
#         print(x+y)
#     sumation()
# largest()


# ১. ফাংশন  ব্যবহার করে আয়ত ক্ষেত্রফল বাহির কর ।
# ২. ফাংশন  ব্যবহার করে মৌলিক নাম্বার বের কর ।
# ৩. ফাংশন  ব্যবহার করে ফেকটোরিয়াল নাম্বার ব্যবহার কর ।
# ৪. ফাংশন  ব্যবহার করে   তিনটি সংখ্যার বড় সংখ্যা বের কর ।


# একটি ফাংশন যা আযাত বের করে
# def calculate_area(length, width):
#     area = length * width
#     return area

#  ফাংশনটি কল করা
# length = float(input("দৈর্ঘ্য দয়া করে প্রদান করুন: "))
# width = float(input("প্রস্থ দয়া করে প্রদান করুন: "))

# result = calculate_area(length, width)
# print("আয়তের ক্ষেত্রফল:", result)

# OR

# def area(length,width):
#   area =length*width
#   return area

# length = float(input("Enter your length :"))
# width = float(input("Enter your width :"))

# result = area(length,width)


# print(f"Total Area: ", result)


# def is_prime(num):
#     if num > 1:
#         for i in range(2, int(num**0.5) + 1):
#             if (num % i) == 0:
#                 return False
#         else:
#             return True
#     else:
#         return False

# def find_prime_numbers(limit):
#     primes = [num for num in range(2, limit + 1) if is_prime(num)]
#     return primes

# # এখন আমরা এই ফাংশন ব্যবহার করে মৌলিক নাম্বার বের করতে পারি
# limit = 20  # আপনি চাইলে এই সীমা পরিবর্তন করতে পারেন
# prime_numbers = find_prime_numbers(limit)

# print("মৌলিক নাম্বারগুলি হলো:", prime_numbers)


# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# # ফ্যাক্টোরিয়াল বের করতে ফাংশনটি ব্যবহার করুন
# num = 5  # আপনি চাইলে এই সংখ্যাটি পরিবর্তন করতে পারেন
# result = factorial(num)

# print(f"{num} এর ফ্যাক্টোরিয়াল হলো: {result}")


# def find_largest_number(a, b, c):
#     largest = max(a, b, c)
#     return largest

# # তিনটি সংখ্যা
# num1 = 25
# num2 = 42
# num3 = 18

# # ফাংশনটি ব্যবহার করে বড় সংখ্যা বের করুন
# result = find_largest_number(num1, num2, num3)

# print(f"তিনটি সংখ্যার মধ্যে সবচেয়ে বড় সংখ্যা হলো: {result}")

# OR

# def largest_number(x,y,z):
#   largest = max(x,y,z)
#   return largest

# num1 = 50
# num2 = 80
# num3 = 100

# result = largest_number(num1,num2,num3)
# print(f"largest Number :" ,result)





# ========== function & class practice=================


# Example 01:
# def hello():
#   print("Hello !  My Name is Manoj Gain.")

# hello()


# Example 02:
# def add(x,y):
#   z = x+y
#   print(z)

# add(10 ,5)

         #====================

# Example 03:
# def add (x ,y):
#   z  = x+y
#   return z

# sun = add(10,20)
# print(sun)


  #====================

# Example 04:
# def add (x ,y):
#   z  = x+y
#   a = x-y
#   return z,a

# sum,sub = add(10 ,5)
# print()
# print("Value is sum:-", sum)
# print("Value is sum:-", sub)



# ==============lambda/Anonymous function==============
# def add(a):
#   return a+10

# sum = add(12)
# print(sum)


            #==========or===========
# g = lambda a:a+10
# sum =g(12)
# print(sum)


            #==========or===========
# g = lambda a:a*a

# print(g(12))

# ================or===============

# g = lambda a,b,c,d : a*b*c+d
# print(g(10,15,2,10))


# =============filter, map ,reduce, function============

# lst = [1,2,3,4,5,6,7,8,9,10]
# new_lst = []
# for i in lst:
#   if i % 2 ==1:
#     print(i)
#     new_lst.append(i)
# print()
# print(new_lst)


# =============filter function============
# lst = [1,2,3,4,5,6,7,8,9,10]

# # g = lambda x:(x % 2)==1
# new_lst =list(filter(lambda x:(x % 2)==1,lst))
# print(new_lst)


# =======OR============

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(list(filter(lambda x: (x % 2) == 1, lst)))

# =======OR============

# print(list(filter(lambda x: (x % 2) == 1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))





# =============Map function============

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # g = lambda x: x*x
# print(list(map(lambda x: x*x, lst)))

    #===========OR==================
    
# #lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # g = lambda x: x*x
# print(list(map(lambda x: x*x, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))




# =============Reduce function============

# from functools import reduce
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# sum = reduce(lambda x,y : x+y, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print()
# print(sum)


# ===========class  Practice=============

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





# ===========if function===================
# a = 5
# b =5
# c = 5
# if a > 10:
#     print("A is Greater then 10")
# elif b > 10:
#     print("B is Greater then 10 ")
# elif c > 10:
#     print("C is Greater then 10 ")
# else:
#     print("a, b and c are less then 10")


# ===========if,else / Nastet if  function===================
# a = 15
# b = 5

# if a > 10:
#     print("A is Greater then 10")

#     if b > 10:
#         print("B is Greater then 10 ")
#     else:
#         print("B is less then 10")

# else:
#     print("a less then 10")


# ======swap first & last element/index  in list of python

# my_list = [1,2,3,4,5]
# print(my_list)

# def swaplist(my_list):
#     my_list[0],my_list[-1] = my_list[-1],my_list[0]
#     return my_list


# swaplist(my_list)
# print(my_list)


# ===========Math function==========================


# import math
# x = math.sqrt(25)
# print(x)

# ====================
# import math
# x = math.pow(5,5)
# print(x)


# ====================
# import math
# x = math.pow(5,5)
# print(x)


# ===========Input function==========================

# first_num = int(input("Enter your first  Number: "))
# last_num = int(input("Enter your lsat Number: "))
# print("Total Sum:-" ,first_num+last_num)


# ===========Eval function==========================

# sum = eval(input(" Enter Your an Expression :"))
# print(sum)


# ====================while  loop======================
# i = 1
# while i <= 4:
#     print("Outside i is :", i)
#     j = 1
#     while j <= 4:
#         print("Inside j is:",j)
#         j+=1

#     print()
#     i += 1


# ================For loop==================

# for i in range(1, 101, 2):
#     print(i)

# ========OR==========

# for i in range(1, 21):
#     if i % 5 ==0:
#         continue
#     print(i)


#             #  ========OR==========

# print()
# for i in range(1, 11):
#     if i % 5 ==0:
#         break
#     print(i)

# ========OR==========

# for y in range(5):
#     for i in range(5):
#         print("*" , end="")
#     print()

# ========OR==========

# for y in range(10):
#     for i in range(y):
#         print("*" , end=" ")
#     print()

# ========OR==========

# for y in range(8):
#     for i in range(y+1):
#         print("*-", end="  ")
#     print()

    # ========OR==========

# for y in range(8):
#     for i in range(8-y):
#         print("*-*", end="  ")
#     print()

    # ========Pyramid==========


# def print_pyramid(height):
#     for i in range(1, height + 1):
#         spaces = " " * (height - i)
#         stars = "*" * (2 * i - 1)
#         print(spaces + stars)

# print_pyramid(10)

    # ========OR==========

# for i in range(100, 0, -2):
#     print(i)

    # ========OR==========

# my_list = [1,2,3,4,5,6,7,8,9,10]
# for i in my_list:
#     print(i)

    # ========OR==========

# my_list = "My Name is Manoj Gain"
# for i in my_list:
#     print(i)

    # ===============OR==================

# x = 1
# while x <= 5:
#     print("Outside x is :", x)

#     y = 1
#     while y <= 5:
#         print("Inside Y is :", y)
#         y +=1
#     print()

#     x +=1
