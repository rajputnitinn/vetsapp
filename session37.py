# Nested/Local Function

def outer():
    print("This is outer function")

    def inner():
        print("This is inner function")
   # inner()
    return inner

result = outer()
result()