#loops:doing the same task for the repetition of times
#1,for loo
#2,while loop
#for loop:when we know the number of iterations need to perform
#eg:cooking for for a family
#while loop:when we dont know the number of iterations needs to perform
#eg:cooking food in restaurant

#1,by using index:

# for i in range(1,11):
#     print("hello")

# nums=[10,20,30,40,50]
# for i in range(0,5):
#     print(nums[i]) 

#by using value
# nums=[10,20,30,40,50]
# for num in nums:
#   print(num)

#while loops:

# i=1
# while i<=5:
#     print(i)
#     i+=1


#print even numbers from 1 to 10
# i=0
# while i<=10:
#     if i %2==0:
#         print(i)
#   i+=1 

# for i in range(10,0,-1):
#     print(i)


# i=10
# while i>=1:
#     print(i)
#     i-=1

#sum of numbers from 1to N
# total=0
# for i in range(1,11):
#     total+=i
#     print(total)

#MULTIPLICATION TABLE
# num=int(input("enter number:"))
# for i in range(1,11):
#     print(num*i)

#finding largest number in array without max()

# nums=[10,20,30,40,50]
# largest=nums[0]
# for num in nums:
#     if num>largest:
#         largest=num
# print(largest)        


name="mounika"
reverse_name =name[::-1]
print(reverse_name)
