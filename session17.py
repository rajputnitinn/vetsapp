#strings are immutable
names = "nitin,yuvi,aayus,vikas"
print("names:",names)
upper_case_names = names.upper()
print("names now:",names)
print("upper_case_numbers now:",upper_case_names)

s1 = names.capitalize()
quote = "be exceptional. have a good day."
s2 = quote.title()
s3 = names.swapcase()
s4 = names.replace('n','aa')
print("s1:",s1)
print("s2:",s2)
print("s3:",s3)
print("s4:",s4)

password = input("Enter Your Password: ")
print("Password:", password.strip())

data = '000000033344362'
print("data:",data.strip('0'))

number = 5.57150007686675555
number = float(str(number).strip('5'))
print(number,type(number))
message = "No Internet Connectivity"
print(message.center(120))
print(message.ljust(120))
print(message.rjust(120))
print(message)