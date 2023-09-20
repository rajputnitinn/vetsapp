# args and kwargs
def add(*args):
    print(args)
    print(type(args))
add(10 , 20 ,30 ,40 )


def employee_details(**kwargs):
    print(kwargs)
    print(type(kwargs))
employee_details(Name = "Nitin", Age = 20 , Gender = "Male")

def fun(*args,**kwargs):
    print(args)
    print(kwargs)
fun(10,20,30,"Nitin",age = 20, gender = "Male")




