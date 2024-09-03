import os
import pandas as pd

# Check the current working directory (optional)
print(os.getcwd())

# Read the CSV file
data = pd.read_csv('first_name_and_teams.csv')

def solution_station_5(first_name):
    row = data[data['First Name'].str.lower() == first_name.lower()]
    
    if not row.empty:
        return row['Learning Team'].values[0]
    else:
        return "Name not found"

