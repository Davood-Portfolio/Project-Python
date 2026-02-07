def save_report(summary, summary_path, error_path):
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write("Log Summary Report\n")
        f.write("=================\n")
        f.write(f"Total entries: {summary['total']}\n")
        f.write(f"INFO: {summary['INFO']}\n")
        f.write(f"WARNING: {summary['WARNING']}\n")
        f.write(f"ERROR: {summary['ERROR']}\n")

    with open(error_path, "w", encoding="utf-8") as f:
        for err in summary["errors"]:
            f.write(f"{err['datetime']} - {err['message']}\n")
