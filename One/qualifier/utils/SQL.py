from Modules.CleanData import get_data

# This function adds a new table to the options database. It uses the the time column from the csv to set the name of the newly added table.
def add_new_table(data):
    # Importing the required libraries and dependencies
    import numpy as np
    import pandas as pd
    import hvplot.pandas
    import sqlalchemy

    table_date = data['Time'].iloc[0] 
    # Create a temporary sqlite database
    
    database_connection_string = 'sqlite:///options.db'
    # Create the database engine
    engine = sqlalchemy.create_engine(
        database_connection_string,
        echo=True
    )
    

    # This is where the csv is added to the options database, with the name table_date variable. 


    data.to_sql(table_date,con = engine, index=False, if_exists='replace')
    # CREATE TABLE table_date (
    #     'Symbol','Type','Strike','Open Int','Volume','OI Chg','IV'
    #     ...
    # )
    
    return engine.table_names()
