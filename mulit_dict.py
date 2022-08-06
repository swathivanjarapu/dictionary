# Write a Python program to multiply all the items in a dictionary.

# d={'a':2,'b':6,'c':3,'d':7}
# b=1
# for i in d:
#     b=b*d[i]
# print(b)

d={'a':2,'b':6,'c':3,'d':7}
b=1
for i in d.values():
    b=b*i
print(b)