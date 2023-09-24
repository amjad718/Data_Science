def find_words_with_substring(wordlist, name):
    
    count = 0
    indexes = []
    
    for word in wordlist:
        if name in word:
            count += 1
            indexes.append(word.index(name)+1)
        else:
            indexes.append(0) 
    output_tuple = (count, indexes)
    return output_tuple

wordlist=[]
num = int(input("Enter the number of words"))
for i in range(0,num):
    print("Enter the word ",i+1)
    wordlist.append(input())
name = input("Enter the string")
result = find_words_with_substring(wordlist, name)
print(result)
