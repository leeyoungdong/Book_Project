import pandas as pd
import numpy as np
import re
import datetime
from stopword import joongang_stoplist, donga_stoplist, khan_stoplist, chosun_stoplist, hani_stoplist


def donga_new(donga):
    # df = donga.drop([donga.columns[0]], axis=1)
    donga.columns = ['index', '0','date']
    df = donga.drop_duplicates(['0'])
    df_result = pd.DataFrame()

    for i in donga_stoplist:
        result = df[df['0'].str.contains(i,na=False)]
        df_result = pd.concat([df_result,result])
    
    df = pd.merge(df,df_result, how='outer', indicator=True)
    df = df.query('_merge == "left_only"').drop(columns=['_merge'])
    df['date'] = df['date'].apply(lambda x: pd.to_datetime(str(x), format='%Y-%m-%d'))
    df = df.rename(columns={'0':'title'})
    df['company'] = 'donga'
    df = df.drop('index', axis=1)
    return df

def joongang_new(df):
    df.columns = ['index','context','date']
    df['context'] = df['context'].str.strip("\n")
    df = df.drop_duplicates(['context'])
    
    df_result = pd.DataFrame()
    for i in joongang_stoplist:
        result = df[df['context'].str.contains(i)]
        df_result = pd.concat([df_result,result])

    df = pd.merge(df,df_result, how='outer', indicator=True)
    df = df.query('_merge == "left_only"').drop(columns=['_merge'])
    df['date']= df['date'].str.slice(0,10)
    df['date']= pd.to_datetime(df['date'])
    df = df.rename(columns={'context':'title'})
    df['company'] = 'joongang'
    df = df.drop([df.columns[0]], axis=1)
    return df

def hani_new(hani):
    # df = hani.drop([hani.columns[0]], axis=1)
    hani.columns = ['index','category','title','pdate']
    df = hani[['title','pdate','category']]
    df = df.drop_duplicates(['title'])
    
    df_result = pd.DataFrame()
    for i in khan_stoplist:
        result = df[df['title'].str.contains(i,na=False)]
        df_result = pd.concat([df_result,result])

    df = pd.merge(df,df_result, how='outer', indicator=True)
    df = df.query('_merge == "left_only"').drop(columns=['_merge'])
    df['pdate'] = df['pdate'].str.slice(4,14)
    df = df.rename(columns={'pdate':'date'})
    df['company'] = 'hani'
    df = df[['title','date','company','category']]
    return df



def chosun_new(chosun):
    # df = chosun.drop([chosun.columns[0]], axis = 1)
    chosun.columns = ['index','0','date']
    df = chosun.rename(columns={'0':'title'})

    df = df.drop_duplicates(['title'])
    
    df_result = pd.DataFrame()

    for i in chosun_stoplist:
        result = df[df['title'].str.contains(i)]
        df_result = pd.concat([df_result,result])

    df = pd.merge(df, df_result, how='outer', indicator=True)
    df = df.query('_merge == "left_only"').drop(columns=['_merge'])
    df['company'] = 'chosun'
    df = df.drop('index', axis=1)
    return df

def khan_new(df):
    df.columns = ['index','context','date']
    df = df.drop_duplicates(['context'])

    df_result = pd.DataFrame()
    
    for i in hani_stoplist:
        result = df[df['context'].str.contains(i,na=False)]
        df_result = pd.concat([df_result,result])
    
    df = pd.merge(df,df_result, how='outer', indicator=True)
    df = df.query('_merge == "left_only"').drop(columns=['_merge'])
    df['date'] = df['date'].apply(lambda x: pd.to_datetime(str(x), format='%Y-%m-%d'))
    df = df.rename(columns={'context':'title'})
    df['company'] = 'khan'
    df = df.drop([df.columns[0]], axis=1)
    return df