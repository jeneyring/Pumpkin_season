# This py file is for the wrangle functions of the Pumpkin Season project!#
import pandas as pd


def creating_pumpkin_patch(df):
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



