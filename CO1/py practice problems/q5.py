n = int(input("Enter a positive integer"))
sum = 0
for i in range(0,n+1):
    if i % 2 == 0:
        sum = sum + (i*i*i)
print(sum)