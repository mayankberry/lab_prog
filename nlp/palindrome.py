# str = input("Enter String ")


# def check(str):
#     return str == str[::-1]
 

# res = check(str)
 
# if res:
#     print("It is a Palindrome")
# else:
#     print("It is Not a Palindrome")



# ways to remove ith charecter in python
# upper case half string 
# capitalize the first and last charecter in string of eacgh word
# Wap to enter only vovels in a string 
# count the number of matching charecters in a pair of string 


# Task 1  

# c = ""
# s = input("Enter String : ")
# d = list(s)
# word = input("Enter Chareter to Remove : ")

# for i in range(0, len(d)-1):
#     if d[i] == word:
#         d.pop(i)
#         f = c.join(d)
#         print(f)

# Task 2

s = "mayank"

o = s[:len(s)//2]
print(o.upper())



