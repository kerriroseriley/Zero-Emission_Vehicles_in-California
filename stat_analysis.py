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


# -----------------------------
# YEARLY GROWTH ANALYSIS
# -----------------------------

# Build grouped table (safe + flexible)
growth = df.groupby(["Year", "Fuel Type Code"]).size().unstack(fill_value=0)

# Ensure both columns exist (prevents errors if missing)
if "ELEC" not in growth.columns:
    growth["ELEC"] = 0
 
if "HY" not in growth.columns:
    growth["HY"] = 0

growth = growth.sort_index()

# =========================================================
# ELECTRIC GROWTH PLOT
# =========================================================
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

# =========================================================
# HYDROGEN GROWTH PLOT
# =========================================================
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