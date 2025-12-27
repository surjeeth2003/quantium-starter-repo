import pandas as pd
from pathlib import Path

# Path to data folder
DATA_DIR = Path("data")

# Read all CSV files in data folder
dfs = []
for csv_file in DATA_DIR.glob("*.csv"):
    df = pd.read_csv(csv_file)
    dfs.append(df)

# Combine all files into one DataFrame
combined_df = pd.concat(dfs, ignore_index=True)

# Filter only Pink Morsels
pink_df = combined_df[combined_df["product"] == "Pink Morsels"].copy()

# Create Sales column
pink_df["Sales"] = pink_df["quantity"] * pink_df["price"]

# Select required columns
final_df = pink_df[["Sales", "date", "region"]]

# Rename columns to match requirement
final_df.columns = ["Sales", "Date", "Region"]

# Save output
output_path = DATA_DIR / "pink_morsels_sales.csv"
final_df.to_csv(output_path, index=False)

print(f"Output written to {output_path}")
