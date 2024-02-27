import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_csv(file_path):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Display basic information about the DataFrame
    print("Basic Information:")
    df.info()

    # Display the first 5 rows of the DataFrame
    print("\nFirst 5 Rows:")
    print(df.head())

    # Enhanced summary statistics
    print("\nEnhanced Summary Statistics:")
    print(df.agg({
        "quantity": ["sum", "mean", "std", "min", "max"],
        "price": ["sum", "mean", "std", "min", "max"]
    }))

    # Check for and display any missing values
    missing_values = df.isnull().sum()
    print("\nMissing Values:")
    print(missing_values[missing_values > 0])

    # Calculate total sales (price * quantity) and add it as a new column
    df["total_sales"] = df["price"] * df["quantity"]

    # Group sales by date and sum the total sales
    sales_by_date = df.groupby("date")["total_sales"].sum().reset_index()

    # Plotting sales grouped by date
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=sales_by_date, x="date", y="total_sales")
    plt.xticks(rotation=45)
    plt.title("Sales Grouped by Date")
    plt.xlabel("Date")
    plt.ylabel("Total Sales")
    plt.tight_layout()
    plt.show()

    # Displaying a histogram of total sales to understand distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(df["total_sales"], bins=20, kde=True)
    plt.title("Distribution of Total Sales")
    plt.xlabel("Total Sales")
    plt.ylabel("Frequency")
    plt.show()

if __name__ == "__main__":
    file_path = "sales_data.csv"
    analyze_csv(file_path)
