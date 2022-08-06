# d =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
# c=0
# for i in d.values():
#     for j in i:
#         c+=1
# print(c)

# stu = [{'id': 1, 'success': True, 'name': 'Lary'},
#  {'id': 2, 'success': False, 'name': 'Rabi'},
#  {'id': 3, 'success': True, 'name': 'Alex'}]
# c=0
# for i in stu:
#     for j in i.values():
#         c+=1
# print(c)
        

# a=[1,2,3,4,5]
# d={}
# for i in a:
#     d[i]={}
# print(d)

l=[1,2,3,4]
a=b={}
for i in l:
    b[i]={}
    b=b[i]
print(a)