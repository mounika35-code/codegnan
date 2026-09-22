# this is first portion of python 
#print:show something on the screen
# print("hello")
# print("mounika")
# print(10+20)
# print(30)


#COMMENTS:python does not execute this lines when use # symbol is to understand ourself or other programmers
# print("hello")
# print("mounika")

#VARIABLE :is a name used to store data values
# name="mounika"
# age=22
# course="python"
# print(name)
# print(age)
# print(course)


#DATA TYPES:is used to tell python what kind of values we are storing
#there are four types in this that are
# name="mounika"    #string
# age=22   #integer
# percentage=84.9   #float
# is_student=True   #boolean
# print(name)
# print(age)
# print(percentage)
# print(is_student)



# TYPE()tells us what type of data something is:
# name="mounika"   
# age=22   
# percentage=84.9   
# is_student=True   
# print(type(name))
# print(type(age))
# print(type(percentage))
# print(type(name))


#INPUT():takes information from user
# name=input("enter your name:")
# print(name)


#type conversion is having input can be give like a str(text) it can take everything
# age=int(input("enter your age:"))
# print(type(age))


# OPERATORS
# ARTHIMETIC OPERATORS:are used to perform calulations
# a=10
# b=20
# print(a-b)   #subtract
# print(a+b)   #addition
# print(a*b)   #multiply
# print(a/b)   #divide
# print(a//b)  #floor division
# print(a**b)  #power
# print(a%b)   #remainder operators

#comparision operator:are used to compare two values 
# a=10
# b=5
# print(a<b)   #a is lesser than b
# print(a>b)   #a is greater than b
# print(a==b)   #equal 
# print(a!=b)    #not equal to
# print(a>=b)    #greatherthan or equal to
# print(a<=b)     #lesserthan or equal to
# = is a assign/store 
#==is a compare values


#logical operators:both conditions must be true 
# age=22        #it is AND OPERATOR
# has_id=True
# print(age >=18 and has_id==True)
# age=22         #IT IS OR OPERATOR
# has_permission=True
# print(age >=18 or has_permission==True)
# is_student=True #REVERSE OPERATOR
# print(not is_student)


# ASSIGNING OPERATOR:
# number=20
# number+=5     #it is operator of +=
# print(number)
# number=20
# number-=5      #it is operator of -=
# print(number)
# number=20       # it is operator of *=
# number*=5
# print(number)
# number=20        # it is operator of /=
# number/=5
# print(number)


# membership operator:check whether something exist inside another value: 
# name= "mounika"

# print("m" in name)   #it is a in operator
# print("z"in name)
# print("m"not in name)  # it is not in operator
# print("z"not in name)


    # IDENTIFY OPERATORS:CHECK WHETHER TWO VARIABLES ARE REFFERING TO SAME OBJECT IN MEMORY
# A=[1,2]
# B=[1,2]
# print(A==B)
# print(A is B)     #IT IS A IS OPERATOR
# print(A is not B)    #IT IS IS NOT OPERATOR


#IF STATEMENT :IT ALLOWS THE PROGRAM TO MAKE A DECISION
# age=22
# if age >=18:       #it is a if statement
#     print("you are eligible")

# age=int(input("enter your age:"))
# if age>=18:
#     print("you are eligible")      #it is a input with if statement


# age=int(input("enter your age:"))
# if age>=18: 
#  print("you are eligible")       #it is using with input and else
# else:  
#  print("you are not eligible")


# age=int(input("enter your age:"))
# if age>=18:
#     print("adult")            #it is using elif method
# elif age>=13:
#     print("teenager")
# else:
#     print("child")    


# marks=int(input("enter your marks:"))
# if marks>=90:
#     print("A GRADE")
# elif marks>=80:            #i used multiple elif conditions
#     print("B GRADE")
# elif marks>=75:
#     print("C GRADE")
# else:
#     print("fail")    


#nested if means an if statementinsideanother if statement
# age=int(input("enter youe age:"))
# has_id=input("D0 you have id? ")
# if age>=18:
#     if has_id=="yes":
#         print("you can enter")
#     else:
#          print("ID is required")
# else:
#     print("you are under 18")         
                        

# age=int(input("enter your age:"))
# has_id= input("DO YOU HAVE AN ID")     #it is if with AND CONDITION
# if age>=18 and has_id=="yes":
#     print("you can enter")
# else:
#     print("you cannot enter")    


# age=int(input("enter your age:"))
# has_id= input("DO YOU HAVE AN ID")     #it is if with OR CONDITION
# if age>=18 or has_id=="yes":
#     print("you can enter")
# else:
#     print("you cannot enter")    



is_raining=False
if not is_raining:
    print("you can go outside")     #it is reverse condition
else:
    print("take an umbrella")    


#conditional expression
# age=int(input("enter your age:"))
# if age>=18:
#     result="ADULT"        #value_if_true if condition else value_if_false
# else:    
#     result="CHILD"
# print(result)
# age=int(input("enter your age:"))
# result="ADULT" if age>=18 else "CHILD"    #oneline code of conditional expression
# print(result)


#truely and fasely conditions:python treats some values as true and some as false when used in condition
# name=(input("enter your name:"))
# if name:
#     print("you have a name")
# else:
#     print("you did not have a name")    