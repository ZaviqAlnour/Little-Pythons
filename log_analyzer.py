import csv; import json
import sys; import os
from collections import Counter

csv_file = 'logFile.csv'

def load_logs(csv_file):
    if not os.path.exists(csv_file):
        print(f"\033[31mError: File not found: {csv_file}\033[0m")
        sys.exit()
    logs = []

    with open(csv_file, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        reader.fieldnames = [name.strip() for name in reader.fieldnames]

        for row in reader:
            cleaned_rows = {k.strip(): v.strip() for k, v in row.items()}
            logs.append(cleaned_rows)

    return logs        

def print_distribution(title, counts, label):
    total = sum(counts.values())
    print(f"\n{title}")
    print(f"Total items counted: {total}\n")

    if total == 0:
        print("No data available.")
        return
    
    header_fmt = "{:<25} {:>8} {:>10}"
    print(header_fmt.format(label, "Count", "Percentage"))
    print("-" * 45)

    row_fmt = "{:<25} {:>8} {:>9.2f}%"
    for item, count in counts.items():
        percentage = (count / total) * 100
        print(row_fmt.format(item[:24], count, percentage))



def log_level_distribution(logs):
    levels = [row.get("level", "UNKNOWN") for row in logs]
    counts = Counter(levels)

    print_distribution(
        title="ALL Log Levels",
        counts=counts,
        label="Level"
    )

    return {"total": sum(counts.values()), "data": dict(counts)}


def error_distribution(logs, field):
    items = [
        row.get(field, "UNKNOWN")
        for row in logs
        if row.get("level") in ("WARN", "ERROR")
    ]

    counts = Counter(items)

    print("\033[31mIssues Detected (WARN + ERROR):\033[0m")
    print_distribution(
        title=f"{field.capitalize()} Distribution",
        counts=counts,
        label=field.capitalize()
    )

    return {"total": sum(counts.values()), "data": dict(counts)}

def main():
    logs = load_logs(csv_file)

    if not logs:
         sys.exit()
    
    print("Core python Log Analyzer")
    print("-" * 30)
    report = {}
    report["logs_levels"] = log_level_distribution(logs)
    report["sources"] = error_distribution(logs, "source")
    report["events"] = error_distribution(logs, "event")
    report["messages"] = error_distribution(logs, "message")

    with open("output.json", "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)

    print("\noutput.json file created successfully")    

if __name__ == "__main__":
    main()