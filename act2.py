print("half pyramind pattern of stars(num): ")
n = int(input("enter the num of row: "))

num = 1
for i in range(n):
    for j in range(i + 1):
        print(num , end= " ")
        num = num + 1
    print()
