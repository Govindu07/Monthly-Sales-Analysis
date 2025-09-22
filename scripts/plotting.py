import matplotlib.pyplot as plt
import os

def plot_monthly_sales(monthly_sales, output_folder="../results"):
    os.makedirs(output_folder, exist_ok=True)
    plt.figure(figsize=(10,5))
    plt.plot(monthly_sales.index, monthly_sales.values, marker='o', color='blue')
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Total Sales")
    plt.grid(True)
    plt.tight_layout()
    
    file_path = os.path.join(output_folder, "monthly_sales_trend.png")
    plt.savefig(file_path)
    print(f"Monthly sales plot saved to {file_path}")
    plt.show()

def plot_product_sales(df, output_folder="../results"):
    os.makedirs(output_folder, exist_ok=True)
    product_sales = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)
    plt.figure(figsize=(8,5))
    product_sales.plot(kind="bar", color="orange")
    plt.title("Total Sales by Product")
    plt.xlabel("Product")
    plt.ylabel("Sales")
    plt.tight_layout()
    
    file_path = os.path.join(output_folder, "product_sales_bar.png")
    plt.savefig(file_path)
    print(f"Product sales plot saved to {file_path}")
    plt.show()

def plot_region_sales(df, output_folder="../results"):
    os.makedirs(output_folder, exist_ok=True)
    region_sales = df.groupby("Region")["Sales"].sum()
    plt.figure(figsize=(6,6))
    region_sales.plot(kind="pie", autopct="%1.1f%%")
    plt.title("Regional Sales Share")
    plt.ylabel("")
    plt.tight_layout()
    
    file_path = os.path.join(output_folder, "region_sales_pie.png")
    plt.savefig(file_path)
    print(f"Regional sales plot saved to {file_path}")
    plt.show()
