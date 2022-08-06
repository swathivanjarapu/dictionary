# fruit = {}

# def addone(index):
#     if index in fruit:
#         fruit[index] += 1
#     else:
#         fruit[index] = 1
# addone('Apple')
# addone('Banana')
# addone('apple')
# addone('Apple')

# print(len(fruit))
# print(fruit)

dict1 = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
for each_row in zip(*([i] + (j)for i, j in dict1.items())):
    print(*each_row, " ")
