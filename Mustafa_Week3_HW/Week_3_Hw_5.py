"""equal_reverse.py 
Write a function that controls the given inputs whether 
they are equal to their reversed order or not. 
Example: Input >>> madam, tacocat, utrecht Output >>> True, True, False"""

def equal_reverse(x):
    x1=[]
    x2=[]
    x1=[i for i in x]
    le=len(x1)
    x2=x1[le::-1]
    st1 = str(x1[:])
    st2 = str(x2[:])
    if st1==st2:
        return print(st1, "inverse of the word", st2,"True")
    else:
        return print(st1, "inverse of the word", st2,"False")
x=input('enter the word:')
equal_reverse(x)