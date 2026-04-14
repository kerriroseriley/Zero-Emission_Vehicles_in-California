import pandas as pd

pd.options.mode.copy_on_write = True


# Load Data
zev_vehicles = pd.read_csv("ZEVs_filtered.csv", dtype={"zip": str})
zev_stations = pd.read_csv("stations_2020_2025.csv", dtype={"ZIP": str})


# Standardize columns
zev_vehicles = zev_vehicles.rename(columns={"ZIP": "zip"})
zev_stations = zev_stations.rename(columns={"ZIP": "zip"})


# Clean ZIP codes
zev_vehicles["zip"] = zev_vehicles["zip"].astype(str).str.strip().str[:5]
zev_stations["zip"] = zev_stations["zip"].astype(str).str.strip().str[:5]


# Convert Year
zev_vehicles["Year"] = pd.to_numeric(zev_vehicles["Year"], errors="coerce")
zev_stations["Year"] = pd.to_numeric(zev_stations["Year"], errors="coerce")


# Filter 2025
vehicles_2025 = zev_vehicles[zev_vehicles["Year"] == 2025]
stations_2025 = zev_stations[zev_stations["Year"] == 2025]


# Split Fuel Type

ev_vehicles = vehicles_2025[vehicles_2025["fuel"] == "Electric"]

hydrogen_vehicles = vehicles_2025[vehicles_2025["fuel"] == "Hydrogen"]


# Aggretgate Vehicles 

ev_vehicle_zip = (
    ev_vehicles.groupby("zip")["vehicles"]
    .sum()
    .reset_index(name="num_ev_vehicles")
) 

h2_vehicle_zip = (
    hydrogen_vehicles.groupby("zip")["vehicles"]
    .sum()
    .reset_index(name="num_h2_vehicles")
)


# Stations

ev_stations = stations_2025[stations_2025["Fuel Type Code"] == "Electric"]
h2_stations = stations_2025[stations_2025["Fuel Type Code"] == "Hydrogen"]


ev_station_zip = ev_stations.groupby("zip").size().reset_index(name="num_ev_stations")
h2_station_zip = h2_stations.groupby("zip").size().reset_index(name="num_h2_stations")


# Merge and Ratio Function

def merge_and_ratio(v, s, vcol, scol, ratio_col):
    df = pd.merge(v, s, on="zip", how="outer").fillna(0)

    df[ratio_col] = df.apply(
        lambda r: r[vcol] / r[scol] if r[scol] > 0 else None,
        axis=1
    )
    return df


ev_results = merge_and_ratio(
    ev_vehicle_zip, ev_station_zip,
    "num_ev_vehicles", "num_ev_stations",
    "ev_vehicles_per_station"
)

h2_results = merge_and_ratio(
    h2_vehicle_zip, h2_station_zip,
    "num_h2_vehicles", "num_h2_stations",
    "h2_vehicles_per_station"
)


# Save Outputs

ev_results.to_csv("ELEC_ratio.csv", index=False)
h2_results.to_csv("HY_ratio.csv", index=False)


print(ev_results.head())
print(h2_results.head())