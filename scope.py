#scope
#scope is the region of a program where a variable can be accessed
#local scope
#global scope

#local scope-
#a variable that created  inside a function 
#a variable that creaated outside a funtion

#local scope
# def display():
#     name="mounika"
#     age=22
#     print(name)
#     print(age)
# display()    

#different functions can have a variable with same name

#comment code
# def first():
#     x=10
#     print(x)

# comment code
# def second():
#     x=20
#     print(x)  

#first()
#second()
      
#global scope -varibles declared outside the 
#function has global scope

# name="mounika"
# age=22
# #comment code
# def display():
#     print(name)
#     print(age)
# display()
# print(name)

#code suggestions

# x=100
# #comment code
# def display():
#     global x
#     x=200
# print(x)
# display()
# print(x)


#pass by value and pass by reference
#comment code
# def display (x):
#     x=20
# a=10
# display(a)
# print(a)

# def change(x):
#     x=20
#     print("inside func:",x)
# a=10
# change(a)
# print("outside func:",a)
# change(a)
# print("outside function:",a)

#X receives a refrences to the same integer
# object
# x=20
# before:
# a->10 x =10
# after x =20
# a -10,x=20

#comment code
# def add_10(x):
#     x+=10
#     print("inside func:",x)
# nums=50
# add_10(nums)
# print("outside func:",nums)

#code suggestions

# comment Connection

# def add_element(data):
#     data.append(40)
# values=[10,20,30,]
# add_element(values)
# print(values)

#recursion 
# 5
# 4
# 3
# 2
# 1

#for i in range(5,0,-1):
#print(i)

# comment code
# def count_down(n):
#     #base case
#     if n==0:
#         return
#     #recursion case
#     print(n)
#     count_down(n-1)

# count_down(5)

#factorial of a number using recursion

# comment Code
def fact(n):
    #base case
    if n <=1:
        return 1
    #recursion case
    return n*fact(n-1)
print(fact(5))
