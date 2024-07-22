'''
    list comprehension x=[output:for x in sequence/list:condition(optional)]
'''
squares=[]
for i in range(1,11):
    if i%2==0:
        s=i**2
        squares.append(s)

print(squares)
print('='*90)

squares_l=[ i**2 for i in range(1,11) ]
squares_l=[ i**2 for i in range(1,11) if i%2==0 ]
squares_l=[ i**2 for i in range(1,11) if i%2==0 if i>5]
print(squares_l)

print('='*90)

o_e=[(i,'Odd' if i%2!=0 else 'Even' ) for i in range(1,11)]

print(o_e)
print('='*90)
# *************************************************************

l2d=[[1,2],[3,4],[5,6],[5,6]]

l=[two for one in l2d for two in one] 
print(l)