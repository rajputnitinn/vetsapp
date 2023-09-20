#for each or enhanced for loop
data = list(range(10,101,10))
print("data is:",data)
#for idx in range(len(data)):
#    print(data[idx])

data = set(data)
# element can be any name of your choice
for element in data:
    print(element)

student ={
    "rollno":1,
    "name":"nitin",
    "age":20
}
items = student.items()
for items in items:
    print(items[0],items[1])

print("dictionary keys only...")
keys = student
