# WAP to do tasks on strings 
# 1) Print complete string.
# 2) Print first charecter of the string. 
# 3) Print charecters starting from 3rd to 5th. 
# 4) Print string starting from 3rd charecter to end. 
# 5) Print string 2 times. 
# 6) Concat 2 strings and print it. 


str1 = "mayank"
str2 = "Berry"

print("Choose String Operation From the List ")
print(""" 
1) Print complete string.
2) Print first charecter of the string. 
3) Print charecters starting from 3rd to 5th. 
4) Print string starting from 3rd charecter to end. 
5) Print string 2 times. 
6) Concat 2 strings and print it.  """)

a = int(input("Enter Choice : "))
str1 = input("Enter String : ")

if a == 1:
    print(str1)
elif a == 2:
    print(str1[0])
elif a == 3: 
    print(str1[2:5])
elif a == 4:
    print(str1[2:])
elif a == 5:
    for i in range(2):
        print(str1)
elif a == 6:
    str2 = input("Enter Second String : ")
    print(str1 + str2)
else: 
    print("Invalid Input")


# Task 1

# print(str1)

# # Task 2

# print(str1[0])

# # Task 3

# print(str1[2:5])

# # Task 4

# print(str1[2:])

# # Task 5 

# for i in range(2):
#     print(str1)

# # Task 6
    
# print(str1 + str2)