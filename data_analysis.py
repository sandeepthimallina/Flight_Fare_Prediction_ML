import pandas as pd

# Load the dataset
df = pd.read_csv("data/Freshly_cleaned.csv/Freshly_cleaned.csv")

# -------------------------------
# BASIC DATASET INFORMATION
# -------------------------------

print("=" * 50)
print("FLIGHT FARE DATASET ANALYSIS")
print("=" * 50)

print("\nDataset loaded successfully!")

print("\nNumber of rows:", df.shape[0])
print("Number of columns:", df.shape[1])

# -------------------------------
# COLUMN NAMES
# -------------------------------

print("\nColumn names:")
for column in df.columns:
    print("-", column)

# -------------------------------
# DATA TYPES
# -------------------------------

print("\nData types:")
print(df.dtypes)

# -------------------------------
# MISSING VALUES
# -------------------------------

print("\nMissing values:")
print(df.isnull().sum())

# -------------------------------
# DUPLICATE ROWS
# -------------------------------

print("\nNumber of duplicate rows:")
print(df.duplicated().sum())

# -------------------------------
# PRICE INFORMATION
# -------------------------------

print("\nPrice statistics:")
print(df["price"].describe())

# -------------------------------
# UNIQUE VALUES
# -------------------------------

print("\nUnique values in important columns:")

print("\nAirlines:")
print(df["airline"].unique())

print("\nFrom:")
print(df["from"].unique())

print("\nTo:")
print(df["to"].unique())

print("\nClass:")
print(df["class"].unique())

print("\nStops:")
print(df["stops"].unique())

print("\nMonth:")
print(df["month"].unique())

print("\nAnalysis completed!")