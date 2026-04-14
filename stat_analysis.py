"""
Zero Emissions Vehicles Charger Stations Analysis
Input: stations_2020_2025.csv
Output: plots
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Load dataset
# -----------------------------
df = pd.read_csv("stations_2020_2025.csv")

# -----------------------------
# Clean columns
# -----------------------------
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

# -----------------------------
# Output folder
# -----------------------------
os.makedirs("outputs", exist_ok=True)

# =========================================================
# 1. YEARLY GROWTH (ELEC vs HY)
# =========================================================
growth = df.groupby(["Year", "Fuel Type Code"]).size().unstack(fill_value=0)

plt.figure(figsize=(10,6))

plt.plot(growth.index, growth["ELEC"], marker="o", label="Electric (ELEC)", color="blue")
plt.plot(growth.index, growth["HY"], marker="o", label="Hydrogen (HY)", color="green")

plt.title("ZEV Station Growth (2020–2025)")
plt.xlabel("Year")
plt.ylabel("Number of Stations")
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("outputs/growth_comparison.png", dpi=300)
plt.show()

# =========================================================
# 2. TOP 10 ZIP CODES
# =========================================================
elec_top10 = (
    df[df["Fuel Type Code"] == "ELEC"]["ZIP"]
    .value_counts()
    .head(10)
    .sort_values()
)

hy_top10 = (
    df[df["Fuel Type Code"] == "HY"]["ZIP"]
    .value_counts()
    .head(10)
    .sort_values()
)

plt.figure(figsize=(14,6))

# Electric
plt.subplot(1,2,1)
plt.barh(elec_top10.index, elec_top10.values, color="blue")
plt.title("Top 10 ZIPs - Electric Stations")
plt.xlabel("Number of Stations")

# Hydrogen
plt.subplot(1,2,2)
plt.barh(hy_top10.index, hy_top10.values, color="green")
plt.title("Top 10 ZIPs - Hydrogen Stations")
plt.xlabel("Number of Stations")

plt.tight_layout()
plt.savefig("outputs/top10_zip_chargers.png", dpi=300)
plt.show()

