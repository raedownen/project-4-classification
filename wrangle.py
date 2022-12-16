import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

import env

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from scipy import stats


###################################################################################
#################################### ACQUIRE DATA #################################
###################################################################################

#function to go get TEA discipline data from the web
# Annual Summaries for All Districts in the State 2018/19, 2019/20, 2020/21, and 2021/22 School Years

    
    filenames = 'DISTRICT_summary_22.csv', 'DISTRICT_summary_21.csv', 'DISTRICT_summary_20.csv', 'DISTRICT_summary_19.csv'
   
    #else go get the data
    else:
        df = new_telco_data()
        df.to_csv(filename,index=False)
        
    return df

###################################################################################
##################################### PREP DATA ###################################
###################################################################################

def clean_tea(df):
    '''Prepares acquired TEA data for exploration'''
    df = df.rename(columns={'AGGREGATION LEVEL':'agg_level', 'REGION':'region', 'DISTNAME':'dist_name', 'DISTRICT':'district_num', 'CHARTER_STATUS':'charter_status', 'SECTION':'section', 'HEADING':'heading', 'HEADING NAME':'heading_name'})
    df['charter_encoded'] = df.charter_status.map({'OPEN ENROLLMENT CHARTER': 1, 'TRADITIONAL ISD/CSD':0})
    df=df[(df.heading == 'A01') | (df.heading ==  'A03')]
    df19=df19[(df19.YR19 != -999)]
    df.drop_duplicates()
    df.dropna()
    df19pivot=df19.pivot(index='district_num', columns='heading_name', values= 'YR19').dropna()
    df19=df19.drop(columns=['heading', 'heading_name','heading_encoded','YR19'])
    d22=df22.drop_duplicates()
    df=df.merge(dfpivot,how= 'right', on= 'district_num')
    df = df.rename(columns={'DISTRICT CUMULATIVE YEAR END ENROLLMENT': 'enrollment', 'DISTRICT DISCIPLINE RECORD COUNT':'disciplined'})
    df19['discipline_percent']= (df19['disciplined']/df19['enrollment'])*100
    df19=df19.round({'discipline_percent': 0})
    df22.drop_duplicates()
    df= df.drop(columns=['agg_level', 'region', 'district_num', 'section','charter_status'])
    
    
    
    
    
    
    
    
    
    
    df.drop_duplicates(inplace=True)
    df = df[df.total_charges!=' ']
    df.total_charges = df.total_charges.astype(float)
    df['churn_encoded'] = df.churn.map({'Yes': 1, 'No': 0})
    df.drop(columns=['customer_id','payment_type_id', 'internet_service_type_id','contract_type_id', 'churn'], inplace=True)
    
    return df
###################################################################################
#################################### SPLIT DATA ###################################
###################################################################################

#Step 5: Test and train dataset split
def split_tea_data(df):
    '''
    This function performs split on tea data, stratify charter_encoded.
    Returns train, validate, and test dfs.
    '''
    train_validate, test = train_test_split(df, test_size=.2, 
                                        random_state=123, 
                                        stratify=df.charter_encoded)
    train, validate = train_test_split(train_validate, test_size=.3, 
                                   random_state=123, 
                                   stratify=train_validate.charter_encoded)
    return train, validate, test

#train, validate, test= split_tea_data(df) 

