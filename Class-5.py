
# ========  Set Data Types ===========

# 5. Set Types  : set, frozenset.

# syntsx= = {"value"}
# Opratation : Unordered , Immutable/unchangable ,Duplication not Allow

# Method 17 Types:
# add(), clear(), copy(), difference(), difference_update(), discard(), intersection(), intersection_update(), isdisjoint(), issubset(), issuperset(), pop(), remove(), symmetric_difference(), symmetric_difference_update(), union(), update()

# mySet= {"mango","babana", "orange","apple"}
# print()
# print(mySet)

# # Or
# for x in mySet:
#   print(x)


# Method 17 Types:
# add(), clear(), copy(), difference(), difference_update(), discard(), intersection(), intersection_update(), isdisjoint(), issubset(), issuperset(), pop(), remove(), symmetric_difference(), symmetric_difference_update(), union(), update()

# mySet= {"mango","babana", "orange","apple"}


# 01. add()
# mySet= {"mango","babana", "orange","apple"}
# mySet.add("painapple")
# print()
# print(mySet)


# 02. clear()
# mySet= {"mango","babana", "orange","apple"}
# mySet.clear()
# print()
# print(mySet)


# 03. copy()
# mySet= {"mango","babana", "orange","apple"}
# fruits = mySet.copy()
# print()
# print (fruits)

#  or
# x=mySet.copy()
# print()
# print(x)


# 04. difference()
# fruits= {"mango","babana", "orange","apple"}
# fish = {"kai","orange", "apple"}
# my_result=fruits.difference(fish)
# print()
# print(my_result)
# Note :fruits - fish


# 05. difference_update()
# fruits= {"mango","babana", "orange","apple"}
# fish = {"kai","orange", "apple"}
# fruits.difference_update(fish)
# print()
# print(fruits)
# #Note :fruits - fish


# 06. discard()
# fruts= {"mango","babana", "orange","apple"}
# fruts.discard("babana")
# print()
# print(fruts)


# 07. intersection()
# fruts= {"mango","babana", "orange","apple"}
# fish = {"kai","orange", "apple"}
# my_result = fruts.intersection(fish)
# print()
# print(my_result)


# 08. intersection_update()
# fruts= {"mango","babana", "orange","apple"}
# fish = {"kai","orange", "apple"}
# fruts.intersection_update(fish)
# print()
# print(fruts)


# 09. isdisjoint()
# fruts= {"mango","babana", "orange","apple"}
# fish = {"kai","shing", "illish"}
# my_result=fruts.isdisjoint(fish)
# print()
# print(my_result)


# 10. issubset()
# fruts= {"mango","babana", "orange","apple"}
# fish = {"kai","shing", "apple"}
# my_result=fruts.issubset(fish)
# print()
# print(my_result)


# 11. issuperset()
# fruts= {"mango","babana", "orange","apple"}
# fish = {"kai","shing", "apple"}
# my_result=fruts.issuperset(fish)
# print()
# print(my_result)


# 12. pop()
# fruts= {"mango","babana", "orange","apple"}
# fruts.pop()
# print()
# print(fruts)


# 13. remove()
# fruts= {"mango","babana", "orange","apple"}
# fruts.remove("babana")
# print()
# print(fruts)


# 14. symmetric_difference()
# Note  fruits + fish
# fruits= {"mango","babana", "orange","apple"}
# fish = {"kai","shing", "apple"}
# x=fruits.symmetric_difference(fish)
# print()
# print(x)


# 15. symmetric_difference_update()
# fruts= {"mango","babana", "orange","apple"}
# fish = {"kai","shing", "apple"}
# fruts.symmetric_difference_update(fish)
# print()
# print(fruts)


# 16. union()
# fruits= {"mango","babana", "orange","apple"}
# fish = {"kai","shing", "apple"}
# x=fruits.union(fish)
# print()
# print(x)


# 17. update()
# fruts= {"mango","babana", "orange","apple"}
# fish = {"kai","shing", "apple"}
# fruts.update(fish)
# print()
# print(fruts)




#========= Boolean data Type ==========#

# x = 15
# y = 15

# print(x > y)
    
# if  x > y:
#     print('X is grater than Y')

# elif x < y:
#     print('Y is grater than X')
    
# else:
#     print('X is Same value Y')