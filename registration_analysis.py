"""
Zero Emissions Vehicle Registrations Analysis
Input: ZEVs_filtered.csv
Output: bev_growth.png, bev_zip_top10.png, h2_zip_top10.png
""" 

# import  modules
import pandas as pd
import matplotlib.pyplot as plt

# Load the data - Reads cleaned dataset into a DataFrame
df = pd.read_csv("outputs/ZEVs_filtered.csv")

# Clean the data by removing extra spaces from column names
df.columns = df.columns.str.strip()

# Ensure fuel column is a string type and remove extra spaces
df["fuel"] = (
    df["fuel"]
    .astype(str)
    .str.strip()
)

# Converts ZIP codes to strings and remove whitespaces
df["zip"] = df["zip"].astype(str).str.strip()

# Convert Year column to numeric; invalid values become NaN
df["Year"] = pd.to_numeric(df["Year"], errors="coerce")

# Drop rows where Year could not be converted
df = df.dropna(subset=["Year"])

# Convert Year to integer type for cleaner plotting
df["Year"] = df["Year"].astype(int)

# Convert vehicles column to numeric; replaces invalid values with 0
df["vehicles"] = pd.to_numeric(df["vehicles"], errors="coerce").fillna(0)



# Yearly Registration Growth

# Group data by Year and fuel type, sum vehicles, and put fuel types into columns
growth = df.groupby(["Year", "fuel"])["vehicles"].sum().unstack(fill_value=0)

# Sort DataFrame by Year index in ascending order
growth = growth.sort_index()

# Ensure both columns exist
# Add missing column for Battery Electric if it doesn't exist
if "Battery Electric" not in growth.columns:
    growth["Battery Electric"] = 0

# Adds missing column for Hydrogen Fuel Cell if it doesn't exist
if "Hydrogen Fuel Cell" not in growth.columns:
    growth["Hydrogen Fuel Cell"] = 0
 
    
# Electrive Vehicle Growth
# Create a new figure for the Battery Electric Vehicles Registration line Chart
plt.figure(figsize=(8,5))

# plots Battery Electric vehicle growth over time
plt.plot(
    growth.index,
    growth["Battery Electric"],
    marker="o",
    color="blue"
)
# Force x-axis to show only whole years
plt.xticks(growth.index)
# Sets the chart title
plt.title("Battery Electric Vehicle Registrations Growth (2020–2025)")
# Labels x-axis
plt.xlabel("Year")
# Label y-axis
plt.ylabel("Number of Registrations")
# Adds grid lines
plt.grid(True, alpha=0.3)

# Prevents overlapping elements
plt.tight_layout()

# Save plot
plt.savefig("outputs/bev_growth.png", dpi=300)

# Display plot
plt.show()



# Hydrogen Growth Plot
# Creates figure for hydrogen vehicle registration growth
plt.figure(figsize=(8,5))
 
# Plots hydrogen fuel cell growth over time
plt.plot(
    growth.index,
    growth["Hydrogen Fuel Cell"],
    marker="o",
    color="green"
)
# Forces x-axis to show whole years
plt.xticks(growth.index)
# Sets chart title
plt.title("Hydrogen Fuel Cell Vehicle Registration Growth (2020–2025)")
# Labels x-axis
plt.xlabel("Year")
# Labels y-axis
plt.ylabel("Number of Registrations")
# Adds gridlines
plt.grid(True, alpha=0.3)

# Fixes layout
plt.tight_layout()

# Save hydrogen growth plot
plt.savefig("outputs/h2_growth.png", dpi=300)
# Display the plot
plt.show()


# Top Zip Code Distribution

# Groups data by ZIP and fuel type, summing total vehicles
zip_counts = df.groupby(["zip", "fuel"])["vehicles"].sum().reset_index()


# Electric Vehicle Distribution
# Filters Battery Electric Vehicle data, sorts by highest registrations, keeps top 10 zip codes
bev_zip = (
    zip_counts[zip_counts["fuel"] == "Battery Electric"]
    .sort_values("vehicles", ascending=False)
    .head(10)
)

# Creates bar chart for top 10 Battery Electric Vehicle Registration Zip Codes
plt.figure(figsize=(8,5))
plt.bar(bev_zip["zip"], bev_zip["vehicles"], color="green")

# Set chart title
plt.title("Battery Electric Vehicles Registrations in California by Zip Code (2025)")
# Label x-axis
plt.xlabel("ZIP Code")
# Label y-axis
plt.ylabel("Number of Registrations")
# Rottate ZIP labels for readability
plt.xticks(rotation=45)
# Add grid lines
plt.grid(axis="y", alpha=0.3)

# Cleans up layout
plt.tight_layout()

# Save ZIP distribution plot
plt.savefig("outputs/bev_zip_top10.png", dpi=300)

# Display the plot
plt.show()


# Hydrogen Zip Code Distribution
# Filters hydrogren data, sorts, and selects top 10 ZIP codes
h2_zip = (
    zip_counts[zip_counts["fuel"] == "Hydrogen Fuel Cell"]
    .sort_values("vehicles", ascending=False)
    .head(10)
)

# Create bar chart for Hydrogen ZIP distribution
plt.figure(figsize=(8,5))
plt.bar(h2_zip["zip"], h2_zip["vehicles"], color="blue")

# chart title
plt.title("Hydrogen Fuel Cell Vehicles Registrations in California by ZIP Code (2025)")
# Label x-axis
plt.xlabel("ZIP Code")
# Label y-axis
plt.ylabel("Number of Registrations")
# Rotate ZIP labels
plt.xticks(rotation=45)
# Add grid lines
plt.grid(axis="y", alpha=0.3)

# Clean up layout
plt.tight_layout()

# Save Hydrogen Registration ZIP plot
plt.savefig("outputs/h2_zip_top10.png", dpi=300)

# Display final plot
plt.show()