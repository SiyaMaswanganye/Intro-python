import numpy as np
# to make all comments we select all, then backslash "/"
lists = ["siya", 3.676, True ]
print(lists)
print(type(lists))
lists.extend(["jake", 3.14])
print(lists)
lists.append("Andile") #this is used to add only one item onto the list rather, and to add more you'd have to create list inside the list
tuples = ("siya", 3.32)
print(tuples)
print(type(tuples))

vectors = {"Kings", 3.32, "Kings", None}
print(vectors)
print(type(vectors))
print(type(None))

#Dictionaries
LetsGoDict = {"Aglet":"Tip of a lace", "Jake": "Hoe", "Siya": "Always a victim"}
print(LetsGoDict)
print(type(LetsGoDict["Jake"])) # calling a single key from the dictionary
for k in ["Jake", "Aglet"]:#calling multiple things in a dictionary (redundent)
    print(LetsGoDict[k])

LetsGoDict["Money"]="Always getting chopped" # Adding to thr dictionary
print(LetsGoDict)

#Array, Vectors and Matrices 

onebythree = [1, 3, 5] # matric of 1 by 3 , these are vectors 
threebyone = [[1],  #matric of 3 by 1 [[1],[3],[5]] also works as the 3 by 1, these are vectors 
              [3],
              [5]]
aonebythree = np.array(onebythree) # have to create a array for our matrix to be able to act as matrices rather than lists 
athreebyone = np.array(threebyone)
 
matrixmultiplication = aonebythree * athreebyone #any other mathematical function that can be applied to matrices 
print(matrixmultiplication)
matrixdivision = aonebythree/athreebyone
print(matrixdivision)
#inverting both fuctions 
invertedmatrix = athreebyone.reshape((1,3))*aonebythree.reshape((3,1)) # .reshape is used to change the shape of an existing matrix
print(invertedmatrix)

experiment01 = np.dot(aonebythree,athreebyone) #dot product which will convert equal lengthed sequences to a scalar 
print(experiment01)

Lists1 = [[2, 4], # this is a 2 by 2 list, this still has to be converted into a matix via array to use complex operations(multiplication)
            [6, 8]]
Lists2 = [[3, 6], [9,12]]
Matrices1 = np.array(Lists1) #iitialising matrices from lists 
Matrices2 = np.array(Lists2)

newlistcaculation = Lists1 + Lists2 # this shows that this is a list
print(newlistcaculation)
newmatrixcalculation = Matrices1 + Matrices2
print(np.add(Matrices1,Matrices2)) #This is a shorter way of adding matrices np.subtract, np.multiply, np.divide can also be used
print(newmatrixcalculation)

print(newlistcaculation[2]) # this will call the point 3,6
print(newlistcaculation[2][0]) # this will call 3 specifically

matrix5 = np.array([1, 2, 3
                    ,4, 5, 6,
                    7, 8, 9]).reshape((3, 3))

RandomlyGenerateNumbers = np.random.randint(20, size = (3,3)) #there's randfloat, randstr, and np.random.rand...(max numbere, size = ...)
print(RandomlyGenerateNumbers)

def Newfunction (a, b): #definition of the function is declared by 'def'
    return a + b  #This is necesary to define what we want from the function, and we do not need to def a + b to a variable since it is professionaly not adviced 
exampleofapplication = Newfunction(3,5) #these are necessary to show the use of the function and the print is just for visual purposes 
print(exampleofapplication) #this is just to see what the results are...

#These are lambda functions, Lambda functions are particularly useful when you need a quick function for a short period and don't want to formally define a complete function.

lambdavariable = lambda a, b, c: a * b ** c #This is the shorter way of writing the general function # b**c is b to the power of c, this is used for easy operations 
print(lambdavariable(5,3,2))  #Lambda functions are particularly useful when you need a quick function for a short period and don't want to formally define a complete function.

print((lambda a, b, c: a * b ** c)(* (4,3,2))) # this is the best way of writing a lambda function since it's of no perfect use since it's used for just defining a function quickly


primes = [2, 3, 5, 7]
sprimes=[]
for p in primes:
    sprimes.extend([p**2])


