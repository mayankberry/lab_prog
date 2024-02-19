a = input("Enter Pin : ")

d = {'0' : 'zero', '1' : 'One', '2' : 'Two', '3' : 'three', '4' : 'four', '5' : 'five'}

for i in a:
    if i in d:
        print(d[i])
        