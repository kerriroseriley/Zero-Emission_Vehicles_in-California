"""
Filtering Zero Emissions Vehicles Charger Stations 
Input: stat_20.csv, stat_21.csv, stat_22.csv, stat_23.csv, stat_24.csv, stat_25.csv
Output: stations_2020_2025.csv
"""

# import modules
import pandas as pd

# Input files
files = {
    "inputs/stat_20.csv": 2020,
    "inputs/stat_21.csv": 2021,
    "inputs/stat_22.csv": 2022,
    "inputs/stat_23.csv": 2023,
    "inputs/stat_24.csv": 2024,
    "inputs/stat_25.csv": 2025
}

# Empty list to store yearly DataFrames
dfs = []

#  Load and tag each year - Reads each CSV file into a DataFrames
for file, year in files.items():
    df = pd.read_csv(file)
    
    # Add a new column indicating the year of the dataset
    df["Year"] = year
    # Stores each yearly DataFrame in a list 
    dfs.append(df)

# Combine all years
# Merges all yearly DataFrames into one large DataFrame
combined = pd.concat(dfs, ignore_index=True)


# Clean and filter - Converts State column to string and removes extra whitespaces
combined["State"] = combined["State"].astype(str).str.strip()

# Standardizes fuel type codes (string, trimmed, uppercase)
combined["Fuel Type Code"] = combined["Fuel Type Code"].astype(str).str.strip().str.upper()

# Filters dataset to california only and electric and hydrogen only (ELEC and HY)
filtered = combined[
    (combined["State"] == "CA") &
    (combined["Fuel Type Code"].isin(["ELEC", "HY"]))
]

# Select columns to be included:
final_df = filtered[["Year", "Fuel Type Code", "ZIP", "Station Name"]]

# Save my output to CSV file
final_df.to_csv("outputs/stations_2020_2025.csv", index=False)

# Confirms creation of output file
print("Dataset created: stations_2020_2025.csv")