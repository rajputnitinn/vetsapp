class Employee:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def show(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Gender:",self.gender)
employee1=Employee(name= "nitin", age= 20, gender= "male")
employee2=Employee(name= "aayush", age= 21, gender= "female")
employee1.show()
print("              ")
employee2.show()