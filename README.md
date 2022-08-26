# Solar_Disaggregation
# Overview 
This project takes the net load data measured by smart meters and other widely available environmental measurements (e.g., publicly monitored solar irradiance and temperature) as inputs, and disaggregate the net load traces into BTM solar generation, and regular (non-EV) load traces. Notably, the developed algorithms do not rely on any separately metered data of solar generation behind the smart meters. Rather, novel methods that effectively exploit the temporal correlations and cross-customer correlations of the customers' energy consumption are developed to achieve accurate BTM solar estimation. 
# How to use
Before using the code, all the input data and variables should be prepared. 
For solar disaggregation for aggregated customer, two files are needed: aggregated_withsolar.csv and aggregated_withoutsolar.csv. The first file contains:
- Time information 
- Aggregation of grid data, solar data, and total consumption data, of customers with solar panels (solar data is only used to do validation) 
- Other physical inputs. (obtained from NSRDB dataset.) 

The second file contains:
- Time information 
- The aggregation of total consumption data og customers without solar panels 
- Solar irradiance information. 
The number of solar cusoters and nonsolar customers, the approximate latitude and longitude are also required as input variables.

For solar disaggregation for individual customer, two files are needed: withsolar_ori.csv and withoytsolar_ori.csv. 
- The first file contains the load infortion for each solar customer. 
- The second file contains load infortion for each non-solar customer. 
