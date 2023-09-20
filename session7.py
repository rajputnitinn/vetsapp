my_data = (10,20,30)
numbers = (
    (10,20,30),
    (40,50,60,70,80),
    (90,99)
)
large_data = (
    (10,20,30),
    (40,50,60,70,80),
    (90,99)
)
(
    (10,20,30),
    (40,50,60,70,80),
    (90,99)
)


# 1. indexing
print(len(my_data))
print(my_data[1])
print(len(numbers))
print(numbers[1])
print(numbers[1][2])

print(large_data[1][2])

print(my_data[-1])
print(numbers[-1])


#slicing
data = list(range(10,101,10))
print("data :",data)
print("data(:5)",data[:5])
print("data(5:9)",data[5:9])
print("data(-5:-2)",data[-5:-2])


 #concatination
data1 = (10,20,30)
data2 = (40,50,30)
data3 = data1 + data2
print("data3:",data3)

#multiplicity

data4 = data1 * 2
print("data4:",data4)

#membership testing
print(10 in data1)
print(100 in data1)


