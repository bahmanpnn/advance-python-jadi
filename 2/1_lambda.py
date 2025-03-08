"""

    lambda args:expression.
    sort(key=function:optional).
    map(function,list)->map object.
    filter(function,list)->filter object.

"""

# example 1
# A function that returns the length of the value:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(key=myFunc)
# print(cars)



# example 2 
# A function that returns the 'year' value:
def myFunc(e):
  return e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

cars.sort(key=myFunc)
# print(cars)

# example 3 / lambda + sort
a=[-6,4,2,-2,1,3,2,7,4]
a.sort(key=lambda x:x>=1)
print(a)
print("_"*80)


# example 4 / lambda + sort
a=[(1,2),(4,5),(3,4),(3,2)]
a.sort(key=lambda x:x[1])
print(a)
print("_"*80)


# example 5 lambda + map
my_list=[2,3,4,5,1,0]
my_list=list(map(lambda x:x*2,my_list))
print(my_list)
print("_"*80)


#example 6  / lambda + map
x=56
a="x is bigger than 10" if x>10 else "x is smaller than 10"
print(a)
l=[3,1,41,12,15,17,35,56,11,78]
l=list(map(lambda x:'big' if x<20 else 'small',l))
print(l)
print("_"*80)



# example 7  /  lambda + filter
my_list=[3,1,41,12,15,32,17,35,56,11,78]
my_list=list(filter(lambda x:x%2!=0,my_list))
print(my_list)