import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#get new merged csv with both files
home = pd.read_csv("home_ownership_data.csv")
loan = pd.read_csv("loan_data.csv")
merged = home.merge(loan, on="member_id")
merged.to_csv("output.csv", index=False)
#fetch datagram of output.csv
output = pd.read_csv("output.csv")
#get the average of all stats by grouping in home ownership type
average = output.groupby(["home_ownership"]).mean()
#only keep the loan amnt column
average = average[["loan_amnt"]]
#load back into output.csv
average.to_csv("output.csv", index=True)
average = pd.read_csv("output.csv")
#graph
print(average)
average.set_index("home_ownership").plot.bar()
plt.xticks(rotation=0)
plt.xlabel("Home ownership")
plt.ylabel("Average loan amount ($)")
plt.title("Average loan amounts per home ownership")
plt.show()
