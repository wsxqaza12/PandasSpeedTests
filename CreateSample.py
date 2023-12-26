import pandas as pd
import numpy as np
import os
import argparse

def estimate_df_size(df):
    return round(df.memory_usage(deep=True).sum() / (1024 ** 3), 2)  # GB

def create_large_dataset(target_size_gb, csv_file_path):
    current_size_gb = 0
    chunk_size = 10**6  # 100萬行
    df = pd.DataFrame()

    while current_size_gb < target_size_gb:
        temp_df = pd.DataFrame({
            'group_column': np.random.randint(0, 1000, size=chunk_size),
            'value_column1': np.random.rand(chunk_size),
            'value_column2': np.random.rand(chunk_size)
        })
        
        df = pd.concat([df, temp_df], ignore_index=True)
        current_size_gb = estimate_df_size(df)
        print(f"Current DataFrame size: {current_size_gb} GB")

    df.to_csv(csv_file_path, index=False)
    print(f"DataFrame saved to {csv_file_path}")
    print(f"Total size: {os.path.getsize(csv_file_path) / (1024 ** 3)} GB")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a large dataset for testing.")
    parser.add_argument("--size", type=float, default=5, help="Target size of the dataset in GB.")
    parser.add_argument("--output", type=str, default="large_dataset.csv", help="Path to the output CSV file.")
    
    args = parser.parse_args()
    
    create_large_dataset(args.size, args.output)
