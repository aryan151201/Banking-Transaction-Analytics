import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# -----------------------------
# SETTINGS
# -----------------------------

NUM_TRANSACTIONS = 50000

np.random.seed(42)
random.seed(42)

# -----------------------------
# MASTER DATA
# -----------------------------

banks = [
    "HDFC Bank",
    "ICICI Bank",
    "SBI",
    "Axis Bank",
    "Kotak Bank",
    "Yes Bank",
    "IndusInd Bank",
    "Bank of Baroda",
    "Punjab National Bank",
    "IDFC First Bank"
]

transaction_types = ["NEFT", "RTGS"]

channels = [
    "Internet Banking",
    "Mobile Banking",
    "Branch",
    "Corporate Banking"
]

regions = [
    "Mumbai",
    "Pune",
    "Navi Mumbai",
    "Thane",
    "Delhi",
    "Bangalore",
    "Hyderabad",
    "Chennai",
    "Kolkata",
    "Ahmedabad"
]

success_status = ["SUCCESS", "FAILED", "REJECTED"]

failure_reasons = [
    "RBI_REJECT",
    "IFTAS_REJECT",
    "TIMEOUT",
    "INSUFFICIENT_FUNDS",
    "INVALID_ACCOUNT",
    "TECHNICAL_ERROR",
    "DUPLICATE_TRANSACTION"
]

# -----------------------------
# GENERATE TRANSACTIONS
# -----------------------------

start_date = datetime(2026, 1, 1)

data = []

for i in range(1, NUM_TRANSACTIONS + 1):

    transaction_id = f"TX{i:06d}"

    transaction_date = start_date + timedelta(
        days=random.randint(0, 273)
    )

    transaction_time = (
        datetime.min
        + timedelta(
            hours=random.randint(0, 23),
            minutes=random.randint(0, 59),
            seconds=random.randint(0, 59)
        )
    ).time()

    transaction_type = random.choices(
        transaction_types,
        weights=[75, 25]
    )[0]

    sender_bank = random.choice(banks)

    receiver_bank = random.choice(
        [bank for bank in banks if bank != sender_bank]
    )

    # RTGS generally has higher transaction values
    if transaction_type == "RTGS":
        amount = round(
            np.random.uniform(200000, 2000000), 2
        )
    else:
        amount = round(
            np.random.uniform(1000, 200000), 2
        )

    channel = random.choice(channels)

    region = random.choice(regions)

    # -----------------------------
    # TRANSACTION STATUS
    # -----------------------------

    status = random.choices(
        success_status,
        weights=[88, 7, 5]
    )[0]

    if status == "SUCCESS":

        failure_reason = None

        processing_time = round(
            np.random.uniform(1, 30), 2
        )

    else:

        failure_reason = random.choice(
            failure_reasons
        )

        processing_time = round(
            np.random.uniform(10, 120), 2
        )

    data.append([
        transaction_id,
        transaction_date.date(),
        transaction_time,
        transaction_type,
        sender_bank,
        receiver_bank,
        amount,
        status,
        failure_reason,
        processing_time,
        channel,
        region
    ])

# -----------------------------
# CREATE DATAFRAME
# -----------------------------

columns = [
    "transaction_id",
    "transaction_date",
    "transaction_time",
    "transaction_type",
    "sender_bank",
    "receiver_bank",
    "amount",
    "status",
    "failure_reason",
    "processing_time_seconds",
    "channel",
    "region"
]

df = pd.DataFrame(data, columns=columns)

# -----------------------------
# SAVE DATASET
# -----------------------------
import os

# Get the project directory
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create data/raw folder if it doesn't exist
raw_data_dir = os.path.join(project_dir, "data", "raw")
os.makedirs(raw_data_dir, exist_ok=True)

# Save dataset
output_path = os.path.join(raw_data_dir, "banking_transactions.csv")

df.to_csv(output_path, index=False)

print("Dataset created successfully!")
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")
print(f"Saved to: {output_path}")

print("\nFirst 5 records:")
print(df.head())

print("\nTransaction status:")
print(df["status"].value_counts())

print("\nTransaction type:")
print(df["transaction_type"].value_counts())
