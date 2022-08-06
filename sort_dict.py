# d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

# s= sorted(d.items())

# print('ascending order : ',s)

# s1= dict( sorted(d.items(),reverse=True))

# print('descending order : ',s1)

# x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_x = sorted(x.items(), key=lambda kv: kv[1])
# print(sorted_x)

# import operator
# x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_x = sorted(x.items(), key=operator.itemgetter(1))
# print(sorted_x)

# import operator
# x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_x = sorted(x.items(), key=operator.itemgetter(0))
# print(sorted_x)