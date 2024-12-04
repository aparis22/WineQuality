'''
Author: Andrew Paris Boske & Shawn Burchfield
Class: COMSC.230
Purpose: Organizing unorganized data using SciPy
'''
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from ucimlrepo import fetch_ucirepo 

# Fetch dataset
wine_quality = fetch_ucirepo(id=186) 

# Data (as pandas dataframes)
X = wine_quality.data.features 
Y = wine_quality.data.targets 

# Extract alcohol and quality columns
alcohol_data = X['alcohol'].values.flatten()
pH_data = X['pH'].values.flatten()
quality_data = Y.values.flatten()

# Combine into a DataFrame
data_alcQuality = pd.DataFrame({'alcohol': alcohol_data, 'quality': quality_data})
data_phQuality = pd.DataFrame({'pH': pH_data, 'quality': quality_data})

# Group alcohol values into rounded categories (e.g., nearest integer)
data_alcQuality['alcohol_group'] = data_alcQuality['alcohol'].round()  # Round alcohol content to nearest whole number
data_phQuality['pH_group'] = data_phQuality['pH'].round(1) # Round pH to the nearest tenth

# Group by the amount of times each quality is called
quality_counts_alcohol = data_alcQuality.groupby(['alcohol_group', 'quality']).size().unstack(fill_value=0) # Each time an alcohol level lands in a quality
quality_counts_pH = data_phQuality.groupby(['pH_group', 'quality']).size().unstack(fill_value=0) # Each time a pH level lands in a quality

def alcVsQuality():
    quality_counts_alcohol.plot(
        kind='bar', 
        stacked=True, 
        figsize=(12, 6),
        cmap='tab10',  # Use a color map for better visualization
        edgecolor='black'
    )
    plt.title('Quality Distribution per Alcohol Content')
    plt.xlabel('Alcohol Content')
    plt.ylabel('Count of Quality Scores')
    plt.grid(axis='y', linestyle='--')
    plt.legend(title='Quality Score', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()

# Call the function to display the plot
alcVsQuality()

def phVsQuality():
    quality_counts_pH.plot(
        kind='bar', 
        stacked=True, 
        figsize=(12, 6),
        cmap='tab10',  # Use a color map for better visualization
        edgecolor='black'
    )
    plt.title('Quality Distribution per pH Group (Grouped by Nearest Tenth)')
    plt.xlabel('pH Level (Rounded to Nearest Tenth)')
    plt.ylabel('Count of Quality Scores')
    plt.grid(axis='y', linestyle='--')
    plt.legend(title='Quality Score', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()

# Call the function to display the plot
phVsQuality()