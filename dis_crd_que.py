a=[{'v':"soo1"},{"v":"soo2"},{"vi":"soo1"},{"vi":"soo5"},{"vii":"soo5"},{"v":"soo9"},{"vii":"soo7"}]
b=[]
for i in a:
    c=i.values()
    if c not in b:
        b.extend(c)
print(b)

# def abc(n):
#     return n*n*n
#     print("hi")
# print(abc(3))

# d=[2,4,5,7]
# my_dict={}
# Sum=0
# i=0
# while i<len(d):
#         sum=d[i]
#         my_dict.update({i:sum})
#         i+=1
# print(my_dict)

x={'V': [1, 4, 6, 10,11], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
for i,k in x.items():
    for j in k:
        if j%2!=0:
            x[i].remove(j)
print(x)

my_dict = {}
my_dict[(1,2,4)] = 8
my_dict[(4,2,1)] = 10
my_dict[(1,2)] = 12

sum = 0
for k in my_dict:
    sum += my_dict[k]

print(sum)
print(my_dict)