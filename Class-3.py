
# Welcome to Python Programme Language Tutorial.


# 1.========== list data type ==============
# yntax:
# List_variable = ["Ramen","Rane","Manoj"]

# Operation 3 types: Oradered, Changeable, Duplicate Allow

# Ordered:
# List_variable = ["Ramen","Rane","Manoj"]


# Changeable:
# List_variable = ["Ramen","Rane","Manoj"]
# List_variable[0] = "Sanjoy"
# print(List_variable)


# Duplicate:
# List_variable = ["Ramen","Rane","Manoj","Ranu"]
# print(List_variable)


# Methods 11 types :
# append("value"), clear() ,copy(), count("value") ,extend() ,index("value") ,insert(indexNumber,"value") ,pop() ,remove("value") ,sort(),reverse()


# Entra 3 methods
# min(), max(), len()

# 01. append("value")
# List_variable = ["Ramen","Rane","Manoj"]
# List_variable.append("Sanjoy")
# print(List_variable)

# 02. clear()
# List_variable = ["Ramen","Rane","Manoj"]
# List_variable.clear()
# print(List_variable)


# 03. copy()
# List_variable = ["Ramen","Rane","Manoj"]
# print(List_variable)
# x = List_variable.copy()
# print(x)

# 04. count("value")
# List_variable = ["Ramen","Rane","Manoj","Ramen"]
# x = List_variable.count("Ramen")
# print(x)


# 05. extend()
# Brothers = ["Ramen","Rane","Manoj","Sanjoy"]
# sister = ["Lopa" , "Popy" , "Tuthi"]
# Brothers.extend(sister)
# print(Brothers)


# 06. index("value")
# Brothers = ["Ramen","Rane","Manoj","Sanjoy"]
# x = Brothers.index("Sanjoy")
# print(x)

# 07. insert(indexNumbe , "Value")
# Brothers = ["Ramen","Rane","Manoj","Sanjoy"]
# Brothers.insert(3, "Lopa")
# print(Brothers)


# 08. pop()
# Brothers = ["Ramen","Rane","Manoj","Sanjoy"]
# Brothers.pop()
# print(Brothers)


# 09. remove("value")
# Brothers = ["Ramen","Rane","Manoj","Sanjoy"]
# Brothers.remove("Manoj")
# print(Brothers)


# 10. sort()
# Brothers = ["Ramen","Rane","Manoj","Sanjoy"]
# Brothers.sort()
# print(Brothers)


# 10. reverse()
# Brothers = ["Ramen","Rane","Manoj","Sanjoy"]
# Brothers.reverse()
# print(Brothers)


# list data type concanetae

# x = [1,2,3,4,5]
# y = [6,7,8,9,10]
# full_list = x+y
# print()
# print(full_list)
# print()
# x.extend(y)
# print(x)

# Brothers_list  = ["Ramen", "Ranu", "Manoj", "Sanjoy", "Lopa"]

# print(Brothers_list[0])
# print(Brothers_list[0:6])
# print(Brothers_list[::-1])
# print(Brothers_list[0])

# multidimantion list:
 
  
# multidimantion_list = [[10,20,30,40,50],[60,70,80,90,100],[100,200,300,400,500]]
# print()
# print(multidimantion_list[0][3])
# print()
# print(multidimantion_list[1][3])
# print()
# print(multidimantion_list[2][3])


# 2.========== Tuple data type ==============

# Syntax: ( )
# Brothers = ("Ramen","Rane","Manoj")

# Operation 3 types: Oradered, UnChangeable,     Duplicate allow

# Ordered:
# Brothers = ("Ramen","Rane","Manoj")
# print(Brothers)

# UnChangeable:
# Brothers = ("Ramen","Rane","Manoj")
# Brothers[0] = "Sanjoy"
# print(Brothers)

#  or 

# After convert Tuple to list
# Brothers = ("Ramen","Rane","Manoj")
# print(Brothers)
# New_Brothers = list(Brothers)
# print(New_Brothers)
# New_Brothers[0]="Sanjoy"
# print(New_Brothers)


# Again convert list to Tuple :
# Brothers = ("Ramen","Rane","Manoj")
# New_Brothers = list(Brothers)
# print(New_Brothers)
# Bro = tuple(New_Brothers)
# print(Bro)



# Duplicate allow:
# Brothers = ("Ramen","Rane","Manoj" ,"Ranu","Sanjoy")
# print(Brothers) 


# Methods 2 types :
#  count("value")  ,index("value") 


# 1.  count("value")
# Brothers = ("Ramen","Ranu","Manoj","Ranu")
# print(Brothers. count("Ranu"))
# print()

# 1.  index("value") 
# Brothers = ("Ramen","Ranu","Manoj","Ranu")
# print(Brothers. index("Ranu"))
# print()


# Tuple concanete
# x = (1,2,3,4,5)
# y = (6,7,8,9,10)
# print()
# print(x+y)


# ================Range Data Type===================

# range (start value , end value , range object)
# range default value 0 , default 01 increement.add()
#
# for x in range(0,101 ,2):
#     print(x)




