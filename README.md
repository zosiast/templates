#
templates
Python scripts for doing basic processing, calculations and plotting

## Python template scripts for basic functions
Data used is on netsratch and should be accessible

### Calculations
ch4_burden: sum total atmospheric CH4 in Tg

ch4_lifetime_oh: uses ch4, trop mask, flux of OH_CH4 reaction, airmass to calculate lifetime of ch4 wrt OH

ch4_oh_flux_total: total reaction flux in Tg yr-1

interhem_grad: uses tropospheric mask to calculate tropospheric interhemisphericgradient

trop_mask: uses pressure field to make trop mask

ch4_lifetime_oh: uses ch4, trop mask, flux of OH_CH4 reaction, airmass to calculate lifetime of ch4 wrt OH

excel_to_pandas: reads in excel sheet and exports csv

get_monthly_data_lat_bin: chunk data by month, select seasons, bin by latitude

### Plotting
cf_global_contours: using cf to plot world map of variable. Includes collapse function to mean over time.

lawrence_plot_template: makes bins by latitude and pressure, averages variable over these bins

multiple_scatter_plotted: continuous colour bar over discrete scatter plots

subplot_figs_with_legend: figure with 6 subplots, axes and labels on outside of figure and legend for all subplots is the same

vertical_profile: variable vs altitude, for single latitude, mulitple latitudes and binned latitudes

zonal_mean: zonal mean from netcdf data

tracer_vert_profile_compare: whole script for reading in obs and model data and making plots for each latitude bin, and seasonal analysis.

gantt_chart: make gantt chart. Also using different plot styles
