print("Enter your name")
 
name = input()

print("My name is %s \n"% name)

print(name[4])

print(name[4:12])   # THIS IS CALLED SLICING

print(name[4:12:2]) #THIS IS CALLED SLICING AND STRIDING

#In this the last number is the after which the char is printed 

print(name.strip('A'))

print(max(name))

print(name.swapcase())

print(list(enumerate(name)))      

#================================================================


print("Enter your name")
name = list(input())


print("My name is %s \n"% name)

for i in name :
    
    x= name.count(i)
    print("{0} = {1}" .format(i, x))
 
#=================================================================
    
    
def char_frequency(str1) :
    
    dic = {}
    
    for n in str1 :
        x = dic.keys()
        
        if n in x :
            dic[n] += 1

        else :
            dic[n] = 1
    
    return dic
    
print("Enter string")

s = input()

d = char_frequency(s)

print(d)

#==========================================================


def word_count(str) :
    
    count = {}
    word = str.split()

    for i in word :
        
        if i in count :
            count[i] += 1

        else :
            count[i] = 1
    
    return count
    
    
print("Enter string")

s = input()

print(word_count(s))
    

#========================================


def pass_gen(str,bday) :
    
    if len(s) < 2 :
        return''
    
    else :
        password = (bday[0]+s[0:2]+s[-2:]+bday[1]) [::-1]  #  IMPORTANT  #
    
    return password


print("Enter name")
s = input()

print("Enter birthdate")
n = (input())

print(pass_gen(s,n))

#============================================

print("Enter the number")

n = (input())

ans = ''

s=len(n)

for x in range(1,s,2) :

    ans = ans + str(int(n[x]) ** 2)

print(ans[0:4])


#-=======================================

print("Enter the string")
n = (input())

list1 = []

list1 = n.split(",")

list1.sort()

o = ","

print()
print(o.join(list1)) #For Converting list to string


#=================================================



def caesar(realText,step):
    
    outText = []
    crypting = []
    
    uppercase = ['A','B','C','D','E']
    
    lowercase = ['a','b','c','d','e','f','g','h','i','j','k']

    for eachLetter in realText :
        
        if eachLetter in uppercase :
            
            index = uppercase.index(eachLetter)
            crypting = (index + step ) % 26
            newLetter = uppercase[crypting]
            outText.append(newLetter)
        
        elif eachLetter in uppercase :
            
            index = lowercase.index(eachLetter)
            crypting = (index + step ) % 26
            newLetter = lowercase[crypting]
            outText.append(newLetter)
    
    return outText



print("Enter string")

s= input()

code = caesar(s,2) 

print("".join(code))


