from Modules.CleanData import get_data


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

    data.to_sql(table_date,con = engine, index=False, if_exists='replace')
    # CREATE TABLE table_date (
    #     'Symbol','Type','Strike','Open Int','Volume','OI Chg','IV'
    #     ...
    # )
    
    return engine.table_names()
