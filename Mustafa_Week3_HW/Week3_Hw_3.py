"""alphabetical_order
Write a function that takes an input of different words with hyphen (-) 
in between them and then: sorts the words in alphabetical order, adds 
hyphen icon (-) between them, gives the output of the sorted words. 
Example: Input >>> green-red-yellow-black-white Output >>> black-green-red-white-yellow"""

def alphabetical_order(x):
    x1=x.split("-")
    x1.sort()
    x2="-".join(x1)
    print(x2)
x="green-red-yellow-black-white"
alphabetical_order(x)