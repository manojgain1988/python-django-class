
# ===============Python function===========#

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

  #OR
  
  
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


#required possitional function
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
     
# informations(name = "Manoj Gain", number="01911715356",  email="manoj@gmail.com" )




#  length arguments:
# def informations(*name):
#     for x in name:
#         print(x)
# informations("Manoj Gain", "Bithi",  "Juthi" )




# def my_function(child3, child2, child1):
#   print("The youngest child is " + child3)
# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")



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
  