"""
Filter Zero Emission Vehicles Registration
Output: ZEVs_filtered.csv
"""

# import modules
import pandas as pd 

# List of CSV files that will be processed year to year
files = [
    "ZEVs_2020.csv",
    "ZEVs_2021.csv",
    "ZEVs_2022.csv",
    "ZEVs_2023.csv",
    "ZEVs_2024.csv",
    "ZEVs_2025.csv",
] 

# Correct fuel types - Defines which fuel types should be kept in data set
keep_fuels = ["Battery Electric", "Hydrogen Fuel Cell"]

# Empty list to store cleaned DataFrames from each file
filtered_dfs = []

# Reads each CSV file into a DataFrame
for file in files:
    df = pd.read_csv(file, low_memory=False)

    # Clean column names 
    df.columns = df.columns.str.strip()

    # Standardize column names - Renaming inconistent column names into standardized ones
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

    # skips file if any required column is missing
    if not all(col in df.columns for col in required_cols):
        print(f"Skipping {file} (missing columns)")
        continue

    # Convert date column to datetime format (invalid calues become NaT)
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    
    # Removes row where data converstion failed
    df = df.dropna(subset=["date"])
    
    #Extract the year from the date column into a new column
    df["Year"] = df["date"].dt.year

    # Filter fuels - only keeps rows where fuel type is Battery Electric or Hydrogen Fuel Cell
    df = df[df["fuel"].isin(keep_fuels)]

    # converts zip column to string and removes extra spaces
    df["zip"] = df["zip"].astype(str).str.strip()
    
    # Remove OOS "Out of State" 
    df = df[df["zip"].str.upper() != "OOS"]


    # Keep only needed columns
    df = df[["zip", "Year", "fuel", "vehicles"]]
    
    # Add cleaned DataFrame to the list
    filtered_dfs.append(df)

# Combine all cleaned data - Merges all yearly DataFrames into one final dataset
final_df = pd.concat(filtered_dfs, ignore_index=True)

# Save output
final_df.to_csv("ZEVs_filtered.csv", index=False)

# print total rows and first few rows of data set
print("Final rows:", len(final_df))
print(final_df.head())