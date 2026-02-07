def parse_log_file(path):
    entries = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(" ", 3)
            if len(parts) < 4:
                continue
            level, date, time, message = parts
            entries.append({
                "level": level,
                "datetime": f"{date} {time}",
                "message": message
            })
    return entries
