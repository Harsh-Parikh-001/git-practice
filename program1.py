#format specfier/holder (used in modern times)

print("Enter your name")

#input is always in string

s = input()
 
print("Enter your surname")

p = input()


print("Enter your amount")

a = float(input())

print("Thy name is {0} and thy surname is {1} and the amount you have entered is {2}".format(s,p,a) )

#Important

#==========================
  
#format specifier/holder(used in older time)

# print("Enter thy name")

# s = input()

# print("Enter thy surname")

# p = input()

# print("Enter thy amount")

# a = float(input())

# print("Thy name is %s and thy surname is %p and the amount you have entered is %f" %(s,p,a) )


# #=====================

# # format of output

# print("Enter a two digit number")

# i = int(input())

# print("{:05d}" .format(i))

# #========================

# s = "I love python"

# print("HATE" in s)

 
# s = "I love python"

# print("love" in s)              #case sensitive
 

# #=============================

# # String slicing

# print("Hey " * 5)
# # Function Overloading

# s = "I will learn python and machine learning"

# print(s)
# print(s[4:11])
# print(s[:12])
# print(s[5])
# print(s[4:])


# #===============================

# #list

# list1 = ['English', 'Maths', 'Physics', 'Maths', 'Chemistry',  'Maths']

# print(list1)
# print("\n")
# a = list1.count('Maths')
# print("count = ",a)
# list1.pop()
# print(list1)
# del list1[0]
# print(list1)
# list1.append('Biology')  
# print(list1)
# list1.reverse()
# print(list1)

# list1.sort()            #Important
# print(list1)

# #==============================

# #tuple
 
# tup1 = ('English', 'Maths', 'Physics', 'Chemistry', 1500, 2485, 6545, 1256)

# #we can not change the content in a tuple

# print(tup1)
# print("Value at index 2:")
# print(tup1[2])
# print(tup1[2:7])
# tup2 = ('Biology', 'Marathi')
     
# #Concatenate
 
# tup3 = tup1 + tup2                
# #Tuple 1 is not changed the concatenated tuple is stored in a new tuple tup3

# print(tup3)

# #=============================

# # Dictionary

# d = {1 : "Dhavan", 2 : "Rohit", 3 : "Virat", 4 :"Rahul", 5 :"Dhoni", 
#      6 :"Hardik", 7 :"Bhuvi", 8 :"Jadeja", 9 :"Bhumra",10 :"Shami",11 :"Kuldeep"}

# #It is a type of data type which is associated with a rank/number
# #The number need not be in a specific order

# print(d)
# print("\n")
# print(d[3],d[2])

# #========================

# # Change a number to hexa ahnd octal

# print("Enter any numbers")

# n = int(input())

# print("Hexadecimal value = ",hex(n))
# print("octal decimal value = ",oct(n))

# #In python most of the function has a pre written class

# #================================

# # Find the area of circle

# print("Enter the radius")

# r = float(input())

# area = (22/7) * r * r

# print("Area = ",area)
