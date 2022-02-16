namelist = []
print("How many names are in your list?")
count = int(input())
for i in range(count):
    print("Enter name")
    val = input()
    namelist.append(val)

namelist.sort()
namelist