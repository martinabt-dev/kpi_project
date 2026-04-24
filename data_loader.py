import pandas as pd

def load_data():
    # import csv files as df
    retailers_df = pd.read_csv('raw/retailers.csv', decimal=',')
    methods_df = pd.read_csv('raw/methods.csv', decimal=',')
    daily_sales_df = pd.read_csv('raw/daily_sales.csv', decimal=',')
    products_df = pd.read_csv('raw/products.csv', decimal=',')

    # Merge to a big df
    goexplore_df = daily_sales_df.merge(retailers_df, on='Retailer code', how='left')
    goexplore_df = goexplore_df.merge(methods_df, on='Order method code', how='left')
    goexplore_df = goexplore_df.merge(products_df, on='Product number', how='left')
    goexplore_df['Date'] = pd.to_datetime(goexplore_df['Date'], dayfirst=True)
    goexplore_df["revenue"] = goexplore_df["Quantity"] * goexplore_df["Unit sale price"]
    goexplore_df["profit"] = (goexplore_df["Unit price_x"] - goexplore_df["Unit sale price"]) * goexplore_df["Quantity"]
    return goexplore_df