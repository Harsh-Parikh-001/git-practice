#Method 1

print("Enter the number")

n = int(input())

prod = 1 

for i in range (1,n+1) :
    
    prod = prod * i 
    
print("Answer = ",prod)   

 
#============================================= 

#Method 2

#Usage of while loop

n = int(input("Enter the value"))

fact = 1

while (n > 0) :
    fact = fact * n
    n = n-1
    
print("Answer = ",fact)    

#==========================

# Q) To give all the possible combination of any 3 numbers

print("Enter the first value")
a = int(input())


print("Enter the second value")
b = int(input())


print("Enter the third value")
c = int(input())

d = []      #Declartion of list.  
            #Declaration in not needed in python but in order to append we declare

#Append is a method to add any value to a list 
#Append adds the value in the end of the list

d.append(a)
d.append(b)
d.append(c)

#The loop will keep on going till the values in the list ends 

for i in d :
    for j in d :
        for k in d :
            
            if(i!=j and j!=k and i!=k) :
                print(i,j,k)

#======================

#Method 1

print("Enter first list")

s1 = input()

n1=[]

n1.append(s1)

print("Enter second list")

s2 = input()

n2=[]

n2.append(s2)

n3 = []

n3 = n1 + n2

for i in n3 :
    print(i, end = ' ')


# Method 2

a=[]

c=[]


n1 = int(input("Enter the input"))

for i in range(1,n1+1,1) :
    b = int(input("Enter the elemnts"))
    a.append(b)


n2 = int(input("Enter the input"))

for i in range(1,n2+1,1) :
    d = int(input("Enter the elemnts"))
    c.append(b)
    
new = a+c

print("Merged list is:",new)

#================================================

# sort

n = int(input("Enter the number of elements"))

a =[]

for i in range(1,n+1,1) :
    b = int(input("Enter the elemnts"))
    a.append(b)

a. sort()

print(a)

#=================================

import calendar

y = int(input("Enter the year"))

m = int(input("Enter the month"))

print(calendar.month(y,m))

#=======================================

def func (a,b):
    
    c= a+b
    
    return c

a = int(input("Enter the number"))

b = int (input())

c = func(a,b)

print("ANSWER =",c)

#===================

def main() :
    print('''
      1. Add
      2. SUBSTRACT
      3. MULTIPLY
      4. DIVIDE
      5. Exit
          ''')

    n = int(input("Enter the option"))

    if(n == 1 ) :
        
        a = int(input("Enter the numbers"))
        b = int(input("Enter the numbers"))
        add(a,b)

    elif(n == 2 ) :
        
        a = int(input("Enter the numbers"))
        b = int(input("Enter the numbers"))
        sub(a,b)

    elif(n == 3 ) :
        
        a = int(input("Enter the numbers"))
        b = int(input("Enter the numbers"))
        mult(a,b)

    elif(n == 4 ) :
       
        a = int(input("Enter the numbers"))
        b = int(input("Enter the numbers"))

        div(a,b)
        
    elif(n == 5) :
        quit()

def add (a,b) :
    print("ANSWER = ",a+b)
    main()
    
def sub (a,b) :
    print("ANSWER",a-b)
    main()

def mult(a,b) :
    print("ANSWER = ",a*b)
    main()

def div(a,b) :
    print("ANSWER = ", a/b)
    main()


main()

#======================================

def swap (a,b) :
    a,b = b,a
    #This is how we swap two numbers
    
    print("After Swapping")
    print("a = ",a)
    print("b = ",b)


print("Enter the first number")
a = int(input())

print("Enter the second number")
b = int(input())

print("a = ",a)
print("b = ",b)

swap(a,b)

