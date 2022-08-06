# n=int(input("enter "))
# d={}
# for i in range(n):
#     s=input("enter ")
#     d[s]={}
#     k=input("enter ")
#     v=int(input("enter "))
#     d[s][k]=v
# print(d)
# n=int(input(" enter "))
# m=int(input("enter  "))
# while n<=10:
#     print(n)
#     n+=1


d={'shop':{'chaco':15, 'biscu':50,'dirymilk':30,'ice_crem':20}}
# print(d['shop']['chaco'])
item=input("enter ")
qu=int(input("enter "))
for i in d:
    # print(i)
    if d[i][item]==qu:
        print("this quatity")
    else:
        print("it is more than",qu-d[i][item])
        
#     if item in i
#    print("give the quatatie",d[i][item])