import pandas as pd


def analyze_csv(file_path):
    file_path = "sales_data.csv"

    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Display basic information about the DataFrame
    print("Basic Information:")
    df.info()

    # Display the first 5 rows of the DataFrame
    print("\nFirst 5 Rows:")
    print(df.head())

    # Display summary statistics
    print("\nSummary Statistics:")
    print(df.describe())

    # Check for and display any missing values
    missing_values = df.isnull().sum()
    print("\nMissing Values:")
    print(missing_values[missing_values > 0])

    # Calculate total sales (price * quantity) and add it as a new column
    df["total_sales"] = df["price"] * df["quantity"]

    # Group sales by date and sum the total sales
    sales_by_date = df.groupby("date")["total_sales"].sum().reset_index()

    # Display sales grouped by date
    print("\nSales Grouped by Date:")
    print(sales_by_date)
