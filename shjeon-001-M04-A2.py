lists = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print("Enter a number that corresponds to the day of the week:")
index = int(input())
if index < 1 or index > 7:
    print("Please input the numbers ranging (1-7)")
else:
    print(lists[index-1])