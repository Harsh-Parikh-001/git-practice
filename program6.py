#Object oriented programming

class Data :
    
    a=10
    b=20
    
    def display(self):
        
        print("A = ", self.a)
        print("B = ",self.b)


d = Data()

print(d.a)
print(d.b)

d.display()


#===========================================

class Data :

    @staticmethod
    
    def display(a,b):
        
        c = a +  b
        
        print("Answer = ", c)


class Compute :

    @staticmethod
    def input():
        
        a = int(input("Enter the value"))
        b = int(input("Enter the value"))
        
        d1 = Data()
        
        d1.display(a,b)


d2 = Compute()
d2.input()


#================================================

class Data :

    
    def read (self):
        
        self.a = int(input("Enter the value"))
        self.b = int(input("Enter the value"))


    def compute(self) :
        self.ans = self.b + self.a


    def display(self) :
        print("Answer = ", self.ans)

c = Data()
c.read()
c.compute()
c.display()

#================================================

#     PENDING     #
 
# class Data :
    
#     def read(self):
#         print("1. Circle")
#         print("2. Square")
#         self.n = (print("Enter the option number"))

#     def compute(self ):
#         if(self.n==1):
#             self.a = int(print("Enter the radius"))
#             ans = 3.14*self.a*self.a 
            
#         if(self.n == 2):
#             self.a = int(print("Enter the side"))
#             ans = self.a * self.a 
        
        
#     def display(self):
        
#         print("Answer = ", ans)
        
# d = Data()
# d.read()
# d.compute()        
# d.display()
        
        
#===============================================

# #  PENDING   #

# class Data :
#     a = 10
#     __b = 20
    
#     def __printdata():
#         print("INSIDE PRIVATE")
        
#     def display():
#         print("a = ", self.a)
#         print("b = ", self.b)
        
#         self.__printdata()
        

# d1 = Data()

# d1.display()


