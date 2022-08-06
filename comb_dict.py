# dict1 = {'a': 12, 'for': 25, 'c': 9}
# dict2 = {'Geeks': 100, 'geek': 200, 'for': 300}
  
  
# # adding the values with common key
# for key in dict2:
#     if key in dict1:
#         dict2[key] = dict2[key] + dict1[key]
#     else:
#         pass
          
# print(dict2)


d1 = {'a': 100, 'b': 300, 'c':300, 'r':900}
d2 = {'b': 300, 'a': 200, 'd':400}
for i in d1:
    if i in d2:
        d1[i] = d1[i] + d2[i]
print(d1)
