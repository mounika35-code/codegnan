# for i in range(1,6):
#     for j in range(i):
#         print("*",end=" ")
#     print()
#1st iter i=1 j(0,1)j=0
# 2nd iter =i=2 j(0,2)
# 3rd iter=i=3 j(0,3)j=0,1,2
# j(0,4) ,0,1,2,3      
# 
# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()    


# for i in range(5):
#     for j in range(5):
#         print("*",end=" ")
#     print()    


# rows=4
# cols=8
# for i in range(rows):
#     for j in range(cols):
#         print("*",end=" ")
#     print()    

# rows 0->5 spaces-0star
# rows 1->4 spaces-1star
# rows 2->3 spaces-2star
# rows 3->2 spaces-3star
# rows 4->1 spaces-4star
# rows 5->0 spaces-5star
    
# n=5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()        

# n=5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(2*i-1):
#         print("*",end="")
#     print()    


# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()    

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end="")
#     print()    


# for i in range(1,6):
#     for j in range(5,5-i,-1):
#         print(j,end="")
#     print()    


# num=1
# for i in range(1,5):
#     for j in range(i):
#         print(num, end=" ")
#         num +=1
#     print()    

# for i in range(6):
#     for j in range(5,0,-1):
#         print(j,end="")
#     print()    


# for i in range(5,1,-1):
#     for j in range(5,5-i,-1):
#         print(j,end="")
#     print()    

# for i in range(1,6):
#     for j in range(i,0,-1):
#         print(j,end="")
#     print()    

#pyramid patterns

# n=5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(1,2*i):
#         print(j,end="")
#     print()        


# n=5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(0,2*i-1):
#         print(i,end="")
#     print()        


# n=5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(1,2*i):
#         print("*",end="")
#     print()        
# for i in range(n-1,0,-1):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(1,2*i):
#         print("*",end="")
#     print()        


# n=int(input("enter the number of rows:"))
# #upper pyramid
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(1,2*i):
#         print("*",end="")
#     print() 
# #lower pyramid       
# for i in range(n-1,0,-1):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(1,2*i):
#         print("*",end="")
#     print()        


#name patterns

#code

#C
#Co
#COD
#CODE

# name="CODE"                        
# for i in range(1,len(name)+1):
#     for j in range(i):
#         print(name[j],end="")
#     print()    

    
# name="CODE"                                #c
# for i in range(1,len(name)+1):             #cc
#     for j in range(i):                     #ccc
#         print(name[0],end="")              #cccc
#     print()    

   
# name="CODE"                        
# for i in range(0,len(name)):                  #C
#     for j in range(i+1):                      #OO
#          print(name[i],end="")                #DDD
#     print()                                   #EEEE


n=5
for i in range(1,n+1):
    #spaces before the pyramid
    for j in range(n-i):
        print(" ",end="")
   #spaces between the stars
    for j in range(1,2*i):
        if i==n:
            print("*",end="")
        elif j==1 or  j==2*i-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()                     