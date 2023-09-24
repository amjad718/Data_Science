vowels = "AEIOUaeiou"
string = input("Enter the string")
modified_string=""

for i in string:
    if i in vowels:
        modified_string += '*'
    else:
        modified_string += i
        
print(modified_string)