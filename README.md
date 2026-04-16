
# Zero Emission Vehicles and Chargers in California 
#### By Kerri Riley 


Battery Electric Vehicles and Hydrogen Fuel Cell Vehicles are considered zero emission vehicles (ZEVs) as they have no smog-related or Green House Gases (GHG) tailpipe emissions. 

In 2012, The California Air Resource Board (CARB) adopted the Advanced Clean Car I to control motor vehicle emissions through 2025. In 2022, the Advanced Clean Cars II regulations established the next phase which would begin with the 2026 vehicle model year. This included having 100% of new passenger vehicle sales to meet zero emission standards by 2035. 
This analysis shows the growth of Zero Emission Vehicles registration and charging stations in the State of California from 2020 to 2025. It examines the infrastructure gaps that may affect owners of ZEVs. 


## Key Questions This Project Can Help Answer
+ How has Zero Emission Vehicle (ZEV) adoption grown across California from 2020 to 2025?
+ Is charging infrastructure keeping pace with ZEV adoption across different regions in California?


## Input Data
### ZEV Registration Data for 2020 through 2025
+ Obtained from the California Open Data Portal
+ Data Course: [California ZEV Registration Data in 2025](https://data.ca.gov/dataset/vehicle-fuel-type-count-by-zip-code/resource/b459d957-5d94-4b10-999d-770419870364)
+ Downloaded six CSV files containing vehicle registration data by fuel type for the years 2020 through 2025
+ Data includes the number of vehicles located within a zip code jurisdiction, fuel type of the vehicle(s), and zip code

### ZEV Open Public Charging Station Data
+ Obtained from the US Department of Energy: Alternative Fuels Data Center
+ Data Source: [Department of Energy Alternative Fuel Data](https://afdc.energy.gov/data_download)
+ Downloaded six CSV files of all public, open alternative fuel stations in California on December 31 of each year from 2020 to 2025
+ Data shows all alternative fuel stations. Isolate this down to electric battery and hydrogran charging stations only. These are the Zero Emissions Vehicles.
+ Includes station fuel type, state, and zip code, and variable created for the year.

### Geographic Boundary Data
+ Obtained from US Census Bureau's 2025 TIGER/Line Shapefiles
+ Data Source: [US Census TIGER/Line Shapefiles](https://www.census.gov/cgi-bin/geo/shapefiles/index.php))
+ Provides detailed geographic boundary data for the State of California 
+ Shows the state broken down into zip codes
+ Used for geospatial analysis and visualization of charging infrastructure distribution


## What Each Script Does
Vehicle Registration Analysis

zev_registration_filter.py: 
+ Reads six yearly vehicle registration CSV files (2020-2025), cleans column names, and standardizes key fields (ZIP, fuel type, vehicles, date).
+ Cleans the data by fixing ZIP codes, removing invalid entries, and converting vehicle counts to numeric values.
+ Filters the dataset to include only Battery Electric and Hydrogen Fuel Cell vehicles.
+ Combines all years into one dataset and saves the result as a single filtered CSV file.


registration_analysis.py:
+ Loads and cleans the filtered ZEV dataset, ensuring consistent data types for year, fuel type, ZIP codes, and vehicle counts.
+ Aggregates registrations by year and fuel type to analyze growth trends over time.
+ Generates and saves line charts showing registration growth for Battery Electric and Hydrogen Fuel Cell vehicles (2020–2025).
+ Identifies top 10 ZIP codes by registrations for each fuel type and creates corresponding bar charts.


ZEV Charging Station Analysis

stat_filter.py:
+ Loads six yearly station datasets (2020–2025), adds a year column to each, and combines them into one dataset.
+ Cleans key fields by standardizing state and fuel type values.
+ Filters the data to include only California stations offering electric (ELEC) and hydrogen (HY) charging.
+ Selects relevant columns and saves the final dataset as a single CSV file.


stat_analysis.py:
+ Loads and cleans the combined charging station dataset, standardizing fuel types, ZIP codes, and year values.
+ Aggregates the number of stations by year and fuel type (electric and hydrogen).
+ Generates a line chart showing growth in electric charging stations over time.
+ Generates a second line chart showing growth in hydrogen fueling stations over time.

 
Infrastructure Analysis
 
merged.py
+ Loads and cleans vehicle registration and charging station datasets, standardizing ZIP codes and numeric fields.
+ Filters both datasets to 2025 and separates Battery Electric and Hydrogen Fuel Cell data.
+ Aggregates vehicle counts and station counts by ZIP code for each fuel type.
+ Merges datasets and calculates vehicles-per-station ratios, then saves results for electric and hydrogen separately.

map.py
+ Loads electric and hydrogen vehicle ratio datasets and cleans ZIP codes for consistent spatial matching.
+ Loads U.S. ZIP Code Tabulation Areas and state boundaries, then clips ZIP geometries to California.
+ Joins ZEV ratio data to California ZIP geometries, creating geospatial datasets for electric and hydrogen metrics.
+ Exports the results as GeoPackage files, including a California base layer and two ZEV ratio spatial layers.

## Visualizations: Maps and Plots

1. Top 10 Zip Codes of Battery Electric Vehicles Registrations in 2025
![Top 10 Zip Codes of Electric Battery Vehicle Registrations in 2025](https://github.com/kerriroseriley/Zero-Emission_Vehicles_in-California/blob/d8f3a21ad885223bd9c5422fe74612c50f48035b/outputs/bev_zip_top10.png)

1. Top 10 Zip Codes of Hydrogen Fuel Cell Vehicle Registrations in 2025
![Top 10 Zip Codes of Hydrogen Fuel Cell Vehicle Registrations in 2025](https://github.com/kerriroseriley/Zero-Emission_Vehicles_in-California/blob/d8f3a21ad885223bd9c5422fe74612c50f48035b/outputs/h2_zip_top10.png)

1. Top 10 Zip Codes by Electric and Hydrogen Fuel Cell Vehicle Charger Count in 2025
![Top 10 Zip Codes of Electric Battery and Hydrogen Fuel Cell Vehicle Stations in 2025](https://github.com/kerriroseriley/Zero-Emission_Vehicles_in-California/blob/36542493e783044790609cbcfcbfc05c47daeaf2/outputs/top10_zip_charger_stations.png)

1. Growth of Electric Battery Stations 2020-2025
![Growth of Electric Battery Stations 2020-2025](https://github.com/kerriroseriley/Zero-Emission_Vehicles_in-California/blob/bed575d444fda91a00b829992250f859d935ce05/outputs/elec_growth.png)

1. Growth of Hydrogen Fuel Cell Battery Stations 2020-2025
![Growth of Hydrogen Fuel Cell Stations 2020-2025](https://github.com/kerriroseriley/Zero-Emission_Vehicles_in-California/blob/bed575d444fda91a00b829992250f859d935ce05/outputs/hy_growth.png)

1. Growth of Electric Battery Vehicle Registrations 2020-2025
![Growth of Electric Battery Vehicle Registrations 2020-2025](https://github.com/kerriroseriley/Zero-Emission_Vehicles_in-California/blob/8e0c980ebed9b70a630a3ba5d80978c5b1faff2f/outputs/bev_growth.png)

1. Growth of Hydrogen Fuel Cell  Vehicle Registrations 2020-2025
![Growth of Hydrogen Fuel Cell Vehicle Registrations 2020-2025](https://github.com/kerriroseriley/Zero-Emission_Vehicles_in-California/blob/84e18c6905bc00449dae3d2ec0b0f7ab9f917383/outputs/h2_growth.png)

1. Battery Electric Vehicle Registration to Station Ratio by ZIP Code
![Battery Electric Vehicle Registration to Station Ratio](https://github.com/kerriroseriley/Zero-Emission_Vehicles_in-California/blob/8848e80c51d9461f0de5506eb1c8111b6af08d7b/outputs/zev.png)
Classification method: Equal Counts (Quartiles) 

Equal Counts (Quartiles) classification was used to map the vehicle-to-station ratio for Battery Electric Vehicles (BEVs). This method divides the data into classes containing an equal number of observations, allowing for consistent comparison across regions.

BEV charging infrastructure is relatively widespread and more evenly developed, resulting in a smoother distribution of vehicle-to-station ratios. Using quartiles ensures that the data are evenly represented across classes and prevents the map from being dominated by a small number of high or low values. This approach is particularly useful for highlighting relative differences and ranking areas in terms of infrastructure availability.

1.Hydrogen Fuel Cell Vehicle to Station Ratio by ZIP Code
![Hydrogen Fuel Cell Vehicle to Station Ratio](https://github.com/kerriroseriley/Zero-Emission_Vehicles_in-California/blob/b3ee8ddc565b9d189e843b72c79cdd8bb3b3a01e/outputs/hydrogen_map.png)
Classification method: Natural Breaks (Jenks)
 
The Natural Breaks (Jenks) classification method was used to map the vehicle-to-station ratio for Hydrogen Fuel Cell Vehicles. This method identifies natural groupings in the data by minimizing variation within classes and maximizing differences between them.

Hydrogen infrastructure is sparse and unevenly distributed, with significant disparities between regions. As a result, the data exhibit clustering and potential outliers. The Jenks method is well-suited to this type of distribution, as it highlights meaningful gaps and emphasizes areas with particularly high or low vehicle-to-station ratios, providing a more accurate representation of infrastructure inequality.

## Conclusion and Recommendations
This project analyzes trends in Zero Emission Vehicle (ZEV) registrations alongside the spatial distribution and growth of charging infrastructure across ZIP codes in California, with a focus on 2025. By combining vehicle registration data with station availability, the analysis highlights how adoption and infrastructure development are not always aligned geographically.

Key findings show a strong increase in Battery Electric Vehicle (BEV) registrations, particularly between 2021 and 2022, reflecting a rapid acceleration in consumer adoption of electric vehicles during that period. In contrast, hydrogen fuel cell vehicle growth remains comparatively limited and concentrated in fewer areas. While charging infrastructure has expanded over time, the growth is uneven across ZIP codes, resulting in clear disparities between regions with high EV adoption and those with limited charging access.

In several ZIP codes, vehicle adoption has outpaced the development of charging infrastructure, creating potential bottlenecks for continued ZEV adoption. This mismatch suggests that infrastructure expansion has not consistently kept pace with demand, particularly in high-growth EV regions.

For Policy Makers and Planners in California:
 + Targeted infrastructure planning and development: Investments in zero-emission vehicle infrastructure should focus on ZIP codes where ZEV charger availability is disproportionately low compared to the number of registered zero-emission vehicles.
 + Addressing these gaps would improve accessibility and more equitable EV adoption across regions 

## References
“Advanced Clean Cars.” Advanced Clean Cars, ww2.arb.ca.gov/our-work/programs/drive-forward-light-duty-vehicle-program/advanced-clean-cars. Accessed 11 Apr. 2026. 

“Hydrogen in Transportation.” EPA, Environmental Protection Agency, www.epa.gov/greenvehicles/hydrogen-transportation. Accessed 14 Apr. 2026. 

Resolution 22-12. California Air Resources Board. State of California, 25 Aug. 2022, ww2.arb.ca.gov/sites/default/files/barcu/board/books/2022/082522/prores22-12.pdf.



