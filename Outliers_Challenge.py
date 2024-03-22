# TASK: 1. Create a df filled with daily dates ranging from years 2020-2024 and assign random values for each date to represent lightning strikes occurring
# 2. Make the df have columns for geographic data: center_point, longitude, latitude
# 3. Make another df that has the same date data to represent lightning strikes occurring but with these other columns: zip code, city, state, state code
# 4. Create a new df by merging the two dataframes together on columns 'date' and 'lightning_strikes'
# 5. Add in some null data to the new df to the columns 'longitude' and 'latitude' in randomly selected rows but make sure both columns don't have a missing value in the same row
# 6. Output the rows that contain missing values
# 7. Fill in the missing values by using the 'center_point_geom' column
# 8. Output the fully updated and fixed df that now doesn't have any missing values (verify that there aren't any missing values left)
# 9. Create and plot a geo graph (use plotly and annotate each data point in the plot) of: Lightning strikes per year (2020-2024) by City in the USA

#pip install matplotlib
#pip install pandas
#pip install seaborn
#pip install datetime
#pip install plotly
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import datetime
import plotly.express as px
