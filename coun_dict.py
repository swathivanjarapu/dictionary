# d =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
# c=0
# for i,j in d.items():
#     c+=j
# print(c)


# d=[{"name":"liki"},{"dosth":"preethi"},{"mentor":"savitha"}]

# x=input("enter ")
# for i,j in d:
#     print([x.get(i) for x in j])


# d={'a':[8,9,10],'b':[4,3,2]}


# for i in d.values():
#     a=0
#     for j in i:
#         a+=j
#     print(a)
a='418'
# O/P16,1,64
i=0
while i<len(a):
    b=int(a[i])*int(a[i])
    print(b)
    i=i+1