import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("ZEVs_filtered.csv")

df["Year"] = df["Year"].astype(int)
df["vehicles"] = pd.to_numeric(df["vehicles"], errors="coerce").fillna(0)

# ----------------------------------------------------
# FINDING 1: REGISTRATION GROWTH OVER TIME
# ----------------------------------------------------

yearly = df.groupby(["Year", "fuel"])["vehicles"].sum().reset_index()

bev_growth = yearly[yearly["fuel"] == "Battery Electric"].sort_values("Year")
h2_growth = yearly[yearly["fuel"] == "Hydrogen Fuel Cell"].sort_values("Year")

# BEV Growth Plot
plt.figure(figsize=(8,5))
plt.plot(bev_growth["Year"], bev_growth["vehicles"], marker="o", color="green")
plt.title("Finding 1A: Battery Electric Vehicle Growth (2020–2025)")
plt.xlabel("Year")
plt.ylabel("Registrations")
plt.grid(True)
plt.show()

# Hydrogen Growth Plot
plt.figure(figsize=(8,5))
plt.plot(h2_growth["Year"], h2_growth["vehicles"], marker="o", color="blue")
plt.title("Finding 1B: Hydrogen Fuel Cell Growth (2020–2025)")
plt.xlabel("Year")
plt.ylabel("Registrations")
plt.grid(True)
plt.show()


# ----------------------------------------------------
# FINDING 2: TOP ZIP CODES (GEOGRAPHIC CONCENTRATION)
# ----------------------------------------------------

zip_totals = df.groupby(["zip", "fuel"])["vehicles"].sum().reset_index()

bev_zip = (
    zip_totals[zip_totals["fuel"] == "Battery Electric"]
    .sort_values("vehicles", ascending=False)
    .head(10)
)

h2_zip = (
    zip_totals[zip_totals["fuel"] == "Hydrogen Fuel Cell"]
    .sort_values("vehicles", ascending=False)
    .head(10)
)

# BEV ZIP Plot
plt.figure(figsize=(8,5))
plt.bar(bev_zip["zip"], bev_zip["vehicles"], color="green")
plt.title("Finding 2A: Top 10 ZIP Codes - Battery Electric Vehicles")
plt.xlabel("ZIP Code")
plt.ylabel("Registrations")
plt.xticks(rotation=45)
plt.show()

# Hydrogen ZIP Plot
plt.figure(figsize=(8,5))
plt.bar(h2_zip["zip"], h2_zip["vehicles"], color="blue")
plt.title("Finding 2B: Top 10 ZIP Codes - Hydrogen Fuel Cell Vehicles")
plt.xlabel("ZIP Code")
plt.ylabel("Registrations")
plt.xticks(rotation=45)
plt.show()

