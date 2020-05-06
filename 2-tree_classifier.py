import numpy as np
import pandas
from sklearn.tree import DecisionTreeClassifier

data = pandas.read_csv('titanic.csv', index_col='PassengerId')
del (data['Name'], data['SibSp'], data['Parch'], data['Ticket'],
     data['Cabin'], data['Embarked'])
data = data.dropna(axis=0)
Survived = data['Survived']
del (data['Survived'])

X = []

# print(data['Pclass'])
for i in data['Pclass']:
    X.append([i])
j = 0
for i in data['Sex']:
    if i == 'male':
        X[j].append(1)
    else:
        X[j].append(0)
    j += 1
j = 0
for i in data['Fare']:
    X[j].append(i)
    j += 1
j = 0
for i in data['Age']:
    X[j].append(i)
    j += 1

# X = np.array([data['Pclass'], data['Sex'], data['Age'], data['Fare']])
# for i in range(0, len(X[1])):
#     if X[1][i] == 'male':
#         X[1][i] = 1
#     else:
#         X[1][i] = 0
y = np.array(Survived)

# print(X)
# print(X[0])
# print(y)
clf = DecisionTreeClassifier(random_state=241)
# clf = DecisionTreeClassifier()
clf.fit(X, y)
imp = clf.feature_importances_
print(imp)
