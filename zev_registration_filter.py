"""
Filter Zero Emission Vehicles Registration
Output: ZEVs_filtered.csv
"""

import pandas as pd 

files = [
    "ZEVs_2020.csv",
    "ZEVs_2021.csv",
    "ZEVs_2022.csv",
    "ZEVs_2023.csv",
    "ZEVs_2024.csv",
    "ZEVs_2025.csv",
] 

# Correct fuel types
keep_fuels = ["Battery Electric", "Hydrogen Fuel Cell"]

filtered_dfs = []

for file in files:
    df = pd.read_csv(file, low_memory=False)


    # Clean column names FIRST
    df.columns = df.columns.str.strip()


    # Standardize column names
    df = df.rename(columns={
        "ZIP Code": "zip",
        "Zip Code": "zip",
        "zip code": "zip",
        "Fuel Type": "fuel",
        "Fuel": "fuel",
        "fuel type": "fuel",
        "Vehicles": "vehicles",
        "Date": "date"
    }) 

 

    # Make sure required columns exist
    required_cols = ["zip", "fuel", "vehicles", "date"]

    if not all(col in df.columns for col in required_cols):
        print(f"Skipping {file} (missing columns)")
        continue


    # Convert date and extract year

    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.dropna(subset=["date"])
    df["Year"] = df["date"].dt.year


    # Filter fuels (AFTER standardizing)
    df = df[df["fuel"].isin(keep_fuels)]

    # Remove OOS
    df["zip"] = df["zip"].astype(str).str.strip()
    df = df[df["zip"].str.upper() != "OOS"]

    # Keep only needed columns
    df = df[["zip", "Year", "fuel", "vehicles"]]

    filtered_dfs.append(df)


# Combine all cleaned data
final_df = pd.concat(filtered_dfs, ignore_index=True)


# Save output
final_df.to_csv("ZEVs_filtered.csv", index=False)

print("Final rows:", len(final_df))
print(final_df.head())