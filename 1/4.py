'''
4 ==>n 

m.hosSein.python
f.miNa.C
m.aHMad.C++
f.Sara.java

-------------must be this

f Mina C
f Sara java
m Ahmad C++
m Hossein python

'''


n=int(input('give me n= '))

temp_list=[]
for i in range(0,n):
    person=input('give person name= ')
    person=person.split('.')

    person[1]=person[1].capitalize()
    temp_list.append(person)

temp_list=sorted(sorted(temp_list,key=lambda item:item[0]),key=lambda item:item)
# print(temp_list)

for p in temp_list:
    print(p[0],p[1],p[2]) 
