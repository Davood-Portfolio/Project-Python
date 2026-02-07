from parser import parse_log_file
from analyzer import analyze_entries
from report import save_report

def main():
    log_path = "logs/sample.log"
    summary_path = "output/summary.txt"
    error_path = "output/errors.txt"

    entries = parse_log_file(log_path)
    summary = analyze_entries(entries)
    save_report(summary, summary_path, error_path)

    print("Log analysis completed.")
    print(f"Total entries: {summary['total']}")
    print(f"Errors found: {summary['ERROR']}")

if __name__ == "__main__":
    main()
