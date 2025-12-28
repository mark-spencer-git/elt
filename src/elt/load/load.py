def load(con, df):
    df.to_sql('your_table', con=con, if_exists='append', index=False)