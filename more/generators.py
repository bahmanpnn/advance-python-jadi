'''
    generators are easy way to create iterable objects(class,dict,list,...)
    
    there are 2 ways to create generator==>func,expression(comprehension)

    one advantage of generators are being lazy evaluation.
    it means data save in memory and does not run till calling!! so it costs lower sources.


'''

#function generator

#usual simple function
def show1():
    return 'hello'
    return 'hello2'

#generator function
def show2():
    yield 'show2_hello'
    yield 'show2_hello2'


print(show1())
print('='*90)

print(show2()) #it show object memory of data
print('='*90)

for i in show2():
    print(i)


print('='*90)

def show3(number):
    print('starting')
    while(number>=1):
        yield number
        number-=1
    
for i in show3(5):
    print(i)


print('='*90)

def show4(number):
    print('starting')
    while(number>=1):
        yield number
        number-=1
    
s=show4(5)
print(next(s))
print(next(s))
print(next(s))

print('='*90)
#expression-comprehension

x=[i for i in range(1,11) if i%2==0] #this is simple list comprehension
print(x)

print('='*90)
y=(i for i in range(1,11) if i%2==0) #this is comprehension
print(y)
print(next(y))
print(next(y))
print('='*90)



###########################################################

#for example we want slice of a comprehension and need first 3 of them.
e=[i for i in range(1,100) if i%2==0]
temp=slice(0,3,1)
print(e[temp])
print('temp is=',temp)

print(e[:3])



print('='*90)
#comprehension shows its power in working with big datas and cost lower sources!!
z=(i for i in range(1,100) if i%2==0)
print(next(z))
print(next(z))
print(next(z))








