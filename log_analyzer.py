import csv
from collections import Counter

def main():
    log_level_distribution()

csv_file = 'logFile.csv'
iteams = []

def log_level_distribution():
    items = []

    with open(csv_file, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            items.append(row["level"])

    logs_count = Counter(items)
    total_items = sum(logs_count.values())

    print(f"\nTotal items counted: {total_items}\n")
    print("Level : Count (Percentage)")
    print("-" * 30)

    for level, count in logs_count.items():
        percentage = (count / total_items) * 100
        print(f"{level}\t{count}\t{percentage:.2f}%")


main()