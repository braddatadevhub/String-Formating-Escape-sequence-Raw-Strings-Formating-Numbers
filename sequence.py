What is string formating important?
old styling
str.format()
Escape sequence
Raw string
formating numbers



name = "Brad"
age = 30
ratio = 0.25

#2
# print("My name is "+ name +" and I am "+ str(age) +" years old.")

# %s
# %d
# %f

#print("My name is %s and I am %d years old with %.1f percentage"%(name, age, ratio))

#3
#print("My name is {n} and I am {a} years old with {r} percentage".format(n=name, a=age, r=ratio))

#4
# "\t", "\\", "\'", "\"", "\b", "

# print(f'Name\'s: {name}\nAge: {age}\nratio: {ratio}\nStatus:\tSubscribed') 

# print(r'C:/Users/IVY/AppData/Local/Programs/Python/Python314/python.exe')

#padding numbers

# print("{:10}".format(age))

print("Octal: {:o}".format(age))
   