print("half pyramind pattern of stars(*): ")
n = int(input("enter the num of row: "))

for i in range(n):
    for j in range(i + 1):
        print("* " , end= "")
    print()