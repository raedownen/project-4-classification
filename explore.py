import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from scipy import stats


###################################################################################
################################## EXPLORE DATA ###################################
###################################################################################

def split_churn(train):
    '''
    Splits the teclo data into two data frames, one of those who churned
    and one dataframe of those who didn't churn
    '''
    #split data for exploration into a dataframe that shows all info on those who churned
    train_churn = train[train.churn_encoded == 1]

    #and a dataframe that show all info on those who didn't churn
    train_no_churn = train[train.churn_encoded == 0]

    return train_churn, train_no_churn

def churn_percentage(train):
    '''
    Takes in the train data set and returns a pie chart of the percentage
    of customers who churned and who didn't churn.
    '''
    #split data for plotting
    train_churn, train_no_churn = split_churn(train)

    #create the percentages
    values = [len(train_churn.churn_encoded), len(train_no_churn.churn_encoded)] 

    # generate and show pie chart
    plt.style.use('seaborn')
    plt.pie(values, labels=["Churn", "Didn't Churn"] , autopct='%.0f%%', colors=['#ffc3a0', '#c0d6e4'], textprops={'fontsize': 14})
    plt.title('Churned Customers Represent 27% of the Train Data', size=20)
    plt.show()

def tenure_viz(train):
    '''
    Takes in the train data and returns a boxenplot and a histogram
    comparing tenure and churn
    '''
    #split data for plotting histogram
    train_churn, train_no_churn = split_churn(train)

    #set font size
    sns.set(font_scale=1.5)
    #set graph style
    sns.set_style('white')

    #set size of the graphs
    fig, (ax1, ax2) = plt.subplots(1,2, figsize=(20,8))

    #set figure title
    fig.suptitle("Does a customer's tenure affect churn?")

    #plot churn and no churn histogram on top of each other
    sns.histplot(train_no_churn, x='tenure', ax=ax1, binwidth=5, label = "Didn't churn", color='#c0d6e4')
    sns.histplot(train_churn, x='tenure', ax=ax1, binwidth=5, label = "Churned", color='#ffc3a0')
    ax1.set_ylabel(ylabel='Number of customers')
    ax1.set_xlabel(xlabel="Months as a customer (tenure)")
    ax1.legend(loc='upper center', frameon=True)

    #plot boxenplot to compare tenure with churn
    average = train["tenure"].mean()
    sns.boxenplot(data=train, x='churn_encoded', y="tenure", palette='pastel', saturation=1, ax=ax2)
    ax2.set_xlabel(xlabel="Did they churn? \n0 = No, 1 = Yes")
    ax2.set_ylabel(ylabel="Months as a customer (tenure)")
    ax2.axhline(average, ls='--', color='black', label='Average tenure') 
    ax2.legend(loc='upper center', frameon=True)
    plt.show()

def tenure_ttest(train):
    '''
    Takes in train data set and returns ttest results for tenure data
    '''
    #separate train into two groups (churn and no churn) for testing
    train_churn, train_no_churn = split_churn(train)

    #run an independent t-test
    tstat, p = stats.ttest_ind(train_churn.tenure, train_no_churn.tenure, equal_var= False)
    #print results
    print(f"tstat: {tstat:.8}\np-value: {p:.4}")

def monthly_charges_viz(train):
    '''
    Takes in the train data and returns a boxenplot 
    comparing monthly charges and churn
    '''
    
    #split data for plotting
    train_churn, train_no_churn = split_churn(train)

    #set font size
    sns.set(font_scale=1.5)
    #set plot style
    sns.set_style('white')

    #set size of the graphs
    fig, ax = plt.subplots(1,1, figsize=(10,6))

    #plot boxenplot to compare monthly charges with churn
    average = train["monthly_charges"].mean()
    sns.boxenplot(data=train, x='churn_encoded', y="monthly_charges", palette='pastel', saturation=1)
    plt.title("Does a customer's monthly charges affect churn? ")
    plt.axhline(average, ls='--', color='black', label= 'Average Monthly charges') 
    plt.xlabel(xlabel="Did they churn? \n0 = No, 1 = Yes")
    plt.ylabel(ylabel="Monthly Charges")
    plt.legend(loc='upper center', frameon=True)
    plt.show()

def monthly_charges_ttest(train):
    '''
    Takes in train data set and returns ttest results for monthly charges
    '''
    #separate train into two groups (churn and no churn) for testing
    train_churn, train_no_churn = split_churn(train)

    #run an independent t-test
    tstat, p = stats.ttest_ind(train_churn.monthly_charges, train_no_churn.monthly_charges, equal_var= False)
    #print results
    print(f"tstat: {tstat:.6}\np-value: {p:.6}")

def contract_type_viz(train):
    '''
    Takes in the train data and returns a bar plot comparing contract type and churn
    '''
    #set font size
    sns.set(font_scale=1.5)
    #set plot style
    sns.set_style('white')

    #set size of the graphs
    fig, ax = plt.subplots(1,1, figsize=(10,6))

    #plot bar plot to compare contract type with churn
    sns.barplot(x="contract_type", y="churn_encoded", data=train, palette='pastel')
    rate = train["churn_encoded"].mean()
    plt.axhline(rate, label = f'Average churn rate', linestyle='--', color='black')
    plt.title("Does a customer's contract type affect churn? ")
    plt.xlabel(xlabel="Contract Type")
    plt.ylabel(ylabel="Churn Rate")
    plt.legend(frameon=True)
    plt.show()

def contract_type_chi(train):
    '''
    Takes in train data set and returns chi-square results comparing
    contract type and churn
    '''
    #create crosstab of the two variables (contract_type and churn)
    observed = pd.crosstab(train["contract_type"], train["churn_encoded"])

    #run χ^2 test
    chi2, p, degf, expected = stats.chi2_contingency(observed)
    print(f"χ^2: {chi2:.6}\np-value: {p:.6}")

def tech_support_viz(train):
    '''
    Takes in the train data and returns a bar plot comparing tech support and churn
    '''
    #set font size
    sns.set(font_scale=1.5)
    #set plot style
    sns.set_style('white')

    #set size of the graphs
    fig, ax = plt.subplots(1,1, figsize=(10,6))

    #plot bar plot to compare tech support with churn
    sns.barplot(x="tech_support", y="churn_encoded", data=train, palette='pastel')
    rate = train["churn_encoded"].mean()
    plt.axhline(rate, label = f'Average churn rate', linestyle='--', color='black')
    plt.title("Does whether a customer has or doesn't have tech support affect churn? ")
    plt.xlabel(xlabel="Tech Support")
    plt.ylabel(ylabel="Churn Rate")
    plt.legend(frameon=True)
    plt.show()

def tech_support_chi(train):
    '''
    Takes in train data set and returns chi-square results comparing
    tech support and churn
    '''
    #create crosstab of the two variables (contract_type and churn)
    observed = pd.crosstab(train["tech_support"], train["churn_encoded"])

    #run χ^2 test
    chi2, p, degf, expected = stats.chi2_contingency(observed)
    print(f"χ^2: {chi2:.6}\np-value: {p:.6}")