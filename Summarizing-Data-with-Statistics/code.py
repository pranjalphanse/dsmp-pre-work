# --------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#path of the data file- path
#Code starts here 

#Reading of the file
data=pd.read_csv(path)

#Replacing '-'' in the column with 'Agender'
data['Gender'].replace('-','Agender', inplace=True)

#Storing the value counts of 'Gender'
gender_count=data['Gender'].value_counts()

#Plotting bar graph of 'gender_count'
plt.bar(gender_count.index, gender_count)
plt.show()

#Code ends here


# --------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Code starts here
alignment = data['Alignment'].value_counts()
plt.bar(alignment.index, alignment)
plt.show()
plt.plot(label='Character Alignment')


# --------------
#Code starts here
sc_df = data[['Strength', 'Combat']].copy()
sc_covariance=sc_df.cov().iloc[0,1]
sc_strength=sc_df.Strength.std()
sc_combat=sc_df.Combat.std()
sc_pearson = sc_covariance/(sc_strength*sc_combat)
print("Pearson's Correlation Coefficient : ", sc_pearson)

ic_df = data[['Intelligence', 'Combat']].copy()
ic_covariance=ic_df.cov().iloc[0,1]
ic_intelligence=ic_df.Intelligence.std()
ic_combat=ic_df.Combat.std()
ic_pearson = ic_covariance/(ic_intelligence*ic_combat)
print("Pearson's Correlation Coefficient : ", ic_pearson)


# --------------
#Code starts here

#Find the quantile=0.99 value of 'Total' column
total_high= data['Total'].quantile(q=0.99)

#Subsetting the dataframe based on 'total_high' 
super_best=data[data['Total']>total_high]

#Creating a list of 'Name' associated with the 'super_best' dataframe
super_best_names=list(super_best['Name'])

#Printing the names
print(super_best_names)

#Code ends here


# --------------
#Code starts here
f, (ax_1, ax_2, ax_3) = plt.subplots(3, sharex=True, sharey=True)
ax_1.set_title("Intelligence")
plt.boxplot(data['Intelligence'])
plt.show()

ax_2.set_title("Speed")
plt.boxplot(data['Speed'])
plt.show()

ax_3.set_title("Power")
plt.boxplot(data['Power'])
plt.show()




