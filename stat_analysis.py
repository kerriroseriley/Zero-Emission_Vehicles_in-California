"""
Zero Emissions Vehicles Charger Stations Analysis
Input: stations_2020_2025.csv
Output: elec_growth.png, hy_growth.png, top10_zip_charger_stations.png
    
""" 

# import modules 
import pandas as pd
import matplotlib.pyplot as plt

# Reads the combined charger station dataset
df = pd.read_csv("outputs/stations_2020_2025.csv")

# Clean Columns by removing whitespace from column names 
df.columns = df.columns.str.strip()

# Standardizes fuel type codes to uppercase and removes whitespace
df["Fuel Type Code"] = (
    df["Fuel Type Code"]
    .astype(str)
    .str.upper() 
    .str.strip()
)

# Converts ZIP codes to string and removes extra spaces
df["ZIP"] = df["ZIP"].astype(str).str.strip()

# Converts Year to numeric; invalid values become NaN, then stored as integers 
df["Year"] = pd.to_numeric(df["Year"], errors="coerce").astype("Int64")

# Removes rows where Year is missing or invalid
df = df.dropna(subset=["Year"])


zip_counts = df.groupby(["ZIP", "Fuel Type Code"]).size().reset_index(name="station_count")

elec_zip = (
    zip_counts[zip_counts["Fuel Type Code"] == "ELEC"]
    .sort_values("station_count", ascending=False)
    .head(10)
)

hy_zip = (
    zip_counts[zip_counts["Fuel Type Code"] == "HY"]
    .sort_values("station_count", ascending=False)
    .head(10)
)

# Top 10 ZIP Code Analysis: Battery Electric Stations

plt.figure(figsize=(7,5))

plt.bar(elec_zip["ZIP"], elec_zip["station_count"], color="blue")

plt.title("Number of Battery Electric Stations by ZIP Code (2025)")
plt.xlabel("ZIP Code")
plt.ylabel("Number of Stations")
plt.xticks(rotation=45)
plt.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.savefig("outputs/elec_top10_zip_charger_stations.png", dpi=300)
plt.show()



# Top 10 ZIP Code Analysis: HFC Stations
plt.figure(figsize=(7,5))

plt.bar(hy_zip["ZIP"], hy_zip["station_count"], color="green")

plt.title("Number of Hydrogen Fuel Cell Stations by ZIP Code (2025)")
plt.xlabel("ZIP Code")
plt.ylabel("Number of Stations")
plt.xticks(rotation=45)
plt.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.savefig("outputs/h2_top10_zip_charger_stations.png", dpi=300)
plt.show()


# Electric min and max
print(f"Electric stations (top 10 zips) - Min: {elec_zip['station_count'].min()}")
print(f"Electric stations (top 10 zips) - Max: {elec_zip['station_count'].max()}")

# Hydrogen min and max
print(f"Hydrogen stations (top 10 zips) - Min: {hy_zip['station_count'].min()}")
print(f"Hydrogen stations (top 10 zips) - Max: {hy_zip['station_count'].max()}")



# Yearly Growth Trends

# Build grouped table: counts number of stations per year and fuel type 
growth = df.groupby(["Year", "Fuel Type Code"]).size().unstack(fill_value=0)

# Ensure both columns exist (prevents errors if missing)
# Adds ELEC column if missing to avoid plotting issues
if "ELEC" not in growth.columns:
    growth["ELEC"] = 0
 
    # Adds HY column if missing to avoid plotting issues
if "HY" not in growth.columns:
    growth["HY"] = 0

# Sorts data by Year in ascending order
growth = growth.sort_index()


# Electric Stations Growth Plot
# Creates a new figure for electric station
plt.figure(figsize=(8,5))

# Plots electric station counts over time 
plt.plot(
    growth.index,
    growth["ELEC"],
    marker="o",
    color="blue"
)

# Chart title
plt.title("Electric Vehicle Station Growth (2020–2025)")
# Labels x-axis
plt.xlabel("Year")
# Labels y-axis
plt.ylabel("Number of Stations")
# Adds grid lines
plt.grid(True, alpha=0.3)

# Cleans up layout to avoid overlap
plt.tight_layout()
# Saves electric station growth plot as image 
plt.savefig("outputs/elec_growth.png", dpi=300)
# Display electric growth plot
plt.show()

# Hydrogen fuel Cell Station Growth Plot
# Creates figure for hydrogen station growth trends
plt.figure(figsize=(8,5))

# Plots hydrogen station counts over time
plt.plot(
    growth.index,
    growth["HY"],
    marker="o",
    color="green"
)

# Sets chart title
plt.title("Hydrogen Fuel Cell Station Growth (2020–2025)")
# Labels x-axis
plt.xlabel("Year")
# Labels y-axis
plt.ylabel("Number of Stations")
# Adds grid lines
plt.grid(True, alpha=0.3)

# Cleans up layout to avoid overlap
plt.tight_layout()
# Save hydrogen growth plot
plt.savefig("outputs/hy_growth.png", dpi=300)
# Display the plot
plt.show()

# Get 2020 and 2025 station counts

# Electric stations
elec_2020 = growth.loc[2020, "ELEC"]
elec_2021 = growth.loc[2021, "ELEC"]
elec_2022 = growth.loc[2022, "ELEC"]
elec_2023 = growth.loc[2023, "ELEC"]
elec_2024 = growth.loc[2024, "ELEC"]
elec_2025 = growth.loc[2025, "ELEC"]

print(f"Electric stations (2020): {elec_2020}")
print(f"Electric stations (2021): {elec_2021}")
print(f"Electric stations (2022): {elec_2022}")
print(f"Electric stations (2023): {elec_2023}")
print(f"Electric stations (2024): {elec_2024}")
print(f"Electric stations (2025): {elec_2025}")

# Hydrogen stations
hy_2020 = growth.loc[2020, "HY"]
hy_2021 = growth.loc[2021, "HY"]
hy_2022 = growth.loc[2022, "HY"]
hy_2023 = growth.loc[2023, "HY"]
hy_2024 = growth.loc[2024, "HY"]
hy_2025 = growth.loc[2025, "HY"]

print(f"Hydrogen stations (2020): {hy_2020}")
print(f"Hydrogen stations (2021): {hy_2021}")
print(f"Hydrogen stations (2022): {hy_2022}")
print(f"Hydrogen stations (2023): {hy_2023}")
print(f"Hydrogen stations (2024): {hy_2024}")
print(f"Hydrogen stations (2025): {hy_2025}")