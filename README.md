# Solar_Disaggregation
# Overview 
This project takes the net load data measured by smart meters and other widely available environmental measurements (e.g., publicly monitored solar irradiance and temperature) as inputs, and disaggregate the net load traces into BTM solar generation, and regular (non-EV) load traces. Notably, the developed algorithms do not rely on any separately metered data of solar generation behind the smart meters. Rather, novel methods that effectively exploit the temporal correlations and cross-customer correlations of the customers' energy consumption are developed to achieve accurate BTM solar estimation. The disaggregation result is evaluated by three metrics: MSE, MASE, CV.
# How to use
Before using the code, all the input data and variables should be prepared. 
**For solar disaggregation for aggregated customer**, two files are needed: aggregated_withsolar.csv and aggregated_withoutsolar.csv. 

The first file (i.e., aggregated_withsolar.csv) contains:
1. Time information 
   - dayofyear: the day of the year (between 1 and 366)
   - timeofday: the hour of the day (between 0 and 23)
   - minute: minute of the hour
  
2. Load information
   - solar: the groud truth of solar generation of the aggregate PV-customer (only used in validation)
   - grid: the netload of the aggregate PV-customer 
   - consumption: the (total) load of the aggregate PV-customer (= solar + grid)
  
3. Other physical inputs. (obtained from NSRDB dataset)
   - temperature: temperature at the given time index
   - zenith: zenith angle of the sun
   - DHI: diffuse horizontal irradiance
   - DNI: direct horizotal irradiance
   - GHI: global horizontal irradiance

The second file (i.e., aggregated_withoutsolar.csv) contains:

1. Time information 
   - dayofyear: the day of the year (between 1 and 366)
   - timeofday: the hour of the day (between 0 and 23)
   - minute: minute of the hour

2. Load information
   - consumption: the (total) load of the aggregate non-PV customer (= solar + grid)

3. Other physical inputs. (obtained from NSRDB dataset)
   - DHI: diffuse horizontal irradiance
   - DNI: direct horizotal irradiance
   - GHI: global horizontal irradiance

**For solar disaggregation for individual customer**, two files are needed: withsolar_ori.csv and withoutsolar_ori.csv. 
The first file (i.e., withsolar_ori.csv) contains:

1. customer id 
   - dataid: id of PV-customer

2. local time
   - local_15min: time index (format: yyyy/mm/dd HH:MM)

3. Load information
   - use: (total) load of that PV-customer
   - gen: ground truth of solar generation of that PV-customer
   - grid: netload of that PV-customer
 
 The second file (i.e., withoutsolar_ori.csv) contains:

1. customer id 
   - dataid: id of non-PV customer

2. local time
   - local_15min: time index (format: yyyy/mm/dd HH:MM)

3. Load information
   - use: (total) load of that non-PV customer

# Perform solar disaggregation

**The number of solar cusoters and nonsolar customers, the approximate latitude and longitude of the customer location are needed to be specified to perform the aggregate disaggregation.**

1. Run Solar_disaggregation_aggregated_supervised_TX.ipynb to perform aggregate solar disaggregation under the supervised framework.
2. Run Solar_disaggregation_aggregated_unsupervised_TX.ipynb to perform aggregate solar disaggregation by using our proposed similarity based unsupervised method.

**The customer id of the individual customer, the approximate latitude and longitude of the customer location are needed to be specified to perform the indidual solar disaggregation.**

1. Run Solar_disaggregation_individual_unsupervised_TX.ipynb to perform individual solar disaggregation by using our proposed similarity based unsupervised method.

# Summary of the output
The three ipynb will return csv files with one additional column called "prediction" which is the estimated solar generation, one additional column called "load" which is the estimated (total) consumption (i.e., the estimated solar generation + netload).

