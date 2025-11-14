# -*- coding: utf-8 -*-
import pandas as pd
df = pd.read_csv("Global Health Statistics.csv")

#Part 2 -Preliminary Steps
#Filtering the data:
specific_countries = ["Canada", "USA"]
specific_years = [2024]
data = df[df["Country"].isin(specific_countries) & df["Year"].isin(specific_years)]

print(data.head())
print(data.info())
print(data.describe())
unduplicated_data = data.drop_duplicates()
print(unduplicated_data)
#data and unduplicated_data have the same number of rows and columns, meaning that there are no duplicatet rows in the dataset.


#Part 3 - Univariate Non-Graphical EDA
#Numerical variables
numeric_variables = ["Year","Prevalence Rate (%)","Incidence Rate (%)","Mortality Rate (%)","Population Affected","Healthcare Access (%)", "Doctors per 1000","Hospital Beds per 1000", "Average Treatment Cost (USD)", "Recovery Rate (%)","DALYs","Improvement in 5 Years (%)","Per Capita Income (USD)", "Education Index", "Urbanization Rate (%)"]

for x in numeric_variables:
    print(x,"information:")
    print(data[x].describe())
    print("Median: ", data[x].median())
    print("Mode: ", data[x].mode())
    print("Variance: ", data[x].var())
    print("Skewness: ", data[x].skew())
    print("Kurtosis: ", data[x].kurt())
    print()

#Categorical variables
categorical_variables = ["Country", "Disease Name", "Disease Category", "Gender", "Treatment Type", "Availability of Vaccines/Treatment", "Age Group"]

for y in categorical_variables:
    print(y,"information:")
    print(data[y].value_counts())
    print("Number of unique values: ", data[y].nunique())
    print("Mode: ", data[y].mode())
    print()
    #Proportion???
    
    
#Part 4 - Univariate graphical EDA    
import seaborn as sns
import matplotlib.pyplot as plt

#5 variables
numerical= ["Prevalence Rate (%)","Incidence Rate (%)","Mortality Rate (%)", "Population Affected","Healthcare Access (%)"]


# Histograms
for col in numerical:
    sns.histplot(data[col], bins=15)
    plt.show()

# By Gender
for col in numerical:
    sns.displot(data, x=col, hue="Gender", kind="hist", bins=15)
    plt.show()

# Stacked histogram
for col in numerical:
    sns.histplot(data, x=col, hue="Gender", bins=15, multiple="stack")
    plt.show()

# Dodge bars
for col in numerical:
    sns.histplot(data, x=col, hue="Gender", bins=15, multiple="dodge")
    plt.show()

# Normalized histograms
for col in numerical:
    sns.histplot(data[col], bins=15, stat="probability")
    plt.show()

# KDE
for col in numerical:
    sns.displot(data, x=col, hue="Gender", kind="kde")
    plt.show()

# Emperical cumulative dist
for col in numerical:
    sns.displot(data, x=col, kind="ecdf" )
    plt.show()
    

#5 new variables
numerical = ["Doctors per 1000","Hospital Beds per 1000","Average Treatment Cost (USD)", "Recovery Rate (%)","Per Capita Income (USD)"]    


#Histograms
for col in numerical: 
    sns.histplot(data[col], bins=15)
    plt.show()

#By gender
for col in numerical: 
    sns.displot(data, x=col, hue="Gender", kind="hist", bins=15) 
    plt.show()
    
#Stacked histograms    
for col in numerical: 
    sns.histplot(data, x=col, hue="Gender", bins=15, multiple="stack") 
    plt.show()
    
#Dodge bars
for col in numerical: 
    sns.histplot(data, x=col, hue="Gender", bins=15, multiple="dodge")
    plt.show()
    
#Normalized histograms
for col in numerical:
    sns.histplot(data[col], bins=15, stat="probability") 
    plt.show()
    
#KDE
for col in numerical: 
    sns.displot(data, x=col, kind="kde") 
    plt.show()
    
#Emperical cumulative dist
for col in numerical: 
    sns.displot(data, x=col, kind="ecdf")
    plt.show()
    
    
#5 new variables
numerical= ["Education Index","Urbanization Rate (%)","Improvement in 5 Years (%)", "DALYs","Year"]


#Histograms
for col in numerical: 
    sns.histplot(data[col], bins=15) 
    plt.show()
    
#By gender
for col in numerical:
    sns.displot(data, x=col, hue="Gender", kind="hist", bins=15) 
    plt.show()
    
#Stacked histogram   
for col in numerical: 
    sns.histplot(data, x=col, hue="Gender", bins=15, multiple="stack") 
    plt.show()

#Dodge bars
for col in numerical:
    sns.histplot(data, x=col, hue="Gender", bins=15, multiple="dodge") 
    plt.show()
    
#Normalized histograms
for col in numerical:
    sns.histplot(data[col], bins=15, stat="probability") 
    plt.show()
    
#KDE
for col in numerical: 
    sns.displot(data, x=col, kind="kde") 
    plt.show()
    
#Emperical cumulative dist
for col in numerical: 
    sns.displot(data, x=col, kind="ecdf") 
    plt.show()
    
    
    
#Part 5 - Multivariate Non-Graphical EDA
#a)
#Relationship between country and treatment type
print(pd.crosstab(data["Treatment Type"],data["Country"]))
print()
#Relationship between disease and treatment type
print(pd.crosstab(data["Disease Name"],data["Treatment Type"]))
print()
#Relationship between Gender and disease type
print(pd.crosstab(data["Disease Name"],data["Gender"]))
print()

#b)
print(pd.crosstab(data["Treatment Type"],data["Country"], normalize="index"))
print()
print(pd.crosstab(data["Disease Name"],data["Treatment Type"], normalize="index"))
print()
print(pd.crosstab(data["Disease Name"],data["Gender"], normalize="index"))
print()

#c)
print(pd.crosstab(index = [data["Country"], data["Gender"]], columns = data["Treatment Type"]))
print()

#Part 6 - Multivariate graphical EDA 

#6.1 Visualizing statistical relationships (5 plots)

import seaborn as sns

#Question A: How does Prevalance Rate (%) relate to Mortality Rate (%) in Canada vs USA?
sns.relplot(data=data, x="Prevalence Rate (%)", y="Mortality Rate (%)", col="Country")
plt.show()

#Question B: How do Treatment Type, Population Affected and Country relate to Average Treatment Cost and Recovery Rate?
sns.relplot(data=data, x="Average Treatment Cost (USD)", y="Recovery Rate (%)", hue="Treatment Type", size="Population Affected", col="Country")
plt.show()

#Question C: How has Mortality Rate (%) changed over the years in Canada vs USA?
sns.relplot(data=data, x="Year", y="Mortality Rate (%)", kind="line", hue="Country")
plt.show()

#Question D:
    
#Question E: In Canada, is there a linear relationship between Healthcare Access (%) and Recovery Rate (%)?
sns.lmplot(data=data, x="Healthcare Access (%)", y="Recovery Rate (%)")
plt.show()





#6.3 Visualizing bivariate distributions

# Question A: How do Prevalence Rate (%) and Treatment cost vary together?
sns.displot(data=data, x="Prevalence Rate (%)", y="Average Treatment Cost (USD)", kind="hist", binwidth=(5, 500), cbar=True)
plt.show()

# Question B: What is the smooth density pattern between Healthcare Access (%) and Recovery Rate (%)? 
sns.displot(data=data, x="Healthcare Access (%)", y="Recovery Rate (%)", kind="kde", levels=10, thresh=0.05)
plt.show()

# Question C: How does the joint distribution of Doctors per 1000 vs Hospital Beds per 1000 differ between Canada and USA?
sns.displot(data=data, x="Doctors per 1000", y="Hospital Beds per 1000", hue="Country", kind="kde")
plt.show()

