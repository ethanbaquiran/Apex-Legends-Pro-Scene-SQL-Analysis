import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect('apex.db')

# Copy and Paste the Queries for the visualizations
# Can also do from queries import results1 but that forces to rerun all queries every time

# Highest Earning players
query1= """
SELECT player_name, SUM(earnings) as total_earnings
FROM player_winnings
GROUP BY player_name
ORDER BY total_earnings DESC
LIMIT 10;
"""

results = conn.execute(query).fetchall()
players = [row[0] for row in results]
earnings = [row[1] for row in results]

plt.figure(figsize=(12,6))
plt.barh(players[::-1], earnings[::-1], color='skyblue')
plt.xlabel('Total Earnings ($)')
plt.title('Top 10 Highest Earning Apex Legends Pro Players')
plt.tight_layout()
plt.show()