
"""
Map ZIP-level ZEV ratios to GeoPackages

Inputs:
- ELEC_ratio.csv
- HY_ratio.csv
- cb_2025_us_zcta520_500k.zip
- cb_2020_us_state_500k.zip 

Outputs: ELEC_ratio.gpkg, HY_ratio.gpkg
"""


import pandas as pd
import geopandas as gpd

# -----------------------------
# 1. Load EV + H2 data
# -----------------------------
ev = pd.read_csv("outputs/ELEC_ratio.csv")
h2 = pd.read_csv("outputs/HY_ratio.csv") 

# Standardize ZIPs (robust)
ev["zip"] = ev["zip"].astype(str).str.extract(r"(\d{5})")[0]
h2["zip"] = h2["zip"].astype(str).str.extract(r"(\d{5})")[0]

# Drop invalid ZIPs
ev = ev.dropna(subset=["zip"])
h2 = h2.dropna(subset=["zip"])

# -----------------------------
# 2. Load geography
# -----------------------------
zcta = gpd.read_file("tl_2025_us_zcta520.zip")
states = gpd.read_file("tl_2025_us_state.zip")

# Ensure CRS match
ca = states[states["STATEFP"] == "06"]

zcta = zcta.to_crs(ca.crs)

# Clip to California FIRST
zcta_ca = gpd.clip(zcta, ca)

# Standardize ZIP column
zcta_ca = zcta_ca.rename(columns={"ZCTA5CE20": "zip"})
zcta_ca["zip"] = zcta_ca["zip"].astype(str)

# -----------------------------
# 3. Debug overlap (IMPORTANT)
# -----------------------------
print("EV ZIPs:", ev["zip"].nunique())
print("H2 ZIPs:", h2["zip"].nunique())
print("CA ZCTAs:", zcta_ca["zip"].nunique())

overlap_ev = set(ev["zip"]) & set(zcta_ca["zip"])
overlap_h2 = set(h2["zip"]) & set(zcta_ca["zip"])

print("EV overlap:", len(overlap_ev))
print("H2 overlap:", len(overlap_h2))

# -----------------------------
# 4. Filter to CA ZIPs
# -----------------------------
ev_ca = ev[ev["zip"].isin(zcta_ca["zip"])]
h2_ca = h2[h2["zip"].isin(zcta_ca["zip"])]

print("EV after filter:", len(ev_ca))
print("H2 after filter:", len(h2_ca))

# -----------------------------
# 5. Merge correctly
# -----------------------------
ev_gdf = zcta_ca.merge(ev_ca, on="zip", how="inner")
h2_gdf = zcta_ca.merge(h2_ca, on="zip", how="inner")

# Convert explicitly
ev_gdf = gpd.GeoDataFrame(ev_gdf, geometry="geometry", crs=zcta_ca.crs)
h2_gdf = gpd.GeoDataFrame(h2_gdf, geometry="geometry", crs=zcta_ca.crs)

# -----------------------------
# 6. Final sanity checks
# -----------------------------
print("EV merged rows:", len(ev_gdf))
print("H2 merged rows:", len(h2_gdf))

print(ev_gdf[["zip", "num_ev_vehicles", "num_ev_stations"]].head())
print(h2_gdf[["zip", "num_h2_vehicles", "num_h2_stations"]].head())

# -----------------------------
# 7. Save GeoPackages
# -----------------------------
ev_gdf.to_file("outputs/ELEC_ratio.gpkg", layer="ev_ratio", driver="GPKG")
h2_gdf.to_file("outputs/HY_ratio.gpkg", layer="h2_ratio", driver="GPKG")


print(ev["num_ev_vehicles"].dtype)
print(ev["num_ev_vehicles"].describe())

print((ev["num_ev_vehicles"] > 0).sum())
