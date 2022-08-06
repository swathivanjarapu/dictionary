m = {'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20}
# a=[]
# for i in m:
#     a.append(m[i])
# print(a)
# max=0
# sec=0
# thi=0
# i=0
# while i<len(a):
#     if a[i]>max:
#         thi=sec
#         sec=max
#         max=a[i]
#     elif a[i]>sec:
#         thi=sec
#         sec=a[i]
#     elif a[i]>thi:
#         thi=a[i]
#     i=i+1
# print(max)
# print(sec)
# print(thi)

f=0
s=0
t=0
for i in m:
    if m[i]>f:
        t=s
        s=f
        f=m[i]
    elif m[i]>s:
        t=s
        s=m[i]
    elif m[i]>t:
        t=m[i]
   
print(f)
print(s)
print(t)
