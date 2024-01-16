
# ========== 7 Types  of Operator In Python===========

# 01. Arithmetic operators  - 7 types
# 02. Assignment operators - 13 types
# 03. Comparison operators  - 6 types
# 04. Logical operators  - 3 types
# 05. Identity operators  - 2 types
# 06. Membership operators  - 2 types
# 07. Bitwise operators  - 6 types


# 01. Arithmetic operators  - 7 types
#       + , - , * , / , % , ** ,  //

# 01 .  +	Addition	 x + y
# 02 . -	Subtraction	 x - y
# 03 . *	Multiplication 	x * y
# 04 . /	Division	 x / y
# 05 . %	Modulus 	x % y
# 06 . **	Exponentiation	 x ** y
# 07 . //	Floor division 	x // y


# Example of Arithmetic Operator:

# 01.   +	Addition	 x + y
# x = 10
# y = 8
# print(x+y)

# 02.  -	Subtraction	 x - y
# x = 10
# y = 8
# print(x-y)

# 03.  *	Multiplication 	x * y
# x = 10
# y = 8
# print(x * y)

# 04.  /	Division	 x / y
# x = 10
# y = 8
# print(x / y)

# 05.  %	Modulus 	x % y
# x = 10
# y = 8
# print(x % y)

# 06.  **	Exponentiation	 x ** y
# x = 10
# y = 8
# print(x * y)

# 07.  //	Floor division 	x // y
# x = 20
# y = 8
# print(x // y)


# 02. Assignment operators  13 Types
# Operator   Example	  Same As
#  =	     x = 5	     x = 5
#  +=	     x += 3	     x = x + 3
#  -=	     x -= 3	     x = x - 3
#  *=	     x *= 3	     x = x * 3
#  /=	     x /= 3	     x = x / 3
#  %=	     x %= 3  	 x = x % 3
#  //=	     x //= 3 	 x = x // 3
#  **=	     x **= 3 	 x = x ** 3
#  &=	     x &= 3  	 x = x & 3
#  |=	     x |= 3	     x = x | 3
#  ^=	     x ^= 3	     x = x ^ 3
#  >>=	     x >>= 3     x = x >> 3
#  <<=	     x <<= 3 	 x = x << 3


# Example of Assignment Operator:
# =	     x = 5	     x = 5
# x = 5
# print()
# print(x)


#  +=	     x += 3	     x = x + 3
# x = 15
# y = 10
# x +=y
# print(x)

#  -=	     x -= 3	     x = x - 3
# x = 15
# y = 10
# x -=y
# print(x)


#  *=	     x *= 3	     x = x * 3
# x = 15
# y = 10
# x *=y
# print(x)

#  /=	     x /= 3	     x = x / 3
# x = 15
# y = 10
# x /=y
# print(x)


#  %=	     x %= 3  	 x = x % 3
# x = 15
# y = 10
# x %=y
# print(x)


#  //=	     x //= 3 	 x = x // 3
# x = 15
# y = 10
# x //=y
# print(x)


#  **=	     x **= 3 	 x = x ** 3
# x = 15
# y = 10
# x **=y
# print(x)


#  &=	     x &= 3  	 x = x & 3
# x = 15
# y = 10
# x &=y
# print(x)

#  |=	     x |= 3	     x = x | 3
# x = 15
# y = 10
# x |=y
# print(x)


#  ^=	     x ^= 3	     x = x ^ 3
# x = 15
# y = 10
# x ^=y
# print(x)


#  >>=	     x >>= 3     x = x >> 3
# x = 15
# y = 10
# x >>=y
# print(x)

#  <<=	     x <<= 3 	 x = x << 3
# x = 15
# y = 10
# x >>=y
# print(x)


# 03. Comparison/Relational operators -6 Types
# Operator	    Name	                            Example
# ==	        Equal	                            x == y
# !=	        Not equal	                        x != y
# >	            Greater than            	        x > y
# <	            Less than	                        x < y
# >=	        Greater than or equal to	        x >= y
# <=	        Less than or equal to	            x <= y


# Example of Comparison/Relational Operator:

