import pandas as pd
import sqlite3

# Connect to database
conn = sqlite3.connect('apex.db')

# Load CSVs
orgs = pd.read_csv('apex/winnings_by_org_allYears.csv')
players = pd.read_csv('apex/winnings_by_player_allYears.csv')
player_info = pd.read_csv('apex/player_info.csv')

# Strip stray whitespace from string columns so joins/queries on player_name
# and team don't silently fail due to formatting inconsistencies
for df in (orgs, players, player_info):
    str_cols = df.select_dtypes(include=['object', 'string']).columns
    for col in str_cols:
        df[col] = df[col].str.strip()

# real_name is missing for many players (no public real name on record).
# Leaving it as NaN makes it ambiguous whether that's missing data or a bug,
# so we make the "unknown" case explicit.
player_info['real_name'] = player_info['real_name'].fillna('Unknown')
players['real_name'] = players['real_name'].fillna('Unknown')

# team is missing for players not currently signed to an org. Same idea,
# make that explicit rather than leaving a silent null.
player_info['team'] = player_info['team'].fillna('Free Agent')

# Standardize status casing so filters like player_status = 'Active' are
# reliable even if source data has inconsistent casing (e.g. 'active').
player_info['player_status'] = player_info['player_status'].str.title()

# Drop any exact duplicate rows that may have come from overlapping source
orgs = orgs.drop_duplicates()
players = players.drop_duplicates()
player_info = player_info.drop_duplicates(subset=['player_name'])

# Push to SQLite
orgs.to_sql('org_winnings', conn, if_exists='replace', index=False)
players.to_sql('player_winnings', conn, if_exists='replace', index=False)
player_info.to_sql('player_info', conn, if_exists='replace', index=False)

# Sanity check
print("Tables created:")
for table in conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall():
    print(" -", table[0])

conn.close()
print("Done!")