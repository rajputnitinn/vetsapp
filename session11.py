#explore set
john_followers = {"john","sia","nitin","vikas","yuvi"}
print("john_followers:",john_followers,type(john_followers))

numbers = list(range(10,101,10))
print("numbers:",numbers, type(numbers))
numbers = set(numbers)
print("numbers now:",numbers,type(numbers))
numbers.add(10)
numbers.add(110)
numbers.add(20)
numbers.add(220)
print("numbers after add:",numbers)

#explore how to remove duplicate numbers from set with help of mathematics

numbers.pop()
numbers.pop()
print("numbers after pop:",numbers)
numbers.discard(40)
print("numbers after discard:",numbers)



john_followers = {"john","sia","nitin","vikas","yuvi"}
yuvi_followers = {"john","sia","nitin"}
jake_followers = {"john","rahul","nitin","vikas","aayush"}
print("john_followers:",john_followers)
print("yuvi_followers:",yuvi_followers)
print("jake_followers:",jake_followers)
followers = john_followers.intersection(jake_followers)
print("followers:",followers)
print("issubset:",yuvi_followers.issubset(john_followers))

print("issuperset:",john_followers.issuperset(yuvi_followers))

A = {1,2,3,4,5,}
B = {4,5,6,7,8}
C = A-B
print("C is:",C)