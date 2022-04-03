import pandas as pd


def fetch_data(cnxn):
    query = 'Select top 10 * From [dbo].[CompanySmallXMLMD5HashNew]'
    print(query)
    df = pd.read_sql(query,cnxn)
    return df