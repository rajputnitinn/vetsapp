#multi value containers
#list set dictionary
#explore list in python
numbers = list(range(10,101,10))
print("numbers are:",numbers,type(numbers))
numbers.append(30)
numbers.append(77)
numbers.append(95)

print("2.numbers:",numbers)
print("Sum:",sum(numbers))
print("Min:",min(numbers))
print("Max:",max(numbers))
print("Length:",len(numbers))

reverse_numbers = list(reversed(numbers))
print("reverse_numbers:",reverse_numbers)

print("Index of 50 is:",numbers.index(50))

print("count of 30 in numbers is:",numbers.count(30))

data = [70,30,50,90,20]
print("data is:",data)
data.sort()
print("data  in sorted form is:",data)
names = ["john","ana","sia","angel","kim"]
names.sort()
print("names:",names)
print("min:",min(names))
print("max:",max(names))

names.remove("sia")
data.remove(30)

print(names)
print(data)


