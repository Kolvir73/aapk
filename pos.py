import pandas as pd
import sqlite3
from pathlib import Path

Path('pos.db').touch()
conn = sqlite3.connect('pos.db')
c = conn.cursor()

c.execute('''create table if not exists pos_members (uname text, fname text, lname text, addr1 text,
            aadr2 text, city text, state text, zip text, country text''')

members = pd.read_csv('pos.csv')
members.to_sql('pos_members', conn, if_exists='append', index=False)
