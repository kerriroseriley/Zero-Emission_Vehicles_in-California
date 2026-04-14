
""" 
Zero Emission Vehicles Charger Analysis
Input: stations_2020_2025.csv
Output: 

""" 
import pandas as pd 
import matplotlib.pyplot as plt 

# Load data
df = pd.read_csv("stations_2020_2025.csv")


# Clean columns
df.columns = df.columns.str.strip()
df["ZIP"] = df["ZIP"].astype(str).str.strip()

 
# -Split by Fuel Type
df_elec = df[df["Fuel Type Code"] == "ELEC"]
df_hy = df[df["Fuel Type Code"] == "HY"]

# Top 10 Zip Codes for Each
elec_top10 = df_elec["ZIP"].value_counts().head(10).sort_values()
hy_top10 = df_hy["ZIP"].value_counts().head(10).sort_values()

# Plot
plt.figure(figsize=(14,6))

#  Electric 
plt.subplot(1,2,1)
plt.barh(elec_top10.index, elec_top10.values, color="blue")
plt.title("Top 10 ZIPs - Electric Charging Stations")
plt.xlabel("Number of Stations")

for i, v in enumerate(elec_top10.values):
    plt.text(v, i, str(v), va='center')

# Hydrogen
plt.subplot(1,2,2)
plt.barh(hy_top10.index, hy_top10.values, color="green")
plt.title("Top 10 ZIPs - Hydrogen Stations")
plt.xlabel("Number of Stations")

for i, v in enumerate(hy_top10.values):
    plt.text(v, i, str(v), va='center')

plt.tight_layout()

# Save image
plt.savefig("top10_zip_charger_stations.png", dpi=300, bbox_inches="tight")

plt.show()

