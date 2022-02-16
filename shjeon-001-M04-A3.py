print("Please input number one:")
num1 = int(input())
print("Please input number two:")
num2 = int(input())
print("Please input number three:")
num3 = int(input())

if num1 < num2 and num2 < num3:
    print("Numbers are increasing")
elif num1 > num2 and num2 > num3:
    print("Numbers are decreasing")
else:
    print("Numbers are neither increasing nor decreasing")