string = input("Enter the string")

for i in string:
    if i in ['a','e','i','o','u']:
        string.replace(i,'*')

print(string)