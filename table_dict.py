# my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
# for row in zip(*([key] + (value) for key, value in sorted(my_dict.items()))):
#     print(*row)

d={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
c=result = map(dict, zip(*[[(key, val) for val in value] for key, value in d.items()]))
print(list(c))


for i,j in d.items():
    for k in j:
        a=map(dict,zip(i,k))
    print(a)