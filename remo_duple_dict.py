# dict1 = {'A': 20, 'B': 15, 'C': 20, 'D': 10, 'E': 20}

# temp = []
# res = dict()
# for key, val in dict1.items():
#     if val not in temp:
#         temp.append(val)
#         res[key] = val
# print(res)


# d = {'A': 20, 'B': 15, 'C': 20, 'D': 10, 'E': 20}
# a={}
# for i,j in d.items():
#     if j not in a.values():
#         a[i]=j
# print(a)


# Write a Python program to remove duplicates from Dictionary.
d= {'id1': 
   {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id2': 
  {'name': ['David'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id3': 
    {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id4': 
   {'name': ['Surya'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
}
a=[]
b=dict()
for i,j in d.items():
    if j not in a:
        a.append(j)
        b[i]=j
print(b)


# res = {}

# for key, value in student_data.items():
#     if value not in res.values():
#         res[key] = value

# print(res)