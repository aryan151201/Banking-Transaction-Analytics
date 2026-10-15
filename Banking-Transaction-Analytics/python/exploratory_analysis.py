import pandas as pd
import os

# -----------------------------
# LOAD DATA
# -----------------------------

project_dir = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

file_path = os.path.join(
    project_dir,
    "data",
    "raw",
    "banking_transactions.csv"
)

df = pd.read_csv(file_path)


# -----------------------------
# TRANSACTION STATUS ANALYSIS
# -----------------------------

status_counts = df["status"].value_counts()

print("\nTRANSACTION STATUS")
print("-" * 40)

print(status_counts)


# -----------------------------
# STATUS PERCENTAGE
# -----------------------------

status_percentage = (
    df["status"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)

print("\nTRANSACTION STATUS PERCENTAGE")
print("-" * 40)

print(status_percentage)



# -----------------------------
# NEFT VS RTGS PERFORMANCE
# -----------------------------

type_status = pd.crosstab(
    df["transaction_type"],
    df["status"]
)

print("\nNEFT VS RTGS TRANSACTION STATUS")
print("-" * 40)

print(type_status)


# -----------------------------
# SUCCESS RATE
# -----------------------------

success_rate = (
    df.groupby("transaction_type")["status"]
    .apply(lambda x: (x == "SUCCESS").mean() * 100)
    .round(2)
)

print("\nSUCCESS RATE BY TRANSACTION TYPE")
print("-" * 40)

print(success_rate)


# -----------------------------
# BANK FAILURE RATE
# -----------------------------

bank_failure_rate = (
    df.groupby("sender_bank")
    .apply(
        lambda x: (
            (x["status"] != "SUCCESS").mean() * 100
        ),
        include_groups=False
    )
    .round(2)
    .sort_values(ascending=False)
)

print("\nBANK FAILURE RATE")
print("-" * 40)

print(bank_failure_rate)


# -----------------------------
# FAILURE REASON ANALYSIS
# -----------------------------

failed_transactions = df[
    df["status"] != "SUCCESS"
]

failure_reasons = (
    failed_transactions["failure_reason"]
    .value_counts()
)

failure_percentage = (
    failed_transactions["failure_reason"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)

print("\nFAILURE REASONS")
print("-" * 40)

print(failure_reasons)

print("\nFAILURE REASON PERCENTAGE")
print("-" * 40)

print(failure_percentage)

# -----------------------------
# PROCESSING TIME BY STATUS
# -----------------------------

processing_analysis = (
    df.groupby("status")["processing_time_seconds"]
    .agg(["count", "mean", "median", "min", "max"])
    .round(2)
)

print("\nPROCESSING TIME BY TRANSACTION STATUS")
print("-" * 60)

print(processing_analysis)


# -----------------------------
# TRANSACTION AMOUNT BY TYPE
# -----------------------------

amount_analysis = (
    df.groupby("transaction_type")["amount"]
    .agg(["count", "mean", "median", "min", "max"])
    .round(2)
)

print("\nTRANSACTION AMOUNT BY TYPE")
print("-" * 60)
print(amount_analysis)

# -----------------------------
# DAILY TRANSACTION VOLUME
# -----------------------------

df["transaction_date"] = pd.to_datetime(df["transaction_date"])

daily_transactions = (
    df.groupby("transaction_date")
      .size()
      .reset_index(name="transaction_count")
)

print("\nDAILY TRANSACTION VOLUME")
print("-" * 60)
print(daily_transactions.head(10))
print("\nTotal Days:", daily_transactions["transaction_date"].nunique())
print("Average Transactions per Day:", round(daily_transactions["transaction_count"].mean(), 2))
print("Maximum Transactions in a Day:", daily_transactions["transaction_count"].max())
print("Minimum Transactions in a Day:", daily_transactions["transaction_count"].min())

print("\nBUSIEST DAYS")
print("-" * 60)

print(
    daily_transactions
    .sort_values("transaction_count", ascending=False)
    .head(5)
)

print("\nLOWEST VOLUME DAYS")
print("-" * 60)

print(
    daily_transactions
    .sort_values("transaction_count")
    .head(5)
)