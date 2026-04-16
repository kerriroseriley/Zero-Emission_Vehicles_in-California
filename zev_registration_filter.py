"""
Filter Zero Emission Vehicles Registration
Inputs: ZEVs_2020.csv, ZEVs_2021.csv, ZEVs_2022.csv, ZEVs_2023.csv, ZEVs_2024.csv, ZEVs_2025.csv
Output: ZEVs_filtered.csv
"""
# Import modules
import pandas as pd

# Input files
files = [
    "inputs/ZEVs_2020.csv",
    "inputs/ZEVs_2021.csv",
    "inputs/ZEVs_2022.csv",
    "inputs/ZEVs_2023.csv",
    "inputs/ZEVs_2024.csv",
    "inputs/ZEVs_2025.csv",
]

# Keep Battery Electric and Hydrogen Fuel Call Fuel Types
keep_fuels = ["Battery Electric", "Hydrogen Fuel Cell"]

filtered_dfs = []

# Process each file
for file in files:
    df = pd.read_csv(file, low_memory=False)

    # Clean column names
    df.columns = df.columns.str.strip()

    # Standardize column names
    df = df.rename(columns={
        "ZIP Code": "zip",
        "Zip Code": "zip",
        "zip code": "zip",
        "Fuel Type": "fuel",
        "Fuel": "fuel",
        "fuel type": "fuel",
        "Vehicles": "vehicles"
    })

    # Check required columns
    required_cols = ["zip", "fuel", "vehicles"]
    if not all(col in df.columns for col in required_cols):
        print(f"Skipping {file} (missing required columns)")
        continue

    # Assign year from filename
    year = file.split("_")[-1].replace(".csv", "")
    df["Year"] = int(year)

    # Clean ZIP Codes
    df["zip"] = df["zip"].astype(str).str.strip().str[:5]

    # Remove invalid ZIPs
    df = df[df["zip"].str.upper() != "OOS"]

    # Clean vehicle count
    df["vehicles"] = pd.to_numeric(df["vehicles"], errors="coerce").fillna(0)

    # Filter fuel type
    df = df[df["fuel"].isin(keep_fuels)]

    # Keep only needed columns
    df = df[["zip", "Year", "fuel", "vehicles"]]

    filtered_dfs.append(df)

# Combine all years
final_df = pd.concat(filtered_dfs, ignore_index=True)

# Save output
final_df.to_csv("outputs/ZEVs_filtered.csv", index=False)

# Debug output
print("Final rows:", len(final_df))
print(final_df.head())

print("\nYear distribution:")
print(final_df["Year"].value_counts().sort_index())

print("\nMax vehicles:")
print(final_df["vehicles"].max())