from sklearn.metrics import confusion_matrix, accuracy_score, f1_score, precision_score, recall_score
from sklearn.neighbors import KNeighborsClassifier


from Assignment3Question3 import x_test, x_train, y_train, y_test

knn_model = KNeighborsClassifier(n_neighbors=5)
#set an n_neighbors as 5, it looks for the nearest 5 neighboring points to consider
knn_model.fit(x_train,y_train)
#trains the model using the training data from x and y train.

y_pred = knn_model.predict(x_test) #predicts labels for the test features using the trained model
print(f"Confusion matrix: \n{confusion_matrix(y_test,y_pred)}") #calculate the confusion matrix with confusion_matrix() to check TP,TN,FP,FN
print(f"Accuracy: \n{accuracy_score(y_test,y_pred)}") #calculate the accuracy based off of the test data and the predicted data
print(f"Precision: \n{precision_score(y_test,y_pred)}") #calculate the precision of the tests.
print(f"Recall: \n{recall_score(y_test,y_pred)}") #calculate the recall scores
print(f"F1-score: \n{f1_score(y_test,y_pred)}") #calculate the f1_scores.

# true positive means that a prediction was made that the person had kidney disease and they did have kidney disease
# true negative means that a prediction was made that the person did not have kidney disease and they did not have kidney disease
# false positive means that a prediction was made that a person had kidney disease but they did not have it.
# false negative means that a prediction was made that a person did not have kidney disease but they had it.

# accuracy alone is not enough to evaluate a classification model because of factors such as:
# 1) majority classes where the model can predict a single thing every single time and get a high accuracy,
#       such as predicting that a person does not have a rare disease, and because it is rare it will almost always be correct.
# 2) overfitting where the model is very accurate when it is fed testing data that is the same as the training data.

# Recall is the most important metric if missing a kidney disease case iss very serious because it focuses on minimizing False negatives,
# it calculates how many positive cases were identified.