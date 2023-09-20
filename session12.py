#explore dictionary
my_tuple = ()
print(my_tuple,type(my_tuple))


my_list = []
print(my_list,type(my_list))


my_set = set()
print(my_set,type(my_set))

my_data = {1:"nitin",2:"yuvi",3:"aayush",4:"vikas"}
print(my_data)

print("Min:",min(my_data))

print("Max:",max(my_data))

print("Sum:",sum(my_data))
print(my_data[2])
my_data.pop(2)
print(my_data)
my_data[5] = "mukesh"
print(my_data)
my_data[5] = "rahul"
print("my_data:",my_data)
del my_data[4]
print("my_data:",my_data)

columns = ['ludhiana','faridkot','moga','samrala']
population = {}.fromkeys(columns,1200)
print("population:",population)
population["ludhiana"] = 3100

print("population:",population)
#convert dictionary into list of tuples

items = list(population.items())
print(items)