"""
Zero Emissions Vehicles Charger Stations - DATA BUILD STEP
Input: stat_20.csv ... stat_25.csv
Output: stations_2020_2025.csv
"""

import pandas as pd

# -----------------------------
# Input files with years
# -----------------------------
files = {
    "stat_20.csv": 2020,
    "stat_21.csv": 2021,
    "stat_22.csv": 2022,
    "stat_23.csv": 2023,
    "stat_24.csv": 2024,
    "stat_25.csv": 2025
}

dfs = []

# -----------------------------
# Load and tag each year
# -----------------------------
for file, year in files.items():
    df = pd.read_csv(file)
    df["Year"] = year
    dfs.append(df)

# -----------------------------
# Combine all years
# -----------------------------
combined = pd.concat(dfs, ignore_index=True)

# -----------------------------
# Clean + filter
# -----------------------------
combined["State"] = combined["State"].astype(str).str.strip()
combined["Fuel Type Code"] = combined["Fuel Type Code"].astype(str).str.strip().str.upper()

filtered = combined[
    (combined["State"] == "CA") &
    (combined["Fuel Type Code"].isin(["ELEC", "HY"]))
]

# -----------------------------
# Select final columns
# -----------------------------
final_df = filtered[["Year", "Fuel Type Code", "ZIP", "Station Name"]]

# -----------------------------
# Save output
# -----------------------------
final_df.to_csv("stations_2020_2025.csv", index=False)

print("Dataset created: stations_2020_2025.csv")