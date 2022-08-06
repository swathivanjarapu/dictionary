in_filepath = 'in_file.txt'
def data_dict(in_filepath):
    with open(in_filepath, 'r') as file:
        for line in file.readlines():
            print(line)
            title, price, count = line.split()
            d = {}
        d['title'] = title
        d['price'] = int(price)
        d['count'] = int(count)
        return d
p=data_dict(in_filepath)
print(p)


# Write a program to display the name of all the employees whose salary is more than 25000 from the following dictionary. # emp={1:(“Amit”,25000),2:(“Suman”,30000),3:(“Ravi”,36000)}
 # Format of data is given below :
 # {Empid : (Empname, EmpSalary}


# emp={1:('Amit',25000),2:('Suman',30000),3:('Ravi',36000)}
# a=list(emp.values())
# for i in a:
#     if i[1]>25000:
#         print(i[0])

    




