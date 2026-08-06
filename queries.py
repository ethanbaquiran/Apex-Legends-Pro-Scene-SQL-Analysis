import sqlite3
import pandas as pd

conn = sqlite3.connect('apex.db')

query1= """
SELECT player_name, SUM(earnings) as total_earnings
FROM player_winnings
GROUP BY player_name
ORDER BY total_earnings DESC
LIMIT 10;
"""

results = conn.execute(query1).fetchall()
print("Top 10 Highest Earning Players:")
for row in results:
    print(f" {row[0]}: ${row[1]:,}")

query2= """
SELECT nationality, COUNT(player_name) as total_nations
FROM player_winnings
GROUP BY nationality
ORDER BY total_nations DESC
LIMIT 10;
"""

results2 = conn.execute(query2).fetchall()
print('Top 10 Most Common Nationalities')
for row in results2:
    print(f" {row[0]}: {row[1]:,}")


query3= """
SELECT team, SUM(earnings) as total_earnings
FROM org_winnings
GROUP BY team
ORDER BY total_earnings DESC
LIMIT 10;
"""

results3 = conn.execute(query3).fetchall()
print('Top 10 Most Earning Orgs')
for row in results3:
    print(f" {row[0]}: ${row[1]:,}")


query4= """
SELECT year, SUM(earnings) as annual_earnings
FROM org_winnings
GROUP BY year
ORDER by year DESC;
"""

results4 = conn.execute(query4).fetchall()
print('Annual Earnings')
for row in results4:    
    print(f" {row[0]}: ${row[1]:,}")

query5= """
SELECT player_winnings.player_name, SUM(earnings) as total_earnings
FROM player_winnings
JOIN player_info ON player_winnings.player_name = player_info.player_name
WHERE player_status = 'Active'
GROUP by player_winnings.player_name
ORDER by total_earnings DESC
LIMIT 10;
"""

results5 = conn.execute(query5).fetchall()
print('Top 10 Current Players Earnings')
for row in results5:
    print(f" {row[0]}: ${row[1]:,}")



query6= """
SELECT nationality, AVG(earnings) as national_earnings
FROM player_winnings
GROUP BY nationality
ORDER BY national_earnings desc
LIMIT 10;
"""

results6 = conn.execute(query6).fetchall()
print('Top 10 Highest Earning Nations')
for row in results6:
    print(f" {row[0]}: ${round(row[1],2):,}")


query7= """
select player_info.team, sum(earnings) as total_earnings
from player_winnings 
join player_info on player_winnings.player_name = player_info.player_name
where player_status = 'Active' and player_info.team is not null
group by player_winnings.player_name
order by total_earnings desc
limit 10;
"""
results7 = conn.execute(query7).fetchall()
print("Top 10 Highest Earning Player's Orgs")
for row in results7:
    print(f" {row[0]}: ${row[1]:,}")

conn.close()