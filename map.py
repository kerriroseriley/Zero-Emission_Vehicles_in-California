  
""" 
Map ZIP-level ZEV ratios to GeoPackages
Inputs: ELEC_ratio.csv, HY_ratio.csv, tl_2025_us_zcta520.zip, tl_2025_us_state.zip
Outputs: CALIFORNIA.gpkg, ELEC_ratio.gpkg, HY_ratio.gpkg
"""

# import modules
import pandas as pd
import geopandas as gpd

# Load the data
ev = pd.read_csv("outputs/ELEC_ratio.csv")
h2 = pd.read_csv("outputs/HY_ratio.csv") 
 
# Standardize ZIPs (robust)
ev["zip"] = ev["zip"].astype(str).str.extract(r"(\d{5})")[0]
h2["zip"] = h2["zip"].astype(str).str.extract(r"(\d{5})")[0]

# Track before counts
ev_before = len(ev)
h2_before = len(h2)

# Drop invalid ZIPs
ev = ev.dropna(subset=["zip"])
h2 = h2.dropna(subset=["zip"])

# Track after counts
ev_after = len(ev)
h2_after = len(h2)

print(f"EV dropped invalid ZIPs: {ev_before - ev_after} ({(ev_before - ev_after)/ev_before:.2%})")
print(f"H2 dropped invalid ZIPs: {h2_before - h2_after} ({(h2_before - h2_after)/h2_before:.2%})")
 
# Geography
zcta = gpd.read_file("tl_2025_us_zcta520.zip")
states = gpd.read_file("tl_2025_us_state.zip")

# Ensure CRS match
ca = states[states["STATEFP"] == "06"]

zcta = zcta.to_crs(ca.crs)

# Clip ZIPS to California 
zcta_ca = gpd.clip(zcta, ca, keep_geom_type=True)
  
# Standardize ZIP column 
zcta_ca = zcta_ca.rename(columns={"ZCTA5CE20": "zip"})
zcta_ca["zip"] = zcta_ca["zip"].astype(str)
 
# Debug overlap
print("EV ZIPs:", ev["zip"].nunique())
print("H2 ZIPs:", h2["zip"].nunique())
print("CA ZCTAs:", zcta_ca["zip"].nunique())

overlap_ev = set(ev["zip"]) & set(zcta_ca["zip"])
overlap_h2 = set(h2["zip"]) & set(zcta_ca["zip"])

print("EV overlap:", len(overlap_ev))
print("H2 overlap:", len(overlap_h2))

#  Filter to CA ZIPs

ev_ca = ev[ev["zip"].isin(zcta_ca["zip"])]
h2_ca = h2[h2["zip"].isin(zcta_ca["zip"])]

print("EV after filtering to CA ZIP:", len(ev_ca))
print("H2 after filter to CA ZIP:", len(h2_ca))

# Merge the data
ev_gdf = zcta_ca.merge(ev, on="zip", how="left")
h2_gdf = zcta_ca.merge(h2, on="zip", how="left")

# Ensure GeoDataFrames
ev_gdf = gpd.GeoDataFrame(ev_gdf, geometry="geometry", crs=zcta_ca.crs)
h2_gdf = gpd.GeoDataFrame(h2_gdf, geometry="geometry", crs=zcta_ca.crs)
 
# Create California layer
ca_fill = ca.copy()
ca_fill["layer"] = "background"

# Save the layers
ca_fill.to_file("outputs/CALIFORNIA.gpkg", layer="ca_fill", driver="GPKG")
ev_gdf.to_file("outputs/ELEC_ratio.gpkg", layer="ev_ratio", driver="GPKG")
h2_gdf.to_file("outputs/HY_ratio.gpkg", layer="h2_ratio", driver="GPKG")
