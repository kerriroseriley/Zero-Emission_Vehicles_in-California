"""
Zero Emissions Vehicles Charger Stations Analysis
Input: stations_2020_2025.csv
Output:
    
""" 
# import modules
import pandas as pd
import matplotlib.pyplot as plt

# Reads the combined charger station dataset
df = pd.read_csv("stations_2020_2025.csv")

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
plt.title("Electric Station Growth (2020–2025)")
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
plt.title("Hydrogen Station Growth (2020–2025)")
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