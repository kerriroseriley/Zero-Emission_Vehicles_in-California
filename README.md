
# Zero Emission Vehicles and Chargers in California
#### By Kerri Riley 


## Purpose of the Analysis
In 2012, The California Air Resource Board (CARB) adopted the Advanced Clean Car I to control motor vehicle emissions through 2025. In 2022, the Advanced Clean Cars II regulations established the next phase which would begin with the 2026 vehicle model year. This included having 100% of new passenger vehicle sales to meet zero emission standards by 2035. 
This analysis shows the growth of Zero Emission Vehicles (ZEVs) registration and charging stations in the State of California from 2020 to 2025. It examines the infrastructure gaps that may affect owners of ZEVs. 


## Key Questions This Project Can Help Answer
+ How has Zero Emission Vehicle (ZEV) adoption grown across California from 2020 to 2026?
+ Is charging infrastructure keeping pace with ZEV adoption across different regions in California?


## Input Data
### ZEV Registration Data for 2020 through 2025
+ Obtained from the California Open Data Portal
+ Data Course: [Califronia ZEV Registration Data in 2025](https://data.ca.gov/dataset/vehicle-fuel-type-count-by-zip-code/resource/b459d957-5d94-4b10-999d-770419870364)
+ Data includes the number of vehicles located within a zip code jurisdiction, fuel type of the vehicle(s), and zip code

### ZEV Open Public Charging Station Data
+ Obtained from the US Department of Energy: Alternative Fuels Data Center
+ Data Source: [Department of Energy Alternative Fuel Data](https://afdc.energy.gov/data_download)
+ Data shows all alternative fuel stations. Isolate this down to electric battery and hydrogran charging stations only. These are the Zero Emissions Vehicles.
+ Includes station fuel type, state, zip code, and geographic coordinates (longitude and latitude).

### Geographic Boundary Data
+ Obtained from US Census Bureau's 2025 TIGER/Line Shapefiles
+ Data Source: [US Census TIGER/Line Shapefiles](https://www.census.gov/cgi-bin/geo/shapefiles/index.php))
+ Provides detailed geographic boundary data for the State of California 
+ Shows the state broken down into zip codes
+ Used for geospatial analysis and visualization of charging infrastructure distribution


## What Each Script Does
Vehicle Registration Analysis

zev_registration_filter.py: 
 + Reads multiple yearly vehicle registration files, cleans column names, and standardizes key fields (ZIP, fuel type, vehicles, date).
 + Converts dates to extract the registration year and removes invalid or missing date entries.
 + Filters data to include only Battery Electric and Hydrogen Fuel Cell vehicles, excluding out-of-state (“OOS”) ZIP codes.
 + Combines all cleaned datasets into one file and saves the result as ZEVs_filtered.csv.


registration_analysis.py:
+ Read Vehicle Registration Data (ZEVs_filtered.csv)
+ Generate descriptive statistics and visualizations:
    + Bar charts showing top 10 zip codes for registration types and counts in 2025
        + Include count labels
    + Create heatmap showing registrations by Zip Code and year


ZEV Charging Station Analysis

stat_filter.py:
 + Reads six yearly CSV files (2020–2025), adds a Year column to each, and combines them into one dataset.
 + Filters the data to include only stations in California (CA) with fuel types ELEC (electric) or HY (hydrogen).
 + Selects a subset of columns: Year, Fuel Type Code, ZIP, and Station Name.
 + Exports the cleaned and filtered dataset to a new CSV file named stations_2020_2025.csv.


stat_analysis.py:

 + Bar chart showing top 10 zip codes for charger station counts
+ Spatial Analysis
    + Heat map showing growth of charger stations over time (2020-2025)
 


## Visualizations: Maps and Plots

1. Top 10 Zip Codes of ZEV Registrations in 2025

![Top 10 Zip Codes of Fuel Hydrogran Cell and Electric Battery Vehicle Registrations in 2025](https://github.com/kerriroseriley/Zero-Emission_Vehicles_in-California/blob/48de6889cd379696a96a97ee7b60659a6a1737e2/outputs/zipcode_registration.png)


1. Top 10 Zip Codes by ZEV Charger Count in 2025

![Top 10 Zip Codes of Fuel Hydrogran Cell and Electric Battery Vehicle Stations in 2025]()


1.  Cumulative ZEV Registration Growth 2020 through 2025

![Cumulative ZEV Registration Growth 2020 through 2025](https://github.com/kerriroseriley/Zero-Emission_Vehicles_in-California/blob/56c73c0e5f3dcbeb6bfd3c38690d9fdf610b304b/outputs/zev_growth_trend.png)


1. Number of Zero Emission Vehicle Chargers Opening in California 2020-2025 by Fuel Type
Graph


1. Number of Zero Emission Vehicles (Hydrogran Fuel Cell and Electric Battery) in California 2020-2025 by Zip Code
Heatmap






## Conclusion and Recommendations






## References
“Advanced Clean Cars.” Advanced Clean Cars, ww2.arb.ca.gov/our-work/programs/drive-forward-light-duty-vehicle-program/advanced-clean-cars. Accessed 11 Apr. 2026. 






