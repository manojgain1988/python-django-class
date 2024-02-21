# what is class ?
# Answer: class halo boject ba kono kichur design ba blue print. class akti object ar acharon nirhdron kore.     abong oi design kora class ar object kemon hobe ba  kemon achoron hobe ta nirdhoron kore.

class Student:
    def __init__(self,name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email
        school_name = 'BM heigh School'
        school_address = 'Baikuntha pur, Kotali para, Gopalgang'

    def stu_info(self):
        print()
        print('Student information:')
        print(f'My name is {self.name}\nI am {self.age} your old\nMy number is {self.number}\nMy email number is {self.email}')


    def Student_parent_info(self, father ,age, fnumber, femail):
        self.father = father
        self.age = age
        self.fnumber = fnumber
        self.femail = femail

        print()
        print('Student Parents Information')
        print(f'\nMy father name is {self.father}\nMy father is {self.age} your old.\nMy father number is {self.fnumber}\nMy father email number is {self.femail}')


class details(Student):
    def super(self, name, age, number, email):
        def __init__(self):
            pass
            
            

    def stu_details(self ,address):
      self.address = address
      print(f'\nStudent Name is :{self.name}\nStudent Age: {self.age} your old.\nStudent number is :{self.number}\nStudent email number is: {self.email}\nMy father name is {self.father}\nMy father is {self.age} your old.\nMy father number is {self.fnumber}\nMy father email number is {self.femail}')
            


Mahin = Student('Manoj Gain','33','01911715356','manoj@gmail.com')
# s2 = Student('Bithi Gain','23','01911715356','manoj@gmail.com')
Mahin.stu_info()
# s2.student_details()

Mahin.Student_parent_info('Ranjit Gain','65','01911715355','ranjitgain@gmail.com')

details('Mahin','23','01703616686','bithi@gmail.com')
details.stu_details(Mahin,'Dhaka Bangladesh')
