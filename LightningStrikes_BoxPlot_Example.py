# Create two new columns
df['week'] = df.date.dt.isocalendar().week # week will be between 1-52
df['day_of_the_week'] = df.date.dt.day_name() # day_of_the_week will be Sunday-Saturday

day_of_the_week_order = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'] # define order of days for the plot
