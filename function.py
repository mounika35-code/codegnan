#functions 
#  -block of code to do particular task:
#WHY USE FUNCTION-TO REPEATETATION OF TASK

#function syntax:
#def function_name(parameters):

#function creation or definition
# def greet():  #greet-function name
#     #function_body
#     return "hello students"
# function_calling
#     print(greet())

#user defined functions
#types of functions
#type 1:no parameters,no return value

# def greet(name):
#     print("hello",name)
# greet("mouni") 
   
#type 3

# def get_number():
#     return 100
# result=get_number()
# print(result)

#type 4
# def add(a,b):
#     return a+b
# result=add(2,3)
# print(result)

#result-gives the result back to the program

#returning multiple values
# def calc(a,b):
#     add=(a+b)
#     sub=(a-b)
#     return add,sub
# x,y=calc(20,10)
# print(x)
# print(y)

#positional arguments
#arguments are matched based on their position

# def student(name,age):
#     print("name:",name)
#     print("age:",age)
# #function_calling
# student("mounika",20)    

#keyword argument

# def student(name,age):
#     print(name)
#     print(age)
# student(age=20,name="mounika")    

#default arguments

# def greet(name="student"):
#     print("hello",name)
# greet("codegnan")    

#variables-length arguments(*args)
# def add(a,b):
#     print(a+b)
# add(2, 3, 4, 5, 6, 7)    

# def add(*numbers):
#     total=0
#     for number in numbers:
#         total+=number
#     return total 
# print(add(10,20))
# print(add(1,2,3,4,5,6,7,8,9))    

#*args -it collects multiple positional arguments into 
#a tuple
#keyword variable-length argument(**kwargs)

#accept multiple keyword  arguments

# def student_details(**details):
#     print(details)
# student_details(
#     name="mouni",
#     age=20,
#     city="hyderabad"
# )

#**kwargs->dictionary
def example(*args,**kwargs):
    print(args)
    print(kwargs)
example(10,20,30,name="mounika",age=20)