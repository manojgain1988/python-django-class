
# def countnumber():
#     for x in range(1,101):
#         print(x)
        
# countnumber()


# List_value = []
# def viewitem():
#     if len(List_value) == 0:
#         print("\t\tList Item is Empty 0!\n")
#     else:
#         for key , item in enumerate(List_value):
#             print(f"\t\t{key} - {item}")
#         print()

# def addnewitem():
#     print("\tWelcome the add new item list block")
#     print("\t02. Show the Item List Block")
#     print("\t01. Add new Item")
#     print("\t00. Back the main programme")
    
    
#     while True:
#         choice = int(input("\tEnter the Option Number: "))
#         if choice == 1 or choice =="01" or choice == "1":            
#             newitem = input("\t\tEnter the new item list: ")
#             List_value.append(newitem)        
#         elif choice == 2 or choice == "02" or choice == "2":
#             for key , item in enumerate(List_value):   
#                 print(f"\t\t{key} - {item}")
#         elif choice == 0 or choice == "0" or choice == "0":
#             break
    
    
# while True:
#     print("==========List programming=============")
#     print("\t00. Close the main Programme")
#     print("\t01. Show the Item List Block")
#     print("\t02. Append the new Item")
#     print()

#     try:    
#         choice = int(input("\tEnter the Option Number: "))
#         if choice == 1 or choice =="01" or choice == "1":
#             viewitem()     
#         elif choice == 2 or choice == "02" or choice == "2":
#             addnewitem()       
#         elif choice == 0 or choice == "00" or choice == "0":
#             pass          
#         else:
#             print("programme is not properly work")
        
#     except:
#         print("\tYour Input is string value !!")
        
        
        
        
        
        
# try:
#     print(x)
# except:
#     print("An Exception Occourred")




# try:
#     print("Hello Manoj Gain")
# except:
#     print("Something went Wrong")
# else:
#     print("Nothing went Wrong")



# try:
#     print("Hello Manoj Gain")
# except:
#     print("Something went Wrong")
# finally:
#     print("The 'try except' is finished")