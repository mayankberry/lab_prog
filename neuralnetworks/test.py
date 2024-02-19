# a = input("Enter string ")
a = "AABBBAAC"

str_lst = list(a)
emp_lst = []

d = {}

for i in range(0, len(str_lst)):
    if str_lst[i] not in emp_lst:
        emp_lst.append(str_lst[i])

print(emp_lst)


# for i in str_lst:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1

# print(d)

print(str_lst)


count = 0
for i in range(0, len(str_lst)):
    for j in range(i, len(str_lst)):
        if str_lst[i] == str_lst[j]:
            count += 1
        else:
            count = 0
    print(str_lst[i], "is times : ", count)