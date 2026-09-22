#identify number either positive or negative or zero 

# num=int(input("enter number:"))
# if num>0:
#     print("positive")
# elif num < 0:
#     print("negative")
# else:        
#     print("zero")


# num=int(input("enter number:"))
# if num%2==0:
#     print("even")
# elif num%  2!=0:
#     print("odd")
# else:
#     print("zero")        



# a=int(input("enter first number:"))
# b=int(input("enter second number"))
# if a>b:
#     print("first number is larger")
# elif b>a:
#     print("second number is a larger")
# else:
#     print("Both are equal")        


#username:admin
#password=password123

# username=input("enter your username:")
# password=input("enter your password:")
# if username == "admin":
#  print("login sucess")
# elif password=="password123":
#   print("login sucess")
# else:
#   print("login failed")
   
# age=int(input())
# license_valid=input("yes/'no")
# if age>=18:
#     if license_valid=="yes":
#         print("you can drive")
#     else:
#         print("valid license required")
# else:
#         print("Too young to drive")              



#movie ticket pricing

#below 5-free
#5-12=100
#13-59=200
#60 and above-120

# age=int(input("enter your age:"))
# if age<=5:
#     print("free")
# elif age<=12:
#       print("100 ticket price")
# elif age <=59:
#     print("200 ticket price")
# else:
#      print("120 ticket price")     
        


# leap=int(input("enter your leap year"))
# if leap % 4==0:
#     print("leap year")
# else:
#     print("not a leap year")    




# performance=int(input("enter your performance:"))
# experience=int(input("enter your experience:"))
# if performance>=90 and experience>=5:
#     print("20% Hike")
# elif performance>=90 and experience<=5:
#     print("10% Hike")
# elif performance>=80:
#     print("10% Hike")
# elif performance>=70:
#     print("5% Hike") 
# else:
#     print("No Hike")    
               

# num=int(input("enter a num:"))
# orginal=num
# reverse=0

# while num>0:
#     digit=num%10
#     reverse=reverse*10+digit
#     num//=10

# if orginal==reverse:
#     print("palindrome")
# else:
#     print("not a palindrome")    


#factorial

#5!=5*4*3*2*1=120

# num=5
# factorial=1

# while num>0:
#     factorial *=num
#     #fact =fact*num
#     num-=1
# print(factorial)    


#fibonnaci series
#0 1 1 2 3 5 8 13 21 34 55

# n=10
# a=0
# b=1
# for i in range(n):
#     print(a,end="")
#     a,b=b,a,a+b
    

#finding duplicate numbers in a list
numbers=[1,2,3,4,5,1,2]
for i in range(len(numbers)):
    for i in range(i+1,len(numbers)):
        if numbers[i]==numbers[i]:
            print(numbers[i])
