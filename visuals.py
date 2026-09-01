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

results = conn.execute(query1).fetchall()
players = [row[0] for row in results]
earnings = [row[1] for row in results]

plt.figure(figsize=(12,6))
plt.barh(players[::-1], earnings[::-1], color='skyblue')
plt.xlabel('Total Earnings ($)')
plt.title('Top 10 Highest Earning Apex Legends Pro Players')
plt.tight_layout()
plt.show()

# Top Earning Orgs
query2= """
SELECT team, SUM(earnings) as total_earnings
FROM org_winnings
GROUP BY team
ORDER BY total_earnings DESC
LIMIT 10;
"""

results2 = conn.execute(query2).fetchall()
orgs2 = [row[0] for row in results2]
earnings2 = [row[1] for row in results2]

plt.figure(figsize=(12,6))
plt.barh(orgs2[::-1],earnings2[::-1],color='red')
plt.xlabel('Total Earnings ($)')
plt.title('Top 10 Highest Earning Orgs')
plt.tight_layout()
plt.show()

# Annual Earnings between Orgs
# cast(___ as integer) - turn values into integers
query3= """
SELECT cast(year as integer), SUM(earnings) as annual_earnings
FROM org_winnings
GROUP BY year
ORDER by year DESC;
"""

results3 = conn.execute(query3).fetchall()
year3 = [row[0] for row in results3]
earnings3 = [row[1] for row in results3]

plt.figure(figsize=(12,6))
plt.plot(year3[::-1],earnings3[::-1])
plt.xlabel('Year')
plt.ylabel('Earnings ($)')
plt.title('Annual Earnings')
plt.xticks([2019,2020,2021,2022])
plt.ticklabel_format(axis = 'y', style = 'plain')
plt.tight_layout()
plt.show()
