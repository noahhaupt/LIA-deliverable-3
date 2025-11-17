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
numeric_variables = ["Prevalence Rate (%)","Incidence Rate (%)","Mortality Rate (%)","Population Affected","Healthcare Access (%)", "Doctors per 1000","Hospital Beds per 1000", "Average Treatment Cost (USD)", "Recovery Rate (%)","DALYs","Improvement in 5 Years (%)","Per Capita Income (USD)", "Education Index", "Urbanization Rate (%)"]

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
    print(data[y].value_counts(normalize = "index"))
    print("Number of unique values: ", data[y].nunique())
    print("Mode: ", data[y].mode())
    print()
    
    
#Part 4 - Univariate graphical EDA    
import seaborn as sns

numerical = ["Prevalence Rate (%)","Incidence Rate (%)","Mortality Rate (%)","Population Affected","Healthcare Access (%)", "Doctors per 1000","Hospital Beds per 1000", "Average Treatment Cost (USD)", "Recovery Rate (%)","DALYs","Improvement in 5 Years (%)","Per Capita Income (USD)", "Education Index", "Urbanization Rate (%)"]
#Year was removed as there is only 1 year (2024).

for variable in numerical:
    sns.displot(data, x = variable, bins=15, hue = "Country", multiple = "stack")
    sns.displot(data, x = variable, bins = 10, hue = "Country", multiple = "dodge")
    sns.displot(data, x = variable, bins = 10, hue = "Country", stat = "density", common_norm = False)
    sns.displot(data, x = variable, kind = "kde", bw_adjust = .2)
    sns.displot(data, x = variable, hue ="Country", kind = "ecdf")
#The graphs were plotted and certain graphs were chosen for each which represent the values properly.
# In the report, 5 numerical variables were described per team member, for a total of 14 plots.

    
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
sns.relplot(data, x="Prevalence Rate (%)", y="Mortality Rate (%)", col="Country")
sns.relplot(data, x="Average Treatment Cost (USD)", y="Recovery Rate (%)", hue="Treatment Type", size="Population Affected", col="Country")

#wrong
sns.relplot(data, x="Year", y="Mortality Rate (%)", kind="line", hue="Country")

sns.lmplot(data, x="Healthcare Access (%)", y="Recovery Rate (%)")


#6.2 Visualizing Categorical data (10 plots)



#6.3 Visualizing bivariate distributions (3 plots)
sns.displot(data, x="Prevalence Rate (%)", y="Average Treatment Cost (USD)", kind="hist", binwidth=(10, .5), cbar=True)
sns.displot(data, x="Healthcare Access (%)", y="Recovery Rate (%)", kind="kde", levels=10, thresh=0.05)
sns.displot(data, x="Doctors per 1000", y="Hospital Beds per 1000", hue="Country", kind="kde")

