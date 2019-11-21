import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#setup and reading the csv file
customer = pd.read_csv('Mall_Customers.csv')

customer.head()
customer.describe()

#Exploring data
#distributing gender
sns.countplot('Gender', data= customer)
plt.title('Distribution of Gender')

#Histogram of age
customer.hist('Age', bins = 35)
plt.title('Distribution of Age')
plt.xlabel('Age')

plt.hist('Age', data=customer[customer['Gender']== 'Male'], alpha = 0.5, label= 'Male')
plt.hist('Age', data=customer[customer['Gender']== 'Female'], alpha = 0.5, label = 'Female')
plt.title('Distribution of Age by Gender')
plt.xlabel('Age')
plt.legend()

#histogram of income
customer.hist('Annual Income (k$)')
plt.title('Distribution of income')
plt.xlabel('Thousands of dollars')

#distribution of income by gender
plt.hist('Annual Income (k$)', data=customer[customer['Gender']=='Male'], alpha = 0.5, label = 'Male')
plt.hist('Annual Income (k$)', data=customer[customer['Gender']=='Female'], alpha = 0.5, label = 'Female')
plt.title('Distribution of Income by Gender')
plt.xlabel('Income')
plt.legend()

male_customer = customer[customer['Gender']== 'Male']
female_customer = customer[customer['Gender']=='Female']

#printing avg spending score
print(male_customer['Spending Score (1-100)'].mean())
print(female_customer['Spending Score (1-100)'].mean())

#age to annual income
sns.scatterplot('Age', 'Annual Income (k$)', hue='Gender', data=customer)
plt.title('Age to Income, Colored by Gender')

#age to spending score

sns.scatterplot('Age', 'Spending Score (1-100)', hue ='Gender', data=customer)
plt.title('Spending score, Colored by Gender')

#Annual income to spending score
sns.scatterplot('Annual Income (k$)','Spending Score (1-100)', hue='Gender', data=customer)
plt.title('Spending score, Annual income')































