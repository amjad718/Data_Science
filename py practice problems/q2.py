import sys

string = input("Enter the string to find the number of upper case and lower case letters: \n")
high = 0
low = 0
for i in string:
    if i.isdigit():
        print("Please only enter alphabets!!")
        sys.exit()
    if i.isupper():
        high = high + 1
    if i.islower():
        low = low + 1
        
print("The number of upper case letters is: ",high)
print("The number of lower case letters is: ",low)
            
