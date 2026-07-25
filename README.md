# Apex Legends Pro Scene SQL Analysis

> Who dominates the Apex Legends pro scene — and is it still the same today?

## Overview
This project uses SQL to analyze professional Apex Legends player and organization earnings data across multiple years. Built with Python and SQLite, the database contains three relational tables covering player winnings, org winnings, and player info. Queries explore top earning players, dominant organizations, nationality breakdowns, and year-over-year prize money trends — all visualized with matplotlib.

## Dataset
Three CSV files loaded into a SQLite database:
- `winnings_by_player_allYears.csv` — player earnings by year and nationality
- `winnings_by_org_allYears.csv` — organization earnings by year
- `player_info.csv` — player details including team and active status

## Tools Used
- Python
- SQLite
- pandas
- matplotlib

## Project Structure
apex-capstone/
├── apex/               # Raw CSV datasets
├── main.py             # Loads CSVs into SQLite database
├── queries.py          # All SQL queries and analysis
├── visuals.py          # Matplotlib visualizations
├── apex.db             # SQLite database
└── README.md

## Key Questions Answered
1. Who are the top 10 highest earning players of all time?
2. Which nationality has the most pro players?
3. Which org has earned the most money all time?
4. How has total prize money grown each year?
5. Which active players have the highest career earnings?
6. Which country has the highest average earnings per player?
7. Which team do the top earning players belong to?
8. Which players earned more than the average?
9. Which orgs have the most active players still competing?
10. For each nationality, who is their highest earning player?

## How to Run
1. Clone the repo
2. Install dependencies: pip install pandas matplotlib
3. Run python main.py to set up the database
4. Run python queries.py to see all query results
5. Run python visuals.py to generate charts

## Key Findings
- TSM is the highest earning org all time with over $576,000 in winnings
- The United States has the most pro players with 370, nearly double Japan in second
- Brazil, Russia, and Thailand round out the top 5 nationalities
