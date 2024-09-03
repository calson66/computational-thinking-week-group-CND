import os
import pandas as pd

# Check the current working directory (optional)
print(os.getcwd())

# Corrected file path (ensure the file name is included)
file_path = r'D:\UvA-DE\Semester_3\computational-thinking-week-group-CND\challenge_day2\first name and teams.csv'

# Read the CSV file
data = pd.read_csv(file_path)

def solution_station_5(first_name):
    row = data[data['First Name'].str.lower() == first_name.lower()]
    
    if not row.empty:
        return row['Learning Team'].values[0]
    else:
        return "Name not found"

# Example usage
print(get_learning_team("Aya"))
