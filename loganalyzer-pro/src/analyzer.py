def analyze_entries(entries):
    summary = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0,
        "total": len(entries),
        "errors": []
    }

    for entry in entries:
        level = entry["level"]
        if level in summary:
            summary[level] += 1

        if level == "ERROR":
            summary["errors"].append(entry)

    return summary
