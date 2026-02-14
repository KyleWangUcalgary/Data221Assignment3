import pandas as pd
import matplotlib.pyplot as plt
crimesCommitted = pd.read_csv("crime.csv") #read the csv file

plt.figure(figsize = (8,8)) #set the figure size of the histogram to 8 inches wide and 8 inches high
plt.hist(crimesCommitted["ViolentCrimesPerPop"]) #make a histogram based off of the violent crimes per population column of the chart
plt.title("distribution of violent crimes committed per population") #set the histogram title
plt.xlabel("violent crimes per pop") #set the histogram x-axis label
plt.ylabel("frequency") #set the histogram y-axis label
plt.show() #display the histogram

plt.figure(figsize = (8,8)) #set the figure size of the boxplot to 8 inches wide and 8 inches high
plt.boxplot(crimesCommitted["ViolentCrimesPerPop"]) #make a histogram based off of the violent crimes per population column of the chart
plt.title("box plot of violent crimes committed per population") #set a box plot title
plt.xlabel("violent crimes per pop") #set the label for the x-axis in the boxplot
plt.ylabel("values") #set a label for the y-axis.
plt.show() #display the boxplot


#the histogram shows that the data is right skewed as the mean and median suggested from question 1.

#the box plot shows that the median is around 0.4.

#the box plot suggests because there are no individual points outside the whiskers.

