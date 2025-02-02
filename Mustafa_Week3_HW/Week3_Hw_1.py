"""Perfect number: Perfect number is a positive integer that is equal to the sum of its proper divisors.
 The smallest perfect number is 6, which is the sum of 1, 2, and 3. 
 Some other perfect numbers are 28(1+2+4+7+14=28), 496 and 8128. 
 Write a function that finds perfect numbers between 1 and 1000. 
 Check perfect numbers between 1 and 1000 and find the sum of the 
 perfect numbers using reduce and filter functions."""



a, perfect_nums = 0, []
for i in range (1,1001):
    nums = []
    for a in range(1,i):
        if i%a == 0:
            nums.append(a)
        else:
            continue
    if sum(nums)==i:
        perfect_nums.append(i)
print("1-1000 between perfect number : ",perfect_nums)