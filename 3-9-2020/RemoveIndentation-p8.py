8.Write a Python program to remove existing indentation
from all of the lines in a given text.

import textwrap
sample_text = '''
    The orange is the fruit of various citrus species in the family Rutaceae 
    see list of plants known as orange,it primarily refers to Citrus × sinensis, 
    which is also called sweet orange, to distinguish it from the related Citrus × aurantium,
    referred to as bitter orange. 
    '''
text_without_Indentation = textwrap.dedent(sample_text)
print()
print(text_without_Indentation )
print()