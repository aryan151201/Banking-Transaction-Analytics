import pandas as pd
import os

# -----------------------------
# LOAD DATA
# -----------------------------

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

file_path = os.path.join(
    project_dir,
    "data",
    "raw",
    "banking_transactions.csv"
)

df = pd.read_csv(file_path)

print("=" * 60)
print("BANKING TRANSACTION DATA QUALITY ANALYSIS")
print("=" * 60)


# -----------------------------
# 1. BASIC INFORMATION
# -----------------------------

print("\n1. DATASET SHAPE")
print("-" * 40)

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])


# -----------------------------
# 2. COLUMN INFORMATION
# -----------------------------

print("\n2. COLUMN INFORMATION")
print("-" * 40)

print(df.info())


# -----------------------------
# 3. MISSING VALUES
# -----------------------------

print("\n3. MISSING VALUES")
print("-" * 40)

missing_values = df.isnull().sum()

print(missing_values)


# -----------------------------
# 4. DUPLICATE RECORDS
# -----------------------------

print("\n4. DUPLICATE RECORDS")
print("-" * 40)

duplicates = df.duplicated().sum()

print("Duplicate rows:", duplicates)


# -----------------------------
# 5. UNIQUE TRANSACTION IDs
# -----------------------------

print("\n5. TRANSACTION ID CHECK")
print("-" * 40)

unique_ids = df["transaction_id"].nunique()

print("Total transaction IDs:", unique_ids)
print("Total rows:", len(df))

if unique_ids == len(df):
    print("All transaction IDs are unique.")
else:
    print("Duplicate transaction IDs found!")


# -----------------------------
# 6. TRANSACTION STATUS
# -----------------------------

print("\n6. TRANSACTION STATUS")
print("-" * 40)

print(df["status"].value_counts())


# -----------------------------
# 7. TRANSACTION TYPE
# -----------------------------

print("\n7. TRANSACTION TYPE")
print("-" * 40)

print(df["transaction_type"].value_counts())


# -----------------------------
# 8. FAILURE REASONS
# -----------------------------

print("\n8. FAILURE REASONS")
print("-" * 40)

print(df["failure_reason"].value_counts(dropna=False))


# -----------------------------
# 9. NUMERIC SUMMARY
# -----------------------------

print("\n9. NUMERIC SUMMARY")
print("-" * 40)

print(df[[
    "amount",
    "processing_time_seconds"
]].describe())


# -----------------------------
# 10. CATEGORICAL VALUES
# -----------------------------

print("\n10. UNIQUE VALUES")
print("-" * 40)

print("Banks:", df["sender_bank"].nunique())
print("Regions:", df["region"].nunique())
print("Channels:", df["channel"].nunique())
print("Transaction Types:", df["transaction_type"].nunique())


print("\n" + "=" * 60)
print("DATA QUALITY ANALYSIS COMPLETED")
print("=" * 60)