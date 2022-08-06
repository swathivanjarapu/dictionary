# d=[{"first":1}, {"second": 2},{"third": 1}, {"four": 5},{"five":5}, {"six":9}, {"seven":7}]
# a=[]
# for i in d:
#     for j in i.values():
#         if j not in a:
#             a.append(j)
# print(a)

# l= [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# print("Original List: ",L)
# u_value = set( val for dic in L for val in dic.values())
# print("Unique Values: ",u_value)

# for i in l:
#     for j in i.values():
    
    
dict={1:10,2:60,3:30,5:50,4:60,5:3}
# output={10: [1], 60: [2, 4], 30: [3], 3: [5]}

i=1
a={}
c=[]
while i<=len(dict):
    if dict[i]==dict[i]:
        a[dict[i]]=[i]
    # else:
    #     a[dict[i]]=[i]
    print(a)
    # a[dict[2]]=c
    # j=i+1
    # while j<len(dict):
    #     if dict[i]==dict[j]:
    #         c.append(i)
    #         c.append(j)
    #         a[dict[2]]=c
        
    #     j=j+1
    i=i+1
# print(a)
