def fetch():
    file = open("IPL-Data-2022.csv", "r")
    lines = file.readlines()

    for line in lines:
        yield line

result = fetch()
print("result:", result)

#print(next(result))
#print(next(result))
#print(next(result))
#print(next(result))
#print(next(result))
#print(next(result))
#print(next(result))
#print(next(result))
#print(next(result))
#print(next(result))

#print(next(result, "no more record"))

while True:
    data = next(result, "Nothing")
    print(data)
    if data == "Nothing":
        break