# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 11:35:48 2023

@author: fahmed
"""

# Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Reading a data
total_data = pd.read_csv("work-hrs/Avg_hours_worked_(1950-2017).csv")

# Filtering data by their Region Code (taking 4 countries)
AUS_df = total_data[total_data['RegionCode']=='AUS']
FRA_df = total_data[total_data['RegionCode']=='FRA']
NOR_df = total_data[total_data['RegionCode']=='NOR']
MEX_df = total_data[total_data['RegionCode']=='MEX']

    
# Lineplot
def first_plot():
    """
    This function makes a line plot of 4 countries between Year and Average 
    Worked hours
    """    

    plt.figure(figsize=(9, 6))
    i = np.arange(1950, 2016, 5)
    plt.plot(AUS_df['Year'], AUS_df['AvgHoursWorked'], label= "Australia")
    plt.plot(FRA_df['Year'], FRA_df['AvgHoursWorked'], label= "France")
    plt.plot(NOR_df['Year'], NOR_df['AvgHoursWorked'], label= "Norway")
    plt.plot(MEX_df['Year'], MEX_df['AvgHoursWorked'], label= "Mexico")
    plt.legend()
    plt.title("Average Hours worked for 4 countries")
    plt.xlabel("Years")
    plt.ylabel("Average Hours per year")
    plt.margins(x=0)
    plt.xticks(i, rotation=30)
    plt.show()
    plt.savefig("lineplot.jpeg")
    

# Histogram
def second_plot():
    """
    This funtion makes histograms of same 4 countries 
    """
    
    plt.figure(figsize=(10, 7))
    plt.subplot(2, 2, 1)
    plt.hist(AUS_df['AvgHoursWorked'], label= "Australia", density= True)
    plt.legend()
    plt.margins(x=0)
    plt.subplot(2, 2, 2)
    plt.hist(FRA_df['AvgHoursWorked'], label= "France", density= True) 
    plt.legend()
    plt.subplot(2, 2, 3)
    plt.hist(NOR_df['AvgHoursWorked'], label= "Norway", density= True) 
    plt.legend()
    plt.subplot(2, 2, 4)
    plt.hist(MEX_df['AvgHoursWorked'], label= "Mexico", density= True) 
    plt.legend()
    plt.show()
    plt.savefig("histogram.jpeg")


# Barplot 
def third_plot():
    """
    This function makes barplots of same 4 countries w.r.t Average Worked Hours
    of year 2010
    """
    # Filtering data for year 2010
    AUS_2010 = AUS_df[AUS_df["Year"] == 2010]
    #print(AUS_2010)
    FRA_2010 = FRA_df[FRA_df["Year"] == 2010]
    #print(FRA_2010)
    NOR_2010 = NOR_df[NOR_df["Year"] == 2010]
    #print(NOR_2010)
    MEX_2010 = MEX_df[MEX_df["Year"] == 2010]
    #print(MEX_2010)
    
    X = np.array([AUS_2010["RegionCode"], FRA_2010["RegionCode"], 
                  NOR_2010["RegionCode"], MEX_2010["RegionCode"]]).flatten()
    print(X)
    Y = np.array([AUS_2010["AvgHoursWorked"], FRA_2010["AvgHoursWorked"], 
                  NOR_2010["AvgHoursWorked"], MEX_2010["AvgHoursWorked"]])\
                  .flatten()
    print(Y)
    plt.figure(figsize=(9,5))
    plt.bar(X, Y)
    plt.title("Average Worked Hours in 2010")
    plt.xlabel("COuntries")
    plt.ylabel("Average working Hours")
    plt.show()
    plt.savefig("barplot.jpeg")


    
# Calling all three functions
first_plot()
second_plot()
third_plot()

