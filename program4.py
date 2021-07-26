# Function overloading solution

def info(s,*names) :
    print("Information about = ",s)
    
    for i in names:
        print(i)


info("food", "Indian", "Italian" , "Mexican")

print("=========================")

info("cars" , "BMW" , "Audi" , "Mercedes" , "Ford")

print("=========================")
 
info("city" , "Mumbai" , "Barcelona" , "Milan" , "New York" , "London" , "Moscow")

#===============================================================

def add(*num) :
    c = sum(num)        # the sum fuction will add all the values in a list
    print("Answer = ",c)
 
print("Enter the number of digits")

n = int(input())
num=[]

print("Enter the numbers")

for i in range(1,n+1):
    
    a = int(input())
    num.append(a)

add(*num)

#=====================================================================

def add(*num) :
    
    c = max(num)        #To find the max number in a given list
    
    print("Answer",c)
       
print("Enter the number of digits")

n = int(input())
num=[]

print("Enter the numbers")

for i in range(1,n+1):
    
    a = int(input())
    num.append(a)

add(*num)

#=====================================================================

def compute(a) :
    
    return a + 2

calculate = compute # A single fuction can be called with multiple names

ans = compute(12)

ans1 = compute(22)

print(ans)

print(ans1)

#=========================================================

def say(func):
    
    def employer():
        
        print("Say something")
        
    def say_name() :
        
        print("Harsh Parikh")
        
    def say_nationalty() :
        
        print("India")
        
    def wrapper() :
        
        employer()
        
        say_name()
        
        say_nationalty()

        func()
   
    return wrapper  
   
@say
def start_interview() :
 
    print("Interview starts")

start_interview()

#=============================================================

#calendar

import calendar

year= int(input("values"))

print("The calendar year is ", year)

print(calendar.calendar(year,2,1,6))

#======================================================================

from datetime import datetime

n = datetime.now()

print("Now ",n)


print("Todays date",n.strftime('%Y-%m-%d'))

print("Todays Date",n.strftime('%m-%d-%Y'))

print("year",n.year)
print("Month",n.month)
print("Day",n.day)
print("Time",n.time())
print("Hour",n.hour)
print("Minute",n.minute)
print("Second",n.second) 