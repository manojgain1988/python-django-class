# ========  Mapping / Dictonary Data Types ===========
# 4. Mapping Type   : dict . syntsx= = { "Key " : "Value "}
# spacial  charecter: No Index-number.
# Example for Mapping/Dictonary Data types:

# Full_name = {
#     "name": "Manoj Gain",
#     "phone": '01911715356',
#     "email": "manojgain@gmail.com",
#     "age": 33,
#     "address": "Muksudpur,Gopalganj"
# }
# print()
# print(Full_name)
# print(Full_name.items)
# print(Full_name["address"])
# print(Full_name["name"], Full_name["age"])

# new element add:
# Full_name["height"] = 5.3
# print(Full_name["height"])



# Operation :-ordered, mutable, duplicate Allow
# Methods 11 Types :clear(), copy(), fromkeys() ,get(), items(), keys(), values(), pop(), popitem(), update(), setdefault()

# 1. copy Method:
# x=Full_name.copy()
# print(x)

# 2. clear Method:
# Full_name.clear()
# print(Full_name)

# 3.fromkeys Method: 
# tuple_name = ("name ", "mobile","age","address")
# value= "Manoj Gain"
# x= dict.fromkeys(tuple_name, value)
# print(x)
# print(x['name'])
# print(x['name'][0])
# print(x['name'][1])

#  or
# tuple_name = ("name ", "mobile","age","address")
# value= ["Manoj Gain",35]
# x= dict.fromkeys(tuple_name,value)
# print(x)

# 4. Get Method:
# print(Full_name.get("name"))

# 5. items Method :
# x=Full_name.items()
# print(x)

#   or
# for x,y in Full_name.items():
#     print()
#     print(x,'=',y)

# 6. keys Method :
# x=Full_name.keys()
# print(x)

#   or
# for x in Full_name.keys():
#     print(x)

# 7. values Method :
# x=Full_name.values()
# print(x)
#   or
# for x in Full_name.values():
#     print(x)

# 8. pop Method :
# Full_name.pop("address")
# print(Full_name)

# 9. popitem Method :
# Full_name.popitem()
# print(Full_name)

# 10. setdefault Method :
# x = Full_name.setdefault("fathers", "Ranjit Gain")
# print(x)

# 11. Update Method :
# Full_name.update({"Height": "5.3 inch"})
# print(Full_name)


# ================Range Data Type===================

# range (start value , end value , range object)
# range default value 0 , default 01 increement.add()
#
# for x in range(0,101 ,2):
#     print(x)


# ================ For loop ===================

# For loop stap by stap:
# Brothers = ["Ramen Gain","Ranu Gain","Manoj Gain","Sanjoy Gain"]
# Brothers = ["Ranu Gain","Manoj Gain","Sanjoy Gain"]
# Brothers = ["Manoj Gain","Sanjoy Gain"]
# Brothers = ["Sanjoy Gain"]

# for x in Brothers:
#     print(x)

#   or
 

# ================ while loop===================


# while loop stap by stap:
# var=0
# while var < len (Brothers):
#     print(var)
#     print(Brothers[var])
#     var += 1





