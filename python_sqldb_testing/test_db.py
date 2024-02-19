import os
import pandas as pd
import sqlite3
from IPython.display import display

main_dir = os.path.dirname(os.path.dirname(os.path.realpath(__name__)))
database_loc = main_dir+"/data_bases/vilkeen.db"

main_db = sqlite3.connect(database_loc)
#cur = main_db.cursor()

# TEST

main_df = pd.read_sql_query("SELECT * FROM saves", main_db)

display(main_df)

## END TEST

def new_save(save_id, name):
    pass


def test_main():
    pass