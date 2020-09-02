3.Write a Python program to test whether a
passed letter is a vowel or not

ch = input(" Enter a Character : ")
if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A'
       or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
    print(ch, "is a Vowel")
else:
    print(ch, "is a not a vowel")