
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




## Pie Chart
#### 1. Breakdown of Zero Emission Vehicle Registration Types in California in 2025
![Pie Chart of Battery Electric to Hydrogen Fuel Cell Vehicle Registrations in 2025](https://github.com/kerriroseriley/Zero-Emission_Vehicles_in-California/blob/2430d9255d085fcd8542a07b89867dc83e2d0e4c/outputs/zev_share_pie_2025.png)
+ This pie chart shows that Battery Electric Vehicles dominate the ZEV industry with 99.1%, or about 1.4 million ZEV registrations, of zero emission vehicles being Battery Electric Vehicles
## Visualizations: Battery Electric
    
    
#### 2. Top 10 ZIP Codes of Battery Electric Vehicle Stations in 2025
![Top 10 ZIP Codes of Electric Battery Vehicle Stations](https://github.com/kerriroseriley/Zero-Emission_Vehicles_in-California/blob/4b2a1f1e1396dd0fa175ea24fab5d9fd9b8f67fe/outputs/elec_top10_zip_charger_stations.png)
+ The top 10 ZIP Codes had a range of 432 to 1,413 battery electic charging stations
    
    
#### 3. Top 10 Zip Codes of Battery Electric Vehicles Registrations in 2025
![Top 10 Zip Codes of Electric Battery Vehicle Registrations in 2025](https://github.com/kerriroseriley/Zero-Emission_Vehicles_in-California/blob/61eb9fd686c60a70472676d6afe90142de5074ce/outputs/bev_zip_top10.png)
+ The top 10 ZIP Codes had a range of 22,015 to 31,909 EV registrations in 2025


#### 4. Growth of Electric Battery Stations 2020-2025
![Growth of Electric Battery Stations 2020-2025](https://github.com/kerriroseriley/Zero-Emission_Vehicles_in-California/blob/bed575d444fda91a00b829992250f859d935ce05/outputs/elec_growth.png)
+ Overall, positive growth in electric battery stations from 2020 to 2025
    + There was a 11,963 increase in the number of electic battery vehicle stations from 2020 to 2025 in California 
+ Major growth from 2020 to 2021 in stations (6,759 stations added)
+ 2021 to 2022, there was minimal change the number of Electric charging stations (Reduction of 20 EV stations)
+ 2022 to 2025, there was moderate growth

#### 5. Growth of Electric Battery Vehicle Registrations 2020-2025
![Growth of Electric Battery Vehicle Registrations 2020-2025](https://github.com/kerriroseriley/Zero-Emission_Vehicles_in-California/blob/a0779ddde01cfd2282bba2e91ecb5ae64fe13e51/outputs/bev_growth.png)
+ Exponential growth of Electric Battery Vehicle Registrations in California 
+ From 2020 to 2025, there was an 1,139,496 increase in the number of electric battery vehicle registrations in the State of California

#### 6. Battery Electric Vehicle Registration to Station Ratio by ZIP Code
![Battery Electric Vehicle Registration to Station Ratio](https://github.com/kerriroseriley/Zero-Emission_Vehicles_in-California/blob/e9e5f319f7837db1a8b6fae485b160fd7bb4ba91/outputs/zev.png)
Missing ZIP codes in the heat map are not errors but result from how the data and geographic boundaries are defined and processed. The analysis combines vehicle registrations, charging station data, and Census ZCTA geometries, and a ZIP code will only appear with a value if it exists in at least one dataset. Areas with no recorded vehicles or stations therefore do not produce values and appear blank. In addition, USPS ZIP codes do not perfectly align with Census ZCTAs, so some ZIP codes in the data have no matching geographic polygon and are excluded during mapping. Further filtering steps, such as removing out-of-state entries, standardizing ZIP formats, and restricting the analysis to California, also eliminate some records. Finally, ZIP codes with zero charging stations yield undefined vehicle-to-station ratios, which are intentionally represented as missing values on the map.


Classification method: Equal Counts (Quartiles) 

+ Equal Counts (Quartiles) classification was used to map the vehicle-to-station ratio for Battery Electric Vehicles (BEVs). This method divides the data into classes containing an equal number of observations, allowing for consistent comparison across regions.

+ BEV charging infrastructure is relatively widespread and more evenly developed, resulting in a smoother distribution of vehicle-to-station ratios. Using quartiles ensures that the data are evenly represented across classes and prevents the map from being dominated by a small number of high or low values. This approach is particularly useful for highlighting relative differences and ranking areas in terms of infrastructure availability.



## Visualizations: Hydrogen Fuel Cell Vehicles 

#### 7. Top 10 Zip Codes by Hydrogen Fuel Cell Vehicle Charger Count in 2025
![Top 10 Zip Codes of Hydrogen Fuel Cell Vehicle Stations in 2025](https://github.com/kerriroseriley/Zero-Emission_Vehicles_in-California/blob/4b2a1f1e1396dd0fa175ea24fab5d9fd9b8f67fe/outputs/h2_top10_zip_charger_stations.png)
+ The top 10 ZIP Codes had a range of 5 to 9 Hydrogen Fuel Cell charging stations

#### 8. Top 10 Zip Codes of Hydrogen Fuel Cell Vehicle Registrations in 2025
![Top 10 Zip Codes of Hydrogen Fuel Cell Vehicle Registrations in 2025](https://github.com/kerriroseriley/Zero-Emission_Vehicles_in-California/blob/61eb9fd686c60a70472676d6afe90142de5074ce/outputs/h2_zip_top10.png)
+ The top 10 ZIP Codes had a range of 334 to 564 HFC registrations in 2025

#### 9. Growth of Hydrogen Fuel Cell Battery Stations 2020-2025
![Growth of Hydrogen Fuel Cell Stations 2020-2025](https://github.com/kerriroseriley/Zero-Emission_Vehicles_in-California/blob/bed575d444fda91a00b829992250f859d935ce05/outputs/hy_growth.png)
+ Positive growth in Hydrogen Fuel Cell charging stations from 2020 to 2023
+ In 2023, we see a downward shift continuing through to 2025
+ This was a decrease from 59 to 50 charging stations in California
+ Overall, there was an increase of 7 HFC charging stations in California

#### 10. Growth of Hydrogen Fuel Cell Vehicle Registrations 2020-2025
![Growth of Hydrogen Fuel Cell Vehicle Registrations 2020-2025](https://github.com/kerriroseriley/Zero-Emission_Vehicles_in-California/blob/8fd2d2e4e8120d2a5b45e65e421debae4f94180f/outputs/h2_growth.png)
+ Growth in Hydrogen Fuel Cell vehicle registrations from 2020 to 2024
+ In 2025, a sharp  decline downwardsin HFC vehicle regstration in California
    + This was likely a market response to the reduciton in Hydrogen Fuel Cell stations we saw in 2023-2025
+ In 5 years, there was a 6,608 increase in the number of Hydrogen Fuel Cell Vehicle Registrations in California


#### 11. Hydrogen Fuel Cell Vehicle to Station Ratio by ZIP Code
![Hydrogen Fuel Cell Vehicle to Station Ratio](https://github.com/kerriroseriley/Zero-Emission_Vehicles_in-California/blob/e9e5f319f7837db1a8b6fae485b160fd7bb4ba91/outputs/hydrogen_ratio.png)
Classification method: Natural Breaks (Jenks)
 
+ The Natural Breaks (Jenks) classification method was used to map the vehicle-to-station ratio for Hydrogen Fuel Cell Vehicles. This method identifies natural groupings in the data by minimizing variation within classes and maximizing differences between them.

+ Hydrogen infrastructure is sparse and unevenly distributed, with significant disparities between regions. As a result, the data exhibit clustering and potential outliers. The Jenks method is well-suited to this type of distribution, as it highlights meaningful gaps and emphasizes areas with particularly high or low vehicle-to-station ratios, providing a more accurate representation of infrastructure inequality.

## Conclusion and Recommendations
This project analyzes trends in Zero Emission Vehicle (ZEV) registrations alongside the spatial distribution and growth of charging infrastructure across ZIP codes in California, with a focus on 2025. By combining vehicle registration data with station availability, the analysis highlights how adoption and infrastructure development are not always aligned geographically.
Key findings show a strong and sustained increase in Battery Electric Vehicle (BEV) registrations, particularly between 2021 and 2022, reflecting a clear market preference and rapid acceleration in consumer adoption. In contrast, hydrogen fuel cell vehicle growth remains comparatively limited and concentrated in fewer areas, indicating weaker market uptake. This divergence suggests that consumers are overwhelmingly favoring BEVs over alternative zero-emission technologies. While charging infrastructure has expanded over time, the growth is uneven across ZIP codes, resulting in clear disparities between regions with high EV adoption and those with limited charging access.
In several ZIP codes, vehicle adoption has outpaced the development of charging infrastructure, creating potential bottlenecks for continued ZEV adoption. This mismatch suggests that infrastructure expansion has not consistently kept pace with demand—particularly in high-growth BEV regions, where the need for reliable and accessible charging is most urgent.
For Policy Makers and Planners in California:
Targeted infrastructure planning and development: Investments in zero-emission vehicle infrastructure should prioritize the expansion of BEV charging networks in ZIP codes where charger availability is disproportionately low relative to BEV registrations. Given strong and growing consumer demand for BEVs, infrastructure deployment should align with this market reality rather than be evenly distributed across technologies with unequal adoption.
Strategic prioritization of BEV ecosystems: Policymakers and infrastructure developers should place greater emphasis on scaling BEV-supporting infrastructure, as current trends indicate that BEVs will continue to dominate ZEV adoption. Concentrating resources on BEV charging networks will maximize impact, reduce adoption bottlenecks, and more effectively support California’s emissions reduction goals.
Addressing these gaps would improve accessibility, support continued growth in BEV adoption, and promote more equitable access to zero-emission transportation across regions.

## References
“Advanced Clean Cars.” Advanced Clean Cars, ww2.arb.ca.gov/our-work/programs/drive-forward-light-duty-vehicle-program/advanced-clean-cars. Accessed 11 Apr. 2026. 

“Hydrogen in Transportation.” EPA, Environmental Protection Agency, www.epa.gov/greenvehicles/hydrogen-transportation. Accessed 14 Apr. 2026. 

Resolution 22-12. California Air Resources Board. State of California, 25 Aug. 2022, ww2.arb.ca.gov/sites/default/files/barcu/board/books/2022/082522/prores22-12.pdf.



