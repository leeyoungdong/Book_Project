import pandas as pd
import numpy as np

ip_month_grade = pd.read_csv(r"C:\Users\maeve\AIB 14\Section6\Codestates Project 2\data\interpark\interpark_month_grade_202211250151.csv")
ip_month_info = pd.read_csv(r"C:\Users\maeve\AIB 14\Section6\Codestates Project 2\data\interpark\interpark_month_info_202211250151.csv")
ip_month_sales = pd.read_csv(r"C:\Users\maeve\AIB 14\Section6\Codestates Project 2\data\interpark\interpark_month_sales_202211250151.csv")

ip_yr_grade = pd.read_csv(r"C:\Users\maeve\AIB 14\Section6\Codestates Project 2\data\interpark\interpark_year_grade_202211241329.csv")
ip_yr_info = pd.read_csv(r"C:\Users\maeve\AIB 14\Section6\Codestates Project 2\data\interpark\interpark_year_info_202211241329.csv")
ip_yr_sales = pd.read_csv(r"C:\Users\maeve\AIB 14\Section6\Codestates Project 2\data\interpark\interpark_year_sales_202211241329.csv")

# grade
def ip_grade(df):
    df = df.rename(columns={'21': 'ProdNo', '30': 'review'})
    df['review'] = df['review'].str.replace(',','').astype(np.float64)
    df = df.drop_duplicates(keep = 'first')
    
    return df

ip_grade(ip_month_grade)
# ip_grade(ip_yr_grade)


# info
def ip_m_info(df):
    df = df.rename(columns={'3': 'accuCnt', '5': 'aggrCnt', '15': 'author', '51': 'category', '187': 'title', '188': 'ProdNo'})
    df.author = df.author.str.replace('\\','')
    df.author = df.author.str.replace('/','')
    df.category = df.category.str.replace('\\','')
    df.category = df.category.str.replace('/','')
    df['accuCnt'] = df['accuCnt'].str.replace(',','').astype(np.float64)
    df['aggrCnt'] = df['aggrCnt'].str.replace(',','').astype(np.float64)
    df.author = df.author.str.replace("'", "")
    df.author = df.author.str.replace('"', '')
    df.category = df.category.str.replace("'", "")
    df.title = df.title.str.replace("'", "")
    df.title = df.title.str.replace('"', '')
    df.title = df.title.str.replace('\\','')
    df.title = df.title.str.replace(' ','')
    df.ProdNo = df.ProdNo.str.replace('\\','')
    df.ProdNo = df.ProdNo.str.replace(' ','')
    df = df.drop_duplicates(keep = 'first')
    
    return df

ip_m_info(ip_month_info)


def ip_y_info(df):
    df = df.rename(columns={'3': 'accuCnt', '5': 'aggrCnt', '15': 'author', '51': 'category', '186': 'title', '187': 'ProdNo'})
    df.author = df.author.str.replace('\\','')
    df.author = df.author.str.replace('/','')
    df.category = df.category.str.replace('\\','')
    df.category = df.category.str.replace('/','')
    df['accuCnt'] = df['accuCnt'].str.replace(',','').astype(np.int64)
    df['aggrCnt'] = df['aggrCnt'].str.replace(',','').astype(np.int64)
    df.author = df.author.str.replace("'", "")
    df.author = df.author.str.replace('"', '')
    df.category = df.category.str.replace("'", "")
    df.title = df.title.str.replace("'", "")
    df.title = df.title.str.replace('"', '')
    df.title = df.title.str.replace('\\','')
    df.title = df.title.str.replace(' ','')
    df.ProdNo = df.ProdNo.str.replace('\\','')
    df.ProdNo = df.ProdNo.str.replace(' ','')
    df = df.drop_duplicates(keep = 'first') # 27975 - 1530 = 26445
    
    return df

ip_y_info(ip_yr_info)


# sales
def ip_sales(df):
    df = df.rename(columns={'315': '구매력?', '319': 'ProdNo'})
    df['구매력?'] = df['구매력?'].str.replace(',','').astype(np.int64)
    df = df.drop_duplicates(keep = 'first')
    
    return df

ip_sales(ip_month_sales)
# ip_sales(ip_yr_sales)