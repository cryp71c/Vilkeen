import os
import sqlite3

main_dir = os.path.dirname(os.path.dirname(os.path.realpath(__name__)))
database_loc = main_dir+"/data_bases/vilkeen.db"

main_db = sqlite3.connect(database_loc)
cur = main_db.cursor()

# TEST

if(int(cur.execute("SELECT COUNT(*) FROM SAVES").fetchall()[0][0])==0):


## END TEST

def new_save(save_id, name):



def test_main():
    if (int(cur.execute("SELECT COUNT(*) FROM SAVES").fetchall()[0][0]) == 0):
        save_id = 1
    else:
        save_id = int(cur.execute("SELECT save_id FROM saves ORDER BY save_id DESC LIMIT 1")) + 1
    name = input()