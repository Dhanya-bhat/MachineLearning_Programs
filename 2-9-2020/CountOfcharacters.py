5. Write a Python program to count the number of
characters (character frequency) in a string.

test_str = input("Enter the string :")
all_freq = {} 
for i in test_str: 
    if i in all_freq: 
        all_freq[i] += 1
    else: 
        all_freq[i] = 1
print ("Count of all characters is :\n "+  str(all_freq))