# Titanic Manual Attemp

import pandas as pd

# Read as a CSV input
dataFrame = pd.read_csv("E:/DataScience/1.Titanic/train.csv")

# Reads the count of features (total cell = 891 samples * 12 features)
dataFrame.size

# Statistics of the data (892 samples each having 12 features)
dataFrame.shape

# Powerful to look at each column type, nullability, missing records
dataFrame.info()

print(dataFrame[0:1])

print(dataFrame["PassengerId"])
print(dataFrame["Survived"])

# Access multiple columns efficiently
columns = ['Pclass','Sex','Age','Embarked']
dataFrame[columns]

# Access Rows
dataFrame[0:2]
dataFrame[:5]
dataFrame[880:]

# Access Columns and Rows
dataFrame.loc[0:2,columns]

# To see a specific row values
dataFrame.loc[1,columns]

dataFrame.Sex == 'Female'

dataFrame.iloc[dataFrame.Sex == 'Male',3]
dataFrame.iloc[dataFrame.Sex == 'Female',3]

titanic_train = pd.read_csv("E:/DataScience/1.Titanic/train.csv")

# Looking for a specific cel giving row condition and column names
titanic_train.iloc[0,1]

# access samples based on condition
titanic_train.loc[titanic_train['Survived']== 1,'Pclass']
titanic_train.loc[titanic_train.Survived== 1,'Pclass']
