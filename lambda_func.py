#lambda functionss

#anonymous-without name
#small anonymous functions
#single line functions

#lambda syntax:
#lambda arguments:expression

# def square(x):
#     print(x*x)
# square(5)

# #lambda:
# square=lambda x:x*x
# print(square(6))

#lambda:
#lambda with one parameter
# square=lambda x:x*x
# print(square(6))

#lambda with multiple parameters
# add=lambda x, y, z:  x + y+ z
# print(add(27, 30, 13))

#LAMBDA WITH IF-ELSE

# check=lambda x: "EVEN" if x % 2==0 else "odd"
# print(check(7))
# print(check(10))

#when should we use lambda?

#small functions temporarily,especially with:
#map(),filter(),sorted(),reduce()

#map-it applies function to every element
#of an iterable
#syntax:map(function,iterable)

# nums=[1,2,3,4,5]
# squares=list(map(lambda x:x*x ,nums))
# print(squares)

#map without lambda
# def square(x):
#     return x*x

# numbers=[1,2,3,4,5]
# result=map(square,numbers)
# print(list(result))

#filter()-it is used when we want to select only
#elements that satisfy a condition

#syntax:filter(function,iteration)

# nums=[1,2,3,4,5,6]
# result=filter(lambda x:x % 2==0,nums)
# print(list(result))

#reduce()-it repeatedly applies a function to
#elements and reduces entire sequence to one 
#final value

#from funtools inport reduce
# from functools import reduce
# numbers=[1,2,3,4,5]
# result=reduce(lambda a,b:a+b,numbers)
# print(result)

# names=["mounika","vinita","triveni","suma"]
# result=sorted(names,key=len)
# print(result)

#sorting words by last character
names=["mounika","triveni","vinita","santhi"]
result=sorted(names,key=lambda x:x[-1])
print(result)