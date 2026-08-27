import sqlite3
import pandas as pd

#SELECT      -- 1. what columns to show
#FROM        -- 2. which table
#JOIN        -- 3. add another table
#WHERE       -- 4. filter rows
#GROUP BY    -- 5. group rows
#HAVING      -- 4.5 filter after the GROUP BY
#ORDER BY    -- 6. sort results
#LIMIT       -- 7. how many rows

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

query8= """
select player_name, sum(earnings) as total_earnings
from player_winnings
where earnings > (select avg(earnings) from player_winnings)
group by player_name
order by total_earnings desc
limit 20;
"""

results8 = conn.execute(query8).fetchall()
print("Players that Earn More than the Average:")
for row in results8:
    print(f" {row[0]}: ${row[1]:,}")

# Which orgs have the most active players still competing?
# Join on team, outer and count player names selecting team name and player_name
query9 = """
select player_info.team, count(player_name) as total
from org_winnings
join player_info on org_winnings.team = player_info.team
where player_status = 'Active' and player_info.team is not NULL
group by org_winnings.team
order by total desc
limit 10;
"""

results9 = conn.execute(query9).fetchall()
print("Top 10 Orgs with the most Active players")
for row in results9:
    print(f" {row[0]}: {row[1]:,} players")

# For each nationality, who is their highest earning player?
# Player_winnings, go by each nationality and sort by the earnings of the players and select the player_names for each earnings
# Having is for after the group by and p2.nationality= player_winnings.nationality is a way to sort and look specifically between same values within a column
query10= """
select nationality, player_name, sum(earnings) as total_earnings
from player_winnings
group by nationality, player_name
having total_earnings = (
    select max(total)
    from (
        select sum(earnings) as total
        from player_winnings p2
        where p2.nationality = player_winnings.nationality
        group by player_name
        )
)
order by nationality;
"""

results10= conn.execute(query10).fetchall()
print("Top Earning Player in each Nationality:")
for row in results10:
    print(f" {row[0]}: {row[1]}")

conn.close()