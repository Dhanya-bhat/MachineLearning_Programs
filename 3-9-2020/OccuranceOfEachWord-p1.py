1. Write a Python program to count the occurrences of each
word in a given sentence.
s=input("enter a sentence :").split()
a=list(set(s))

for i in a:

    print(i,"-",s.count(i))

