numbers = [12, 13, 14, 2, 2 , 3, 10, 0, 1, 12, 13, 27, 50, 49, 39, 5,6,8, 8, 9, 9, 7, 40, 60, 50, 1, 2, 3, 4, 2, 1, 3, 5, 90, 100, 99, 99, 99, 35, 13, 12]

from collections import Counter

counts = Counter(numbers)

for number, count in counts.items():
    print(f"Number {number}: {count} times.")