# dic1={1:10, 2:20}
# dic2={3:30,2:40}
# dic3={5:50,6:60}
# for i  in dic1:
#     if i in dic2:
#          dic2[i]= dic1[i]+ dic2[i]

        
# # print( dic2)
# dic1.update(dic2)
# dic1.update(dic3)
# print(dic1)

# dic1={1:10, 2:20}  
# dic2={3:30, 2:40}  
# dic3={5:50,6:60}  
# # for i in dic1:
# #     if i in dic2:
# #         dic1[i]=dic1[i]+dic2[i]
# # print( dic1)
# dic4 = {}  
# for d in (dic1, dic2, dic3): 
#     if d in dic2:
#          dic1[d]=dic1[d]+dic2[d]
#          dic4.update(d)  
# print(dic4)  
Dic= {1: 'NAVGURUKUL',2: 'IN',  3:{'A' : 'WELCOME','B' : 'To','C' : 'DHARAMSALA'}}
del Dic[3]['A']
print(Dic)