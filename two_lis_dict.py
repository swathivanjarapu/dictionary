fruits = ['mango', 'pear', 'apple','papaya']
price = [90, 78, 110, 60]

fruits_price = zip(fruits, price)

# create dictionary
fruits_dict = {}

for key, value in fruits_price:
    if key in fruits_dict:
        # handling duplicate keys
        pass 
    else:
        fruits_dict[key] = value
        
print(fruits_dict)


students = ['Smith', 'John', 'Priska', 'Abhi']
marks = [93, 89, 91, 88]

# Given lists
print("List of Students : ", students)
print("list of Marks : ", marks)

# Convert to dictionary
res = {students[i]: marks[i] for i in range(len(students))}
print("Dictionary from lists :\n ",res)


items = ['pen', 'paper', 'pencil']
quantities = [5, 20, 15]
items_dict = {key:value for key, value in zip(items, quantities)}

print(items_dict)


students = ['Smith', 'John', 'Priska', 'Abhi']
marks = [89, 53, 92, 86]

students_dict = dict(zip(students, marks))
print(students_dict)

a=['a','b','c','d']
b=[1,2,3,4]
i=0
c={}
while i<len(a):
    c[a[i]]=b[i]
    i=i+1
print(c)

str1 = 'w3resource' 
my_dict = {}
for letter in str1:
    my_dict[letter] = my_dict.get(letter, 0) + 1
print(my_dict)

    
