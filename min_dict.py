# dictionary = {"a": 5, "b": 2, "c": 8}
 
# # get key with min value
# min_key = min(dictionary, key=dictionary.get)
 
# print(min_key)
# # print output => "b"
 
# print(dictionary.get(min_key))

# d = {"a": 5, "b": 2, "c": 8}
# min=10
# for i,j in d.items():
#     if j<min:
#         min=j
# print(min)

d = {"a": 5, "b": 2, "c": 8}
min=10
for i in d:
    if d[i]<min:
        min=d[i]
print(min,i)
 