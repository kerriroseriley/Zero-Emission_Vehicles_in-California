
# Import modules
import pandas as pd

pd.options.mode.copy_on_write = True


# Load Data

ev_vehicles = pd.read_csv("ZEVs_filtered.csv", dtype={"zip": str})
ev_chargers = pd.read_csv("stations_2020_2025.csv", dtype={"ZIP": str})


# Standardize the column names

ev_vehicles = ev_vehicles.rename(columns={"zip": "zip"})
ev_chargers = ev_chargers.rename(columns={"ZIP": "zip"})


# Clean the Zip Codes

ev_vehicles["zip"] = ev_vehicles["zip"].astype(str).str.strip().str[:5]
ev_chargers["zip"] = ev_chargers["zip"].astype(str).str.strip().str[:5]


# Filter for the year of 2025

ev_vehicles["Year"] = pd.to_numeric(ev_vehicles["Year"], errors="coerce")
ev_chargers["Year"] = pd.to_numeric(ev_chargers["Year"], errors="coerce")

ev_vehicles_2025 = ev_vehicles[ev_vehicles["Year"] == 2025]
ev_chargers_2025 = ev_chargers[ev_chargers["Year"] == 2025]


# Count per zip code

vehicles_per_zip = (
    ev_vehicles_2025
    .groupby("zip")
    .size()
    .reset_index(name="num_vehicles")
)

chargers_per_zip = (
    ev_chargers_2025
    .groupby("zip")
    .size()
    .reset_index(name="num_chargers")
)


# Merge (Outer Join)

ca_data = pd.merge(
    vehicles_per_zip,
    chargers_per_zip,
    on="zip",
    how="outer",
    indicator=True
)


# Fill the missing values

ca_data = ca_data.fillna(0)


# Calculate the Ratio

ca_data["vehicles_per_charger"] = ca_data.apply(
    lambda r: r["num_vehicles"] / r["num_chargers"]
    if r["num_chargers"] > 0 else None,
    axis=1
)


# FLAG VALID ZIP RANGE (like NY example)



ca_data["valid_zip"] = 1  # placeholder


# Save the output

ca_data.to_csv("ev_charger_ratio_2025.csv", index=False)


# Print a Summary 

print("\nFinal dataset:\n", ca_data.head())
print("\nTotal ZIPs:", len(ca_data))
print("\nNon-matching rows (from merge indicator):")
print(ca_data["_merge"].value_counts())