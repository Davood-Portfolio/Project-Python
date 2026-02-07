from cleaner import clean_csv

def main():
    input_file = "input/sample.csv"
    cleaned_file = "output/cleaned.csv"
    error_file = "output/errors.txt"

    cleaned_count, error_count = clean_csv(input_file, cleaned_file, error_file)

    print("Cleaning completed.")
    print(f"Valid rows: {cleaned_count}")
    print(f"Errors found: {error_count}")

if __name__ == "__main__":
    main()
