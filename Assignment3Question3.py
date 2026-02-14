import pandas as pd
from sklearn.model_selection import train_test_split


kidneyDiseaseDF = pd.read_csv("kidney_disease.csv") #read the csv from the file.

kidneyDiseaseDF = kidneyDiseaseDF.dropna() #use this to drop rows with NaN values
#this is for question 4 because the confusion matrix cant be done with a matrix that has non-integer values.
binary_map = {"present": 1, "notpresent": 0,"normal": 1, "abnormal": 0,"yes": 1, "no": 0,"good": 1, "poor": 0,"ckd": 1, "notckd": 0}
#a dictionary to replace non-integer values with integers.
#I use 0 for "not" values and 1 for values that are true.
#this is mostly for question 4, since the confusion matrix can't be done if the data frame has non-integer values.
kidneyDiseaseDF.replace(binary_map,inplace=True) #replace all the non-integer values with integers
xLabel = kidneyDiseaseDF.drop(columns = ["classification"]) #set the x label as the matrix without the classification column
yLabel = kidneyDiseaseDF["classification"].astype(int) #set the y label as the column of "classification"

x_train, x_test, y_train, y_test = train_test_split(xLabel,yLabel,test_size=0.3,random_state = 5)
#split the data frame into 70% training data and 30% testing data. the random state is set to a fixed "seed" of 5.

# we should not train and test a model on the same data because it will result in overfitting, where the model
# is too specific for the training data and will not have enough generalization, and it will result in a fake
# high accuracy because the testing data will match the training data exactly.

# the testing set is a subset of the original data provided, it's purpose is to test the model to check how well the model
# can predict new values.
