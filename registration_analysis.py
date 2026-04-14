"""
Zero Emissions Vehicle Registrations Analysis
Input: ZEVs_filtered.csv
Output: growth + ZIP plots
""" 

import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("ZEVs_filtered.csv")

# Clean the data
df.columns = df.columns.str.strip()

df["fuel"] = (
    df["fuel"]
    .astype(str)
    .str.strip()
)

df["zip"] = df["zip"].astype(str).str.strip()

df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
df = df.dropna(subset=["Year"])

# Force to integer years (no decimals)
df["Year"] = df["Year"].astype(int)

df["vehicles"] = pd.to_numeric(df["vehicles"], errors="coerce").fillna(0)

# Yearly Registration growth

growth = df.groupby(["Year", "fuel"])["vehicles"].sum().unstack(fill_value=0)
growth = growth.sort_index()

# Ensure both columns exist
if "Battery Electric" not in growth.columns:
    growth["Battery Electric"] = 0

if "Hydrogen Fuel Cell" not in growth.columns:
    growth["Hydrogen Fuel Cell"] = 0

# Electrive Vehicle Growth
plt.figure(figsize=(8,5))

plt.plot(
    growth.index,
    growth["Battery Electric"],
    marker="o",
    color="green"
)

plt.title("Battery Electric Vehicle Growth (2020–2025)")
plt.xlabel("Year")
plt.ylabel("Number of Registrations")
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("outputs/bev_growth.png", dpi=300)
plt.show()


# Hydrogen Growth Plot
plt.figure(figsize=(8,5))

plt.plot(
    growth.index,
    growth["Hydrogen Fuel Cell"],
    marker="o",
    color="blue"
)

plt.title("Hydrogen Fuel Cell Vehicle Growth (2020–2025)")
plt.xlabel("Year")
plt.ylabel("Number of Registrations")
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("outputs/h2_growth.png", dpi=300)
plt.show()


# Top Zip Code Distribution

zip_counts = df.groupby(["zip", "fuel"])["vehicles"].sum().reset_index()

# Electric Vehicle Distribution
bev_zip = (
    zip_counts[zip_counts["fuel"] == "Battery Electric"]
    .sort_values("vehicles", ascending=False)
    .head(10)
)

plt.figure(figsize=(8,5))
plt.bar(bev_zip["zip"], bev_zip["vehicles"], color="green")

plt.title("Top 10 ZIP Codes - Battery Electric Vehicles")
plt.xlabel("ZIP Code")
plt.ylabel("Number of Registrations")
plt.xticks(rotation=45)
plt.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.savefig("outputs/bev_zip_top10.png", dpi=300)
plt.show()


# Hydrogen Zip Code Distribution
h2_zip = (
    zip_counts[zip_counts["fuel"] == "Hydrogen Fuel Cell"]
    .sort_values("vehicles", ascending=False)
    .head(10)
)

plt.figure(figsize=(8,5))
plt.bar(h2_zip["zip"], h2_zip["vehicles"], color="blue")

plt.title("Top 10 ZIP Codes - Hydrogen Fuel Cell Vehicles")
plt.xlabel("ZIP Code")
plt.ylabel("Number of Registrations")
plt.xticks(rotation=45)
plt.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.savefig("outputs/h2_zip_top10.png", dpi=300)
plt.show()