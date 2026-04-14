"""
Zero Emissions Vehicles Charger Stations Analysis
Input: stations_2020_2025.csv
Output: plots
""" 

import pandas as pd
import matplotlib.pyplot as plt

# Load Data 
df = pd.read_csv("stations_2020_2025.csv")

# Clean Columns
df.columns = df.columns.str.strip()
df["Fuel Type Code"] = (
    df["Fuel Type Code"]
    .astype(str)
    .str.upper()
    .str.strip()
)
df["ZIP"] = df["ZIP"].astype(str).str.strip()
df["Year"] = pd.to_numeric(df["Year"], errors="coerce").astype("Int64")

df = df.dropna(subset=["Year"])



# Yearly Growth Trends
# Build grouped table
growth = df.groupby(["Year", "Fuel Type Code"]).size().unstack(fill_value=0)

# Ensure both columns exist (prevents errors if missing)
if "ELEC" not in growth.columns:
    growth["ELEC"] = 0
 
if "HY" not in growth.columns:
    growth["HY"] = 0

growth = growth.sort_index()

# Electric Stations Growth Plot
plt.figure(figsize=(8,5))

plt.plot(
    growth.index,
    growth["ELEC"],
    marker="o",
    color="blue"
)

plt.title("Electric Station Growth (2020–2025)")
plt.xlabel("Year")
plt.ylabel("Number of Stations")
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("outputs/elec_growth.png", dpi=300)
plt.show()

# Hydrogen fuel Cell Station Growth Plot
plt.figure(figsize=(8,5))

plt.plot(
    growth.index,
    growth["HY"],
    marker="o",
    color="green"
)

plt.title("Hydrogen Station Growth (2020–2025)")
plt.xlabel("Year")
plt.ylabel("Number of Stations")
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("outputs/hy_growth.png", dpi=300)
plt.show()