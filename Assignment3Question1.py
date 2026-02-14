import pandas as pd
crimesCommitted = pd.read_csv("crime.csv")
print("the average of the violent crimes per population is:", crimesCommitted["ViolentCrimesPerPop"].mean()) #calculate the average of violent crimes per population using mean()
print("the median of the violent crimes per population is:",crimesCommitted["ViolentCrimesPerPop"].median())#calculate the median of violent crimes per population using median()
print("the standard deviation of the violent crimes per population is: ",crimesCommitted["ViolentCrimesPerPop"].std())#calculate the standard deviation of violent crimes per population using std()
print("the maximum of the violent crimes per population is: ",crimesCommitted["ViolentCrimesPerPop"].max())#calculate the maximum  of violent crimes per population using max()
print("the minimum of the violent crimes per population is: ",crimesCommitted["ViolentCrimesPerPop"].min())#calculate the minimum of violent crimes per population using min()
#the distribution looks to be slightly right skewed because the mean is to the right of the median.
#if there are more extreme values, the mean is affected more because the mean measures the average and actually uses the
#numbers when it is calculated, whereas the median only takes into account number order, and it will always take the
#middle of the numbers, so even if there are very extreme values, the median will not change
