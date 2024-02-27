import pandas as pd

def analyze_csv(file_path):
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
