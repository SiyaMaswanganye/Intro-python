import numpy as np
import pandas as pd 
from numpy.random import randn
import random

lists = ['Jake', 'Siya', 'Andile']
lists2 = ["Computer Scientist", "Data analyst", "Matriculant"]
dictionary = {'Jake':"Computer Scientist", 'Siya':"Data analyst", 'Andile':"Matriculant"}
arr = np.array(["Computer Scientist", "Data analyst", "Matriculant"])

print(pd.Series(data = lists2))
firstseries = pd.Series(data = lists2, index=lists) #the index is one of the most important parts of a series as the order of the index will be relative to the data 
secondseries = pd.Series([" Employed", " Student", " Unemployed"],["Jake", "Siya", "Andile"])
additionOfSeries = firstseries + secondseries
print(additionOfSeries)
print('addition of series is above')
print( firstseries['Siya'])
print('the first series releasing Siya specifically is above')
print(pd.Series(lists2, lists))
print(pd.Series(arr))
print(pd.Series(arr, lists))
print(pd.Series(dictionary))
random.seed(101) #this is to ensure that  the random numbers are consistent for when we are running the variable randomnumbers 
randomnumber = random.random() #this one will stay consistent because of the seed 
secondrandomnumber = np.random.randn(5) # this will not be as consistent because because numpy is not being accessed unless we use 'np.random.seed(5)'
print('random with seed')
print(secondrandomnumber)
print('second random number')
print(randomnumber)
print('first random number')

#creating a random dataframe

df = pd.DataFrame(randn(5,4),index = "A B C D E".split(),columns= "X Y Z M".split()) # This creates a random number with a 5 x 2 matrix that has horizontal lables with index and column lables respectively
print(df)
print(df['X']) # this will print the specific column of X

df['new'] = df["X"]*2 #This adds oon the dataframe, as long as we define that its in the df dataframe we can add and add calculations  
print(df)
print('with new')

df.drop('new',axis= 1, inplace= True) # This is used to erase a column and the implace is to avoid the need to re-declare it, so the changes will be saved in the memory of df  
print(df)

df.drop('A', axis=0, inplace= True) #this will be used to delete the firstt row of the matrix
print(df)

print(df.loc['B']) #this will print out the rows of the dataframe
print("printing just the row B")

print(df.iloc[0]) #This will fetch the row relative to the location and not the lable, since A was 'dropped' then position 0 will be B 
print("Prints the row relative to the location and not the lable")

print(df.loc['B', 'Z']) # This will provide us with a specific location on the matrix relative to B, Z positions 
print('The value above is an exact location due to two given coordinates')

print(df.loc[['B', 'C'],['X', 'Y']]) #If we want to release a set of columns and rows we can define them as lists of the lables we want to extract
print('This is the release of multiple rows and columns from the dataframe')


print(df)
print(df>0) #This tests which values are meeting the condition set 

print(df[df>0]) #This will release values on the dataframe that meet the condition
print('Which values in the dataframe met the condition set')

print(df[df['X']>0]) # this will release the only row(s) that have met the condition relative to the mentioned column 

print(df[df['Y']>0]['Z']) #This will release the only rows that have met the conditions but also filter out everything else and not "Z"

print(df[df['Y']>0][['Z', 'M']]) #This will release the only rows that have met the conditions but also filter out everything else and not "Z" and "M"

newindex = ' AS, BS, CS, DS'.split() #This is creating anew index
print(newindex)

df['States'] = newindex #This inserts the new index and label them as states
print(df)

df.set_index('States', inplace=True) #This places the index in the right and inplace permanently places it in df
print(df)