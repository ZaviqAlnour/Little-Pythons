from collections import Counter

number = input("Numbers: ")
numbers = []

for num in number:
    numbers.append(int(num))

counts = Counter(numbers)

for number, count in counts.items():
    print(f"Number {number}: {count} times.")