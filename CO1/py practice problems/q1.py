num = int(input("Enter the number"))

def rev(num):
    reverse = 0
    while num != 0:
        rem = num % 10
        reverse = reverse * 10 + rem
        num //= 10
    return reverse

def sumFunc(num):
    new = 0
    while num != 0:
        dig = num % 10
        new = new + dig
        num//=10
    return new

res1 = rev(num)
res2 =sumFunc(num)

print("The reverse of the number is: ",res1)
print("The sum of the number is: ",res2)



