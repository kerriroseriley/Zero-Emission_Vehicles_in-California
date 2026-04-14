"""
Zero Emission Vehicles Registration Analysis
Input: ZEVs_filtered.csv
Output: zipcode_registration.png
"""
# import modules
import pandas as pd
import matplotlib.pyplot as plt

# Load my Data
df = pd.read_csv("ZEVs_filtered.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Fix the Data Types
df["zip"] = df["zip"].astype(str).str.strip()

# Clean Year
df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
df = df.dropna(subset=["Year"])
df["Year"] = df["Year"].astype(int)

# Filter for 2025
df_2025 = df[df["Year"] == 2025]

# Registration Totals by Fuel Type
bev_total = df_2025[df_2025["fuel"] == "Battery Electric"]["vehicles"].sum()
fcev_total = df_2025[df_2025["fuel"] == "Hydrogen Fuel Cell"]["vehicles"].sum()

print("Battery Electric Vehicles (2025):", bev_total)
print("Hydrogen Fuel Cell Vehicles (2025):", fcev_total)

# Split by Fuel Type
bev = df_2025[df_2025["fuel"] == "Battery Electric"]
fcev = df_2025[df_2025["fuel"] == "Hydrogen Fuel Cell"]

# Top 10 Zip Codes
bev_top10 = (
    bev.groupby("zip")["vehicles"]
    .sum()
    .sort_values()
    .tail(10)
)

fcev_top10 = (
    fcev.groupby("zip")["vehicles"]
    .sum()
    .sort_values()
    .tail(10)
)

#  Plot
plt.figure(figsize=(14,6))

# Battery Electric 
plt.subplot(1,2,1)
plt.barh(bev_top10.index, bev_top10.values, color="royalblue")
plt.title("Top 10 ZIPs - Battery Electric Vehicles (2025)")
plt.xlabel("Registrations")

for i, v in enumerate(bev_top10.values):
    plt.text(v, i, str(int(v)), va='center')

# Hydrogen Fuel Cell 
plt.subplot(1,2,2)
plt.barh(fcev_top10.index, fcev_top10.values, color="green")
plt.title("Top 10 ZIPs - Hydrogen Fuel Cell Vehicles (2025)")
plt.xlabel("Registrations")

for i, v in enumerate(fcev_top10.values):
    plt.text(v, i, str(int(v)), va='center')

plt.tight_layout()

# SAVE IMAGE

plt.savefig("outputs/zipcode_registration.png", dpi=300, bbox_inches="tight")

plt.show()



# Cumulative GROWTH TREND

# Filter full time range
df_time = df[(df["Year"] >= 2020) & (df["Year"] <= 2025)]

# Total registrations per year
yearly_total = (
    df_time.groupby("Year")["vehicles"]
    .sum()
    .reindex(range(2020, 2026), fill_value=0)
)


# Cumulative growth
cumulative_total = yearly_total.cumsum()

# Plot growth trend
plt.figure(figsize=(10,6))

plt.plot(
    cumulative_total.index,
    cumulative_total.values,
    marker="o",
    linewidth=2,
    color="darkblue"
)

plt.title("Cumulative ZEV Registration Growth (2020–2025)")
plt.xlabel("Year")
plt.ylabel("Cumulative Registrations")
plt.grid(True)

# Clean x-axis
plt.xticks(cumulative_total.index)

# Optional labels on points
for x, y in zip(cumulative_total.index, cumulative_total.values):
    plt.text(x, y, f"{int(y)}", ha="center", va="bottom")

plt.tight_layout()
plt.savefig("outputs/zev_growth_trend.png", dpi=300, bbox_inches="tight")
plt.show()

# HEATMAP FOR QGIZ SHOWING Distribution of ZEV Registrations by Zip Code and Year (%)

# Filter years 2020–2025
df_qgis = df[(df["Year"] >= 2020) & (df["Year"] <= 2025)]

# BEV by ZIP + Year
bev_q = (
    df_qgis[df_qgis["fuel"] == "Battery Electric"]
    .groupby(["zip", "Year"])["vehicles"]
    .sum()
    .reset_index()
    .rename(columns={"vehicles": "bev"})
)

# FCEV by ZIP + Year
fcev_q = (
    df_qgis[df_qgis["fuel"] == "Hydrogen Fuel Cell"]
    .groupby(["zip", "Year"])["vehicles"]
    .sum()
    .reset_index()
    .rename(columns={"vehicles": "fcev"})
)

# Merge BEV + FCEV
qgis_df = pd.merge(bev_q, fcev_q, on=["zip", "Year"], how="outer")

# Replace NaNs with 0
qgis_df[["bev", "fcev"]] = qgis_df[["bev", "fcev"]].fillna(0)

# Total EVs
qgis_df["total"] = qgis_df["bev"] + qgis_df["fcev"]

# Ensure correct types
qgis_df["Year"] = qgis_df["Year"].astype(int)
qgis_df["zip"] = qgis_df["zip"].astype(str)

# Save file for QGIS
qgis_df.to_csv("outputs/zev_qgis_heatmap.csv", index=False)

print("QGIS file created: registration_qgis_heatmap.csv")


