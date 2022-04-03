#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from pandas.io import gbq

# pip install pandas-gbq --user
# pip install google-cloud --user
# pip install --upgrade google-cloud-storage --user

def csv_to_gcp():
    print('Hi, GCP')
    my_data = pd.read_csv('C:\\Users\\ruchinskyo\\OneDrive - Dun and Bradstreet\\Desktop\\Json Test\\df_append.csv')
    print(my_data.head(5))

    my_data['isMarketable'] = my_data['isMarketable'].astype(str) # Bool type to STR
    my_data['isMailUndeliverable'] = my_data['isMailUndeliverable'].astype(str)
    my_data['isTelephoneDisconnected'] = my_data['isTelephoneDisconnected'].astype(str)
    my_data['isDelisted'] = my_data['isDelisted'].astype(str)

    my_data.to_gbq(destination_table='SomeData.df_append', #dataset.any_table_name
                   project_id='pandasproject01',
                   if_exists='replace') #fail/append/replace
    # 4/1AX4XfWjvPEhSFzARuvb-0JmNTJyXEalezjwT3Js5H-HLGz0aRlEtEJ9-d3E

def main():
    csv_to_gcp()

if __name__ == '__main__':
    main()