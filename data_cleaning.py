import pandas as pd

# Load dataset
df = pd.read_csv("Sample - Superstore.csv", encoding="latin1")

print("Dataset Shape:", df.shape)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Convert date columns
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

# Save cleaned dataset
df.to_csv("cleaned_superstore.csv", index=False)

print("\nData cleaning completed successfully!")