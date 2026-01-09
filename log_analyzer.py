import csv
import json
from collections import Counter

def main():
    csv_file = 'logFile.csv'
    report = {}

    report["logs_levels"] = log_level_distribution(csv_file)
    report["sources"] = source_distribution(csv_file)
    report["events"] = event_distribution(csv_file)
    report["messages"] = message_distribution(csv_file)

    with open("output.json", "w", encoding="utf-8") as file:
        output = json.dump(report, file, indent=4)

    print("\noutput.json file created successfully")
    
def log_level_distribution(csv_file):
    items = []

    with open(csv_file, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            items.append(row['level'])

    logs_count = Counter(items)
    total_items = sum(logs_count.values())

    print(f"\nTotal items counted: {total_items}\n")
    print("Level : Count (Percentage)")
    print("-" * 30)

    for level, count in logs_count.items():
        percentage = (count / total_items) * 100
        print(f"{level}\t{count}\t{percentage:.2f}%")

    return {"total": total_items,"data": logs_count}


def source_distribution(csv_file):
    items = []

    with open(csv_file, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        reader.fieldnames = [name.strip() for name in reader.fieldnames]
        for row in reader:
            if row['level'] in ['WARN', 'ERROR']:
                items.append(row['source'].strip())

    logs_count = Counter(items)
    total_items = sum(logs_count.values())

    print(f"\nTotal items counted: {total_items}\n")
    
    header_fmt = "{:<20} {:>8} {:>10}"
    print(header_fmt.format("Source", "Count", "Percentage"))
    print("-" * 40)

    print('\033[31m' + 'Issues Detected (WARN + ERROR): ' + '\033[0m');print()
    row_fmt = "{:<20} {:>8} {:>9.2f}%"
    for source, count in logs_count.items():
        percentage = (count / total_items) * 100
        print(row_fmt.format(source, count, percentage))

    return {"total": total_items,"data": logs_count}

def event_distribution(csv_file):
    items = []

    with open(csv_file, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        reader.fieldnames = [name.strip() for name in reader.fieldnames]
        for row in reader:
            if row['level'] in ['WARN', 'ERROR']:
                items.append(row['event'].strip())

    logs_count = Counter(items)
    total_items = sum(logs_count.values())

    print(f"\nTotal items counted: {total_items}\n")
    print('\033[31m' + 'Issues Detected (WARN + ERROR): ' + '\033[0m');print()
    header_fmt = "{:<20} {:>8} {:>10}"
    print(header_fmt.format("event", "Count", "Percentage"))
    print("-" * 40)

    row_fmt = "{:<20} {:>8} {:>9.2f}%"
    for source, count in logs_count.items():
        percentage = (count / total_items) * 100
        print(row_fmt.format(source, count, percentage))

    return {"total": total_items,"data": logs_count}

def message_distribution(csv_file):
    items = []

    with open(csv_file, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        reader.fieldnames = [name.strip() for name in reader.fieldnames]
        for row in reader:
            if row['level'] in ['WARN', 'ERROR']:
                items.append(row['message'].strip())

    logs_count = Counter(items)
    total_items = sum(logs_count.values())

    print(f"\nTotal items counted: {total_items}\n")
    print('\033[31m' + 'Issues Detected (WARN + ERROR): ' + '\033[0m');print()
    max_message_length = max(len(msg) for msg in logs_count.keys())
    message_col_width = max(max_message_length, len("Message")) + 2 

    header_fmt = f"{{:<{message_col_width}}} {{:>8}} {{:>10}}"
    print(header_fmt.format("Message", "Count", "Percentage"))
    print("-" * (message_col_width + 8 + 10))

    row_fmt = f"{{:<{message_col_width}}} {{:>8}} {{:>9.2f}}%"
    for message, count in logs_count.items():
        percentage = (count / total_items) * 100
        print(row_fmt.format(message, count, percentage))

    return {"total": total_items,"data": logs_count}

main()