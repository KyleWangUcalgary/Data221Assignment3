from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
from Assignment3Question3 import x_train, x_test, y_train, y_test

k_value_list = [1,3,5,7,9] #creation of a list to hold all of the k values.
accuracy_result = [] #a list to hold all the accuracy results
for num_neighbors in k_value_list:
    #trains the model for k values of 1,3,5,7,9, this is basically to see which k values
    #results in the most accurate value for training data.
    knn_model = KNeighborsClassifier(n_neighbors=num_neighbors) #sets the k value to the current iterated k value in the 1,3,5,7,9 list.
    knn_model.fit(x_train,y_train) #trains the model using the x_train and y_train data.
    y_pred = knn_model.predict(x_test) #predicts the new x values using the x_test
    accuracy_result.append(accuracy_score(y_test,y_pred)) #calculate how accurate the predictions were and add it to the accuracy_results list

results = pd.DataFrame({"k_values": k_value_list, "Accuracy":accuracy_result})
print(results)
#prints out the accuracy's corresponding to each k values in a data frame


print(f"the k value with the best accuracy result is {k_value_list[accuracy_result.index(max(accuracy_result))]}")
#find the maximum accuracy result, and find what k value it corresponds to, then print the k value.

# A higher k value can result in underfitting with higher bias and lower variance.
# A higher k value results in underfitting because it considers a larger amount of neighbors and takes the average of
# too many points, leading to a very generalized model.

# A lower k value can result in overfitting with smaller bias and higher variance.
# A lower k value results in overfitting because it considers not enough neighbors and becomes very specific to every single
# point, without smoothing anything out because it does not take averages.

