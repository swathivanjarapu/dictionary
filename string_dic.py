st = input("Enter a string: ")
dic = {} #creates an empty dictionary
for ch in st:
    if ch in dic: #if next character is already in the dictionary
        dic[ch] += 1
    else:
        dic[ch] = 1 #if ch appears for the first time
for key in dic:
    print(key,':',dic[key])
print(dic)


t="abracadabraaabbccrr"
a={}
c=0
l=[]
for i in t:
    if i not in l:
        l.append(i)
        a[i]=0
    c=c+1
    a[i]+=1
print(a)

  