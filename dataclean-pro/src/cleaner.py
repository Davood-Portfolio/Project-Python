import csv
from validator import is_valid_int, is_valid_float, is_valid_date

def clean_csv(input_file, cleaned_file, error_file):
    cleaned_rows = []
    errors = []

    with open(input_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            row_errors = []

            # Example validation rules
            if not is_valid_int(row["age"]):
                row_errors.append("Invalid age")

            if not is_valid_float(row["salary"]):
                row_errors.append("Invalid salary")

            if not is_valid_date(row["date"]):
                row_errors.append("Invalid date")

            if row_errors:
                errors.append({"row": row, "errors": row_errors})
            else:
                cleaned_rows.append(row)

    # Save cleaned data
    with open(cleaned_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=cleaned_rows[0].keys())
        writer.writeheader()
        writer.writerows(cleaned_rows)

    # Save errors
    with open(error_file, "w", encoding="utf-8") as f:
        for e in errors:
            f.write(str(e) + "\n")

    return len(cleaned_rows), len(errors)
