# This py file is for the wrangle functions of the Pumpkin Season project!#
import pandas as pd


def creating_pumpkin_patch():
    """This function used the USDA pulled csv datasets of pumpkin sales in the 
    U.S. from 2018-2022 and merges each csv together"""
    df = pd.read_csv("pumpkin2020.csv")
    df1 = pd.read_csv("pumpkin2018.csv")
    #mergining together:
    pumpkin_df = pd.concat([df, df1], axis =0)
    df2 = pd.read_csv("pumpkin18.csv")
    df = pd.concat([pumpkin_df, df2], axis = 0)
    return df

def date_index(df):
    """This function takes in your df name of main Pumpkin df
    and sets the date column as dtype datetime and order df chronologically"""
    df['Date']=pd.to_datetime(df['Date'])
    df = df.sort_values(by='Date')
    return df

def drop_col(df):
    """This function drops unneeded columns (due to large nulls)"""
    df = df.drop(columns =['Environment','% Marked Local','Organic'])
    return df


def num_stores(df):
    """This function changes preps the column Number of Stores for dtype change"""
    df['Number of Stores']= df['Number of Stores'].apply(lambda x : x.replace(',',''))
    df['Number of Stores']= df['Number of Stores'].astype(int)
    return df

def last_yr_stores(df):
    """This function preps, fills nulls and changes dtypes the column Last Year Stores
    for exploration of data"""
    df['Last Year\n Stores'] = df['Last Year\n Stores'].astype(str)
    df['Last Year\n Stores'] = df['Last Year\n Stores'].apply(lambda x : x.replace(',',''))
    df['Last Year\n Stores'] = df['Last Year\n Stores'].fillna(value='0')
    return df

def fill_nulls(df):
    """This function fills in NaNs within the various columns of df"""
    df['Variety'] = df[['Variety']].fillna(value='UNKNOWN')
    df['Low Price'] = df[['Low Price']].fillna(value = 0.00)
    df['High Price'] = df[['High Price']].fillna(value = 0.00)
    df['Last Year\n Weighted Avg Price'] = df[['Last Year\n Weighted Avg Price']].fillna(value = 0)
    return df

def main_clean(df):
    """This is the 'momma' wrangle function that combines all the above:"""
    df = creating_pumpkin_patch()
    df = date_index(df)
    df = drop_col(df)
    df = num_stores(df)
    df = last_yr_stores(df)
    df = fill_nulls(df)
    return df


