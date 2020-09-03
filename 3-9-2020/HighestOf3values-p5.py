5.Write a Python program to find the highest 3 values in a
dictionary.
from collections import Counter
my_dict = {'elston': 30, 'winston': 40, 'alsten': 60, 'royston': 50, 'joyston': 20}
k = Counter(my_dict)
high = k.most_common(3)
print("Dictionary with 3 highest values are :")
print("Keys: Values")
for i in high:
   print(i[0]," :",i[1]," ")