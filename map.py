
"""
Map ZIP-level ZEV ratios to GeoPackages

Inputs:
- ELEC_ratio.csv
- HY_ratio.csv
- cb_2025_us_zcta520_500k.zip
- cb_2020_us_state_500k.zip 

Outputs: ELEC_ratio.gpkg, HY_ratio.gpkg
"""

# import modules
import pandas as pd
import geopandas as gpd

# Load ratio data
ev = pd.read_csv("outputs/ELEC_ratio.csv", dtype={"zip": str})
h2 = pd.read_csv("outputs/HY_ratio.csv", dtype={"zip": str})

# Clean ZIP format
ev["zip"] = ev["zip"].astype(str).str.strip().str[:5]
h2["zip"] = h2["zip"].astype(str).str.strip().str[:5]

# Load the shapefiles
zcta = gpd.read_file("tl_2025_us_zcta520.zip")

# States layer 
states = gpd.read_file("tl_2025_us_state.zip")

# Standardize ZIP column
zcta["zip"] = zcta["ZCTA5CE20"]

# Filter to California
# FIPS code for California = '06'
ca = states[states["STATEFP"] == "06"]

# Ensure same CRS before spatial operations
zcta = zcta.to_crs(ca.crs)

# Clip ZIPs to California boundary
zcta_ca = gpd.clip(zcta, ca)


# Drop any of the invalid zip codes (PO Boxs)
valid_zips = set(zcta["zip"])

ev = ev[ev["zip"].isin(valid_zips)]
h2 = h2[h2["zip"].isin(valid_zips)]

# Merge with geometry
ev_gdf = zcta.merge(ev, on="zip", how="inner")
h2_gdf = zcta.merge(h2, on="zip", how="inner")

# Convert to GeoDataFrame explicitly
ev_gdf = gpd.GeoDataFrame(ev_gdf, geometry="geometry")
h2_gdf = gpd.GeoDataFrame(h2_gdf, geometry="geometry")



# Save the geopackage
ev_gdf.to_file("outputs/ELEC_ratio.gpkg", layer="ev_ratio", driver="GPKG")
h2_gdf.to_file("outputs/HY_ratio.gpkg", layer="h2_ratio", driver="GPKG")

# Debugging
print("EV GeoData:")
print(ev_gdf.head())

print("\nH2 GeoData:")
print(h2_gdf.head())

