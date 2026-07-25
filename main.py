import pandas as pd
import sqlite3

# Connect to database
conn = sqlite3.connect('apex.db')

# Load CSVs
orgs = pd.read_csv('apex/winnings_by_org_allYears.csv')
players = pd.read_csv('apex/winnings_by_player_allYears.csv')
player_info = pd.read_csv('apex/player_info.csv')

# Drop messy columns
player_info = player_info.drop(columns=['links'])

# Push to SQLite
orgs.to_sql('org_winnings', conn, if_exists='replace', index=False)
players.to_sql('player_winnings', conn, if_exists='replace', index=False)
player_info.to_sql('player_info', conn, if_exists='replace', index=False)

print("Tables created:")
for table in conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall():
    print(" -", table[0])

conn.close()
print("Done!")