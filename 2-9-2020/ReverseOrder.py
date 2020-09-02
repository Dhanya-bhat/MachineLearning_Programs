1.Write a Python program which accepts the
user's first and last name and print them in
reverse order with a space between them

firstname = input("Enter first name :")
lastname = input("Enter last name :")
fn = firstname[::-1]
ln = lastname[::-1]  
print (fn,"",ln)
