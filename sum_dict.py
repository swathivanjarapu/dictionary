# Write a Python program to sum all the items in a dictionary.
# d= {'a': 100, 'b':200, 'c':300}
# s=0
# for i in d:
#     s=s+d[i]
# print(s)

d= {'a': 100, 'b':200, 'c':300}
def itemSum(dict):
     sum = 0
     for i in dict.values():
           sum = sum + i
      
     return sum
 
# Driver Function
# dict = {'a': 100, 'b':200, 'c':300}
# print("Sum :", itemSum(dict))

# my_dict = {}
# my_dict[(1,2,4)] = 8
# my_dict[(4,2,1)] = 10
# my_dict[(1,2)] = 12

# sum = 0
# for k in my_dict:
#  sum += my_dict[k]

# print(sum)
# print(my_dict)

# dict1={1:2,2:3,3:4,4:5}
# sum=0
# for i in dict1.values(): 
#  sum=sum+i
# print(sum)

# my = {'data1':100, 'data2': -54,'data3': 247}
# s=0

# for i in my.values():
#     s=s+i
# print(s)

my = {'data1':100, 'data2': -54,'data3': 247}
for i,j in my.items():
    if j==-54:
        my[i]=78
print(my)



