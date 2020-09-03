6.Write a Python program to convert a tuple to a string.
def convertTuple(tup): 
    str =  ''.join(tup) 
    return str
tuple = ('G', 'O', 'O', 'G', 'L', 'E') 
str = convertTuple(tuple) 
print(str) 
