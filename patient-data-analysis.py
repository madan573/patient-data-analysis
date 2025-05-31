import pandas as pd
from statistics import mode, StatisticsError

# Read CSV file
def read_patient_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print("CSV file not found!")
        return None
    except Exception as e:
        print("Error reading file:", e)
        return None

# Analyze numeric columns
def analyze_numeric_data(df):
    print("\n--- Patient Data Statistical Summary ---")
    numeric_cols = df.select_dtypes(include=['number'])

    for col in numeric_cols.columns:
        print(f"\nColumn: {col}")
        print(f"Mean   : {numeric_cols[col].mean():.2f}")
        print(f"Median : {numeric_cols[col].median():.2f}")
        try:
            print(f"Mode   : {mode(numeric_cols[col])}")
        except StatisticsError:
            print("Mode   : No unique mode")

# Main function
def main():
    file_path = "data/hospital.csv"
    df = read_patient_data(file_path)

    if df is not None:
        print("\nFirst 5 rows of the data:\n", df.head())
        analyze_numeric_data(df)

if __name__ == "__main__":
    main()
