"""reading_number.py

Write a function that outputs the transcription of an input number 
with two digits. Example: 28---------------->Twenty Eight"""

def reading_number():
    while True:
        x = input("Please enter a two digits number : ")
        print (type(x))
        y = int(x) 
        print (type (y))
        number_for_0_10= ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        number_for_10_20= ["ten", "eleven", "twelve", "thirteen", "forteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
        number_for_20_90= ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninty"]
        if 9<y<20 :
            return print("Your number ", x, "is ---->", number_for_10_20[int(x[1])])
        elif 19<y<100 :
            return print('Your number ', x, "is ---->", number_for_20_90[int(x[0])-2], number_for_0_10[int(x[1])])
        else:
            continue
reading_number()