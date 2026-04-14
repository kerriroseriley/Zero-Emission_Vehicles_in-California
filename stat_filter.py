"""
Zero Emissions Vehicles Charger Stations Analysis
Output: stations_2020_2025.csv
"""
 
# Import required modules
import pandas as pd 

files = {
    "stat_20.csv": 2020,
    "stat_21.csv": 2021,
    "stat_22.csv": 2022,
    "stat_23.csv": 2023,
    "stat_24.csv": 2024,
    "stat_25.csv": 2025
}

dfs = [] 

for file, year in files.items():
    df = pd.read_csv(file)
    df["Year"] = year
    dfs.append(df)

# Combine all years
combined = pd.concat(dfs, ignore_index=True)

# Filter for California and fuel types ELEC and HY
filtered = combined[
    (combined["State"] == "CA") &
    (combined["Fuel Type Code"].isin(["ELEC", "HY"]))
]

# Select only required columns
final_df = filtered[["Year", "Fuel Type Code","ZIP", "Station Name"]]

# Save to CSV
final_df.to_csv("stations_2020_2025.csv", index=False)