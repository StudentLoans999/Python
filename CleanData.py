# An example of using pandas to remove missing values, outliers, and duplicate data

pip install pandas # install the 'pandas' library
import pandas as pd # import the necessary library

# Create a sample DataFrame ('df' with columns 'A', 'B', and 'C', containg some missing values)

data = {
    'A': [1, 2, 3, 4, None, 6, 7, 8, 9],
    'B': [10, 11, 12, 13, 14, 15, 16, 17, 18],
    'C': [19, 20, 21, 22, 23, 24, 25, None, 27]
}

df = pd.DataFrame(data)

# Display the original DataFrame

print("Original DataFrame:")
print(df)

df_cleaned = df.dropna() # drop missing values

# Remove outliers (defines a lower and upper bound based on mean and standard deviation, and then removes rows from df_cleaned where values fall outside this range)

lower_bound = df_cleaned.mean() - 2 * df_cleaned.std()
upper_bound = df_cleaned.mean() + 2 * df_cleaned.std()

df_cleaned = df_cleaned[(df_cleaned >= lower_bound) & (df_cleaned <= upper_bound)]

df_cleaned = df_cleaned.drop_duplicates() # remove duplicate rows

# Display the cleaned DataFrame

print("\nCleaned DataFrame:")
print(df_cleaned)
