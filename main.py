import numpy as np
import pandas as pd

#Read from the csv file
df=pd.read_csv('items 2016-2019.csv')

#Convert zip codes into integers(otherwise we coulndt handle them)
df['zip_code']=df['zip_code'].astype(int)

#We make the calculations for the sum of the products per zip code and sum of sales per store
calc1=df.groupby(['zip_code']).bottles_sold.sum()
calc2=df.groupby(['store_name']).sale_dollars.sum()

#We ectarct it to a new csv the we will insert into Tableau
df.to_csv('aggregated.csv')
