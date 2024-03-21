# TASK: 1. Create some random data with values ranging from 30-109 and a column called 'seconds'
# 2. Create and plot a histogram based on that random data with labels above the highest count of 'seconds'

#import matplotlib.pyplot as plt
#import pandas as pd
#import seaborn as sns
#import numpy as np

# Create DataFrame
data = {'seconds': np.random.randint(30, 110, size=600)} # create df with column 'seconds' consisting of 600 random values between 30 and 109
df = pd.DataFrame(data)

# Create and plot a histogram with seaborn
ax = sns.histplot(df['seconds'], binrange=(40, 100), binwidth=5, color='#4285F4', alpha=1) # uses column 'seconds', bins range from 40-100 and each with a width of 5
ax.set_xticks(range(35, 101, 5)) # sets x-axis tick marks label (starts at 35 and goes to 100 in 5 increments)
ax.set_yticks(range(0, 101, 10))
plt.title('Old Faithful geyser - time between eruptions')

bin_heights = [rect.get_height() for rect in ax.patches] # iterates over each rectangular patch (aka bin) and gets its height
max_height = max(bin_heights) # gets the max of the bin heights

# Add value labels above the top of each bin (based on the height of the tallest bin which is its count)
for i, count in enumerate(bin_heights):
    plt.text((40 + 5*i + 2.5), max_height + 15, str(count), ha='center')

plt.show()
