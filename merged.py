"""
Merging ZEV Stations and Registrations and Ratio Function
Inputs: ZEVs_filtered.csv, stations_2020_2025.csv
Outputs: ELEC_ratio.csv, HY_ratio.csv
"""

# Import modules
import pandas as pd

# Load the data
zev_vehicles = pd.read_csv("outputs/ZEVs_filtered.csv", dtype={"zip": str})
zev_stations = pd.read_csv("outputs/stations_2020_2025.csv", dtype={"ZIP": str})

# Standardize the column names
zev_vehicles = zev_vehicles.rename(columns={"ZIP": "zip"})
zev_stations = zev_stations.rename(columns={"ZIP": "zip"})

# Clean the ZIP codes
zev_vehicles["zip"] = zev_vehicles["zip"].astype(str).str.strip().str[:5]
zev_stations["zip"] = zev_stations["zip"].astype(str).str.strip().str[:5]

# Clean the numeric fields
zev_vehicles["vehicles"] = pd.to_numeric(zev_vehicles["vehicles"], errors="coerce")

# Filter to the Year 2025
zev_vehicles["Year"] = zev_vehicles["Year"].astype(str).str.strip()
zev_stations["Year"] = zev_stations["Year"].astype(str).str.strip()

vehicles_2025 = zev_vehicles[zev_vehicles["Year"] == "2025"]
stations_2025 = zev_stations[zev_stations["Year"] == "2025"]

# Split the fuel types
ev_vehicles = vehicles_2025[
    vehicles_2025["fuel"].str.contains("Battery Electric", case=False, na=False)
]

hydrogen_vehicles = vehicles_2025[
    vehicles_2025["fuel"].str.contains("Hydrogen Fuel Cell", case=False, na=False)
]

# ZIP-level vehicle data (NO SUM because already aggregated)
ev_vehicle_zip = (
    ev_vehicles
    .groupby("zip", as_index=False)
    .agg({"vehicles": "sum"})
    .rename(columns={"vehicles": "num_ev_vehicles"})
)

h2_vehicle_zip = (
    hydrogen_vehicles
    .groupby("zip", as_index=False)
    .agg({"vehicles": "sum"})
    .rename(columns={"vehicles": "num_h2_vehicles"})
)


# Station counts per ZIP
ev_stations = stations_2025[stations_2025["Fuel Type Code"] == "ELEC"]
h2_stations = stations_2025[stations_2025["Fuel Type Code"] == "HY"]

ev_station_zip = (
    ev_stations.groupby("zip")
    .size()
    .reset_index(name="num_ev_stations")
)

h2_station_zip = (
    h2_stations.groupby("zip")
    .size()
    .reset_index(name="num_h2_stations")
)


# Merge + rati Function
def merge_and_ratio(v, s, vcol, scol, ratio_col):
    df = pd.merge(v, s, on="zip", how="outer")

    # Fill only numeric columns (NOT whole dataframe)
    df[[vcol, scol]] = df[[vcol, scol]].fillna(0)

    # Compute ratio safely
    df[ratio_col] = df.apply(
        lambda r: r[vcol] / r[scol] if r[scol] > 0 else None,
        axis=1
    )

    return df

# Apply the function
ev_results = merge_and_ratio(
    ev_vehicle_zip,
    ev_station_zip,
    "num_ev_vehicles",
    "num_ev_stations",
    "ev_vehicles_per_station"
)

h2_results = merge_and_ratio(
    h2_vehicle_zip,
    h2_station_zip,
    "num_h2_vehicles",
    "num_h2_stations",
    "h2_vehicles_per_station"
)

# Save outputs
ev_results.to_csv("outputs/ELEC_ratio.csv", index=False)
h2_results.to_csv("outputs/HY_ratio.csv", index=False)

# Debug
print("EV preview:")
print(ev_results.head())

print("\nH2 preview:")
print(h2_results.head())

print("\nEV max vehicles:", ev_results["num_ev_vehicles"].max())
print("H2 max vehicles:", h2_results["num_h2_vehicles"].max())