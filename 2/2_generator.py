"""
    every where that you see yield know it is generator :))
    generator is a function that we dont want to clean from memory after finishes his working.
    1- generators use for everytime that we have big data like long list of items(student or something).
    it helps us to generate every item when we need and doesnt fill system memory at a time.
    2- we dont know how many item have or want like calculating and returning a random number. 
    3- generators usually use for loops like while or for loops that we need.
"""

# example 0
def firstn():
    return 1,2,3

print(firstn())

print("_"*80)

# example 1
# it Stores all the numbers in mempory at a time
for _ in (1,2,3):
    print(_)

print("_"*80)



# example 2
# but it just remember that last yield and give next on in next calling and doesnt store all the data at a time
def first_generator():
    yield 1
    yield 2
    yield 3

for _ in first_generator():
    print(_)

print("_"*80)

# example 3
def firstn(n):
    num=0
    while (num<n):
        yield num
        num+=1

for i in firstn(5):
    print(i)

