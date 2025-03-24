"""
    https://scikit-learn.org/

"""


from sklearn import tree
import csv
# import os
# print(os.getcwd())

x=[]
y=[]


with open('5/data.csv','r') as csv_file:
    data=csv.reader(csv_file)
    next(data) # pass first row with next method because row[0] is column names.
    
    for row in data:
        # x.append(float(i) for i in row[0:3])
        x.append(row[0:3]) # height,weight,shoe size
        y.append(row[3]) # gender

    # print(x[0])
    # print(y[0])

    # print(x[1])
    # print(y[1])

clf=tree.DecisionTreeClassifier()
clf=clf.fit(x,y)


new_data=[[190,89,43],[160,56,39]]
answer=clf.predict(new_data)

print(answer[0])
print(answer[1])