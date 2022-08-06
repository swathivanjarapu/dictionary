# d={'a':3,'b':7,'c':11,'d':2}
# max=0
# for i in d.values():
#     if i >max:
#         max=i
# print(max)

d={'a':3,'b':7,'c':11,'d':2}
max=0
s=0
for i in d:
    if d[i] >max:
        max=d[i]
    elif max>d[i] and d[i]>s:
        s=d[i]
print(s)
print(max)