"""
Merging ZEV Stations and Registrations and Ratio Function
Inputs: ZEVs_filtered.csv, stations_2020_2025.csv
Outputs: ELEC_ratio.csv, HY_ratio.csv
merged.py 

"""

# import modules
import pandas as pd 

# Enables pandas copy-on-write mode 
pd.options.mode.copy_on_write = True


# Load Data Sets and makes zip column be treated as a string
zev_vehicles = pd.read_csv("ZEVs_filtered.csv", dtype={"zip": str})
zev_stations = pd.read_csv("stations_2020_2025.csv", dtype={"ZIP": str})


# Standardize columns and renames ZIP column to match lowercase format
zev_vehicles = zev_vehicles.rename(columns={"ZIP": "zip"})
zev_stations = zev_stations.rename(columns={"ZIP": "zip"})


# Clean ZIP codes by converting to strings, removing spaces, and only keeping first 5 digits
zev_vehicles["zip"] = zev_vehicles["zip"].astype(str).str.strip().str[:5]
zev_stations["zip"] = zev_stations["zip"].astype(str).str.strip().str[:5]


# Convert Year to string and removes whitespaces
zev_vehicles["Year"] = zev_vehicles["Year"].astype(str).str.strip()
zev_stations["Year"] = zev_stations["Year"].astype(str).str.strip()

# Filter data to only include Year 2025
vehicles_2025 = zev_vehicles[zev_vehicles["Year"] == "2025"]
stations_2025 = zev_stations[zev_stations["Year"] == "2025"]


# Split Fuel Type
# Filters EV 
ev_vehicles = vehicles_2025[
    vehicles_2025["fuel"].str.contains("Battery Electric", case=False, na=False)
]
# Filters Hydrogen Fuel Cell only
hydrogen_vehicles = vehicles_2025[
    vehicles_2025["fuel"].str.contains("Hydrogen Fuel Cell", case=False, na=False)
] 

# Aggretgate Vehicles 

# Groups EV vehicle registrations by zip and sums total vehicle registrations per ZIP
ev_vehicle_zip = (
    ev_vehicles.groupby("zip")["vehicles"]
    .sum()
    .reset_index(name="num_ev_vehicles")
) 
# Groups Hydrogen vehicle registrations by ZIP and sums totals per ZIP
h2_vehicle_zip = (
    hydrogen_vehicles.groupby("zip")["vehicles"]
    .sum()
    .reset_index(name="num_h2_vehicles")
)

# Stations
# Filters EV charging stations
ev_stations = stations_2025[stations_2025["Fuel Type Code"] == "ELEC"]
# Filters Hydrogen Fuel Cell charging stations
h2_stations = stations_2025[stations_2025["Fuel Type Code"] == "HY"]

# Counts EV stations per ZIP
ev_station_zip = ev_stations.groupby("zip").size().reset_index(name="num_ev_stations")
# Counts Hydrogen stations per ZIP
h2_station_zip = h2_stations.groupby("zip").size().reset_index(name="num_h2_stations")


# Merge and Ratio Function

# Function merges vehicle and station data by ZIP, filling missing value with 0
def merge_and_ratio(v, s, vcol, scol, ratio_col):
    df = pd.merge(v, s, on="zip", how="outer").fillna(0)
    # Computes ratio of vehicles per station (and avoids division by 0)
    df[ratio_col] = df.apply(
        lambda r: r[vcol] / r[scol] if r[scol] > 0 else None,
        axis=1
    )
    # Returns merged DataFrame with calculated ratio
    return df

# Applies merge + ratio calulcation for EV data
ev_results = merge_and_ratio(
    ev_vehicle_zip, ev_station_zip,
    "num_ev_vehicles", "num_ev_stations",
    "ev_vehicles_per_station"
)

# Applies merge + ratio calculation for Hydrogen Fuel Cell Data
h2_results = merge_and_ratio(
    h2_vehicle_zip, h2_station_zip,
    "num_h2_vehicles", "num_h2_stations",
    "h2_vehicles_per_station"
)


# Save Outputs to two separate CSV files
ev_results.to_csv("outputs/ELEC_ratio.csv", index=False)
h2_results.to_csv("outputs/HY_ratio.csv", index=False)

# Prints first few rows of results
print(ev_results.head())
print(h2_results.head())