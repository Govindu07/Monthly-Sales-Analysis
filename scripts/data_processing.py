import pandas as pd
import os

def load_sales_data(file_path):
    """Load and preprocess sales data from Excel"""
    df = pd.read_excel(file_path, parse_dates=["Date"])
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df.set_index('Date', inplace=True)
    return df

def monthly_sales_report(df, output_folder="../results"):
    """Calculate monthly sales and save to CSV"""
    os.makedirs(output_folder, exist_ok=True)
    monthly_sales = df['Sales'].resample('M').sum()
    file_path = os.path.join(output_folder, "monthly_sales_report.csv")
    monthly_sales.to_csv(file_path)
    print(f"Monthly sales report saved to {file_path}")
    return monthly_sales