# ==	        Equal	                            x == y
# x = 10
# y = 10
# print()
# print(x ==y)


# !=	        Not equal	                        x != y
# x = 10
# y = 9
# print()
# print(x !=y)

#  or

# x = 10
# y = 10
# print()
# print(x !=y)


# >	            Greater than            	        x > y
# x = 10
# y = 9
# print()
# print(x > y)

#   or

# x = 10
# y = 12
# print()
# print(x > y)


# <	            Less than	                        x < y
# x = 10
# y = 9
# print()
# print(x < y)

#OR

# x = 10
# y = 12
# print()
# print(x < y)


# >=	        Greater than or equal to	        x >= y
# x = 12
# y = 10
# print()
# print(x >= y)


# <=	        Less than or equal to	            x <= y
# x = 8
# y = 10
# print()
# print(x <= y)


# Example of control structure :

# user_input  = int(input("Enter Your Number : "))
# if user_input == 33:
#     print("Exam pass")

# elif user_input > 40:
#     print("Exam GPA C")

# elif user_input < 33:
#     print("Exam fail")

# else:
#     print("-------")


# 04. Logical operators - 3 Types:

# Operator	                  Description	                                Example
# and 	      Returns True if both statements are true	                    x < 5 and  x < 10
# or	      Returns True if one of the statements is true	                x < 5 or x < 4
# not	      Reverse the result, returns False if the result is true not  (x < 5 and x < 10)


# and 	      Returns True if both statements are true	                    x < 5 and  x < 10

# x = 100
# y = 200
# if x == 100 and y == 220:
#      print("x and y sumation:",x + y)
# else:
#     print("x and y Not Sumation")


# or	      Returns True if one of the statements is true	                x < 5 or x < 4
# x = 1000
# y = 250
# if x == 100 or y == 250:
#     print("x and y sumation:",x + y)
# else:
#     print("Not Sumation x")

# not	      Reverse the result, returns False if the result is true not  (x < 5 and x < 10)
# x = 100
# y = 200
# if x not 100:
#     print("x and y sumation:",)
# else:
#     print("Not Sumation")


# 05. Identity operators   -2 Types:
# Operator	      Description	                                              Example
# is 	        Returns True if both variables are the same object	           x is y
# x = ["apple", "banana"]
# y = ["apple", "banana"]
# z = x

# print(x is z)

# is not	    Returns True if both variables are not the same object         x is not y
# x = ["apple", "banana"]
# y = ["apple", "banana"]
# z = x

# print(x is y)

# print(x == y)


# 06. Membership operators  -2 Types:

# Operator	                             Description	                                  Example
# in 	            Returns True if a sequence with the specified
#                   value is present in the object	                                      x in y

# list  = [10,12,13,14,15,]
# if 12 in list:
#     print("12 has found in list.")
# else:
#     print("Not found in list.")


# not in	        Returns True if a sequence with the specified
#                   value is not present in the object	                                 x not in y

# list2  = [10,12,13,14,15,]
# if 16 in list2:
#     print("16 has found in list.")
# else:
#     print("Not found in list.")


# 07. Bitwise operators  -6 Types:
# Operator	      Name	                       Description	                                         Example
# & 	          AND	            Sets each bit to 1 if both bits are 1	                       x & y
# |	              OR	            Sets each bit to 1 if one of two bits is 1	                   x | y
# ^	              XOR	            Sets each bit to 1 if only one of two bits is 1	               x ^ y
# ~	              NOT	            Inverts all the bits	                                        ~x
# <<	   Zero fill left shift	    Shift left by pushing zeros in from the right and
#                                   let the leftmost bits fall off	                               x << 2
# >>	   Signed right shift	    Shift right by pushing copies of the leftmost bit
#                                   in from the left, and let the rightmost bits fall off	       x >> 2





# Happy New year:
# day = "31"
# month = "12"
# year = "2023"
# years = 2024
# biday_year =day+"-" + month+"-"+year
# print()
# print("Biday Year:", biday_year)
# print()
# print("Happy New Year:", years)

# name = "Manoj"
# name1 = "Gain"
# full_name  = (name+" "+name1)
# print("My full Name:" ,full_name)





