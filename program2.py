
list2 = ['a', 'b', 'c']
 
print(list2)

tou1 = (1,2,3,4)

con = list2 +  (list)(tou1)

print(con)

#====================================

# print("Enter the number")

# a = float(input())

# print("Enter the number")

# b = float(input())


# if a > b:
#     print("Largest value is" , a)
        
#     print("This is under if")

# #In python there no concept of brace bracket 
# #The way control structure and nested control structure work is via indentation 
 
# else:
#     print("Largest value is ", b)
#     print("This is under else")    
    
# #===========================

# print("Enter the age")

# a = int(input())

# if a < 2:
#     print("NO ticket is needed")
    
# elif 2 <= a < 13:
#     print("Child fare")
    
# else :
#     print("Adult fare")
    
# #============================    

# #IMPORTANT
# #The for loop is the most used control struture in the loops


# #The numbers in the for bracket is the initialization, final number(n-1) , increment/decrement  
# for i in range(1,16,+3) :
#     print(i) 

# print("===================")

# #Here the initial number is taken as zero and increment is done as +1
# for i in range(6) :
#     print(i)

# print("==================")

# p = [2,5,6,4,222]

# for i in range(5) :
#     print(p[i])         #Same as array  name_of_array[index number]
    
# print("===================")

# #Prints all the number in that data type[list,tuple,dictionary]
# for i in p :
#     print(i)

# print("====================")


# s = "SAMPLE STRING"

# v = ['A','E','I','O','U']

# #IMPORTANT
# #usage of the keyword 'in'

# for i in s:
#     if i in v:
#         print(i)

# print("========================")


# for i in range(6,1,-1) :
#     print(i)

# #============================================


# # To print the tables of any given number

# print("Enter the value")

# a = (int)(input())


# for i in range (1,11):
    
#     d = a * i
    
#     print("{0} * {1} = {2}".format(a,i,d))
    
# #===================================

# # to find the sum of the sequence of 1 upon the denominator square of natural numbers
    
    
# print("Enter the value")

# n = int(input())

# sum = 0

# for i in range (1,n+1):

#     d = 1 /(i*i)
    
#     sum = sum + d
    
   
# print(sum)    
    
# #============================================

# # working of for loop in a dictionary

# d = {231 : "Dhavan", 233 : "Rohit", 322 : "Virat", 422 :"Rahul", 52323 :"Dhoni", 
#      234236 :"Hardik", 7356345 :"Bhuvi", 8 :"Jadeja", 92 :"Bhumra",1311240 :"Shami",11 :"Kuldeep"}

# # The number associated with the string in the dictionary need not be in a order it can be random

# for i in d :
#     print("  ",i,end = ' ')
#     print(d[i])


# #=================================================

# #Method 1
    
# print("Enter the number of rows")

# n = int(input() )

# for i in range(1,n+1) :
    
#     for j in range(1, i+1) :
        
#         print("* ", end = ' ')

#     print()

 
# print("end")

# #============================================

# #Method 2

# print("Enter the number of rows")

# n = int(input() )

# a = '*'

# for i in range(1,n+1) :      # '*' is a overloaded operator which mutilpies the times the string is printed
    
#     print(a*i)

# print("end")  