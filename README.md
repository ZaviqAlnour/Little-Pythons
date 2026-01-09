🐍 Little Pythons

A collection of beginner-friendly Python scripts demonstrating fundamental programming concepts including data manipulation, game development, task management, and data structures.

Table of Contents

Number Frequency Counter

Rock Paper Scissors Game

CLI To-Do List Manager

Unique Elements Collector

Log File Analysis

1. Number Frequency Counter

File: number_frequency.py

Description

A simple program that counts the frequency of individual digits in a user-provided string of numbers using Python's Counter class from the collections module.

Scope

Purpose: Demonstrates basic input handling and frequency counting using built-in data structures

Key Concepts:

User input manipulation

Type conversion (string to integer)

collections.Counter for frequency analysis

Basic looping and list operations

String formatting with f-strings

Features

Takes a string of numbers as input

Converts string digits to integers

Counts occurrence of each number

Displays frequency of each number with formatted output

Example Usage

Input: "112233"
Output:

Number 1: 2 times.
Number 2: 2 times.
Number 3: 2 times.

Technical Details

Import: collections.Counter

Data Structure: List of integers

Time Complexity: O(n) where n is the length of input

Best For: Learning basic counting and data structure usage

2. Rock Paper Scissors Game

File: rock-paper-scissors.py

Description

An interactive game where users play multiple rounds of Rock, Paper, and Scissors against the computer. Features a unique point system, input validation, and the ability to quit mid-game.

Scope

Purpose: Demonstrates game logic, conditional statements, and user interaction

Key Concepts:

Random number generation

Pattern matching with match-case statements (Python 3.10+)

Input validation and error handling

Loop control and game state management

Score tracking and comparison logic

User-friendly output formatting

Features

Personalized greeting with player name

Multiple rounds with configurable count

Unique point system:

Rock win → +2 points

Paper win → +1 point

Scissors win → +3 points

Input validation prevents invalid entries from skipping rounds

'q' command to quit anytime

Detailed round-by-round feedback

Final score display and winner announcement

Example Usage
Enter your name: Ahmed
How many rounds do you want to play?: 3

Round 1
Enter rock, paper, or scissors: rock
You won this round! +2 points.

... [more rounds] ...

---------- GAME OVER ----------
Your total points: 6
Computer total points: 4
Congratulations Ahmed, you won the game!

Technical Details

Import: random

Validation: Loop-based input validation ensures only valid choices are accepted

Pattern Matching: Uses Python 3.10+ match-case for clean game logic

Scope: Intermediate - suitable for learning game mechanics

Unique Feature: Weighted point system makes scissors valuable strategy

3. CLI To-Do List Manager

File: to_do_with_txt_file.py

Description

A command-line To-Do list application with full CRUD operations. Tasks are stored in a CSV file, allowing persistent data storage. Features include adding, viewing, editing, and clearing tasks.

Scope

Purpose: Demonstrates file I/O, CSV handling, data persistence, and application design patterns

Key Concepts:

CSV file reading and writing

File management and existence checking

Dictionary-based data structures

CRUD (Create, Read, Update, Delete) operations

Error handling and user confirmations

Menu-driven interface design

String matching and conditional logic

Features

Add Task: Create new tasks with name, number, details, and due date

View Single Task: Search and display task by number

View All Tasks: List all tasks in the database

Edit Task: Modify existing task information (selective field updates)

Clear All: Delete all tasks with confirmation

File Persistence: Uses tasks.csv for data storage

Error Handling: Graceful handling of file errors and invalid inputs

Automatic File Creation: Creates CSV file with headers if not exists

Example Usage
Welcome to the CLI To-Do List Manager Software.

What do you want to do?
1. Add a task
2. View a task by number
3. View all tasks
4. Edit a task
5. Clear all tasks

Enter your choice: 1

Task Name: Complete Project
Task Number: 1
Details: Python project
Due Date / Time: 2024-01-15
Task "Complete Project" has been added successfully.

CSV Structure
task_number,task_name,task_details,task_due
1,Project,Backend,2024-01-15
2,Report,Analysis,2024-01-20

Technical Details

Imports: csv, sys, os

File Format: CSV with DictWriter / DictReader

Data Validation: Basic string inputs with length guidance

Scope: Intermediate - demonstrates file handling and data management

Best For: Learning CRUD operations and CSV file manipulation

4. Unique Elements Collector

File: unique-elements.py

Description

An interactive program that collects unique numbers from user input, preventing duplicate entries and maintaining a list of unique values.

Scope

Purpose: Demonstrates input validation, list operations, and error handling

Key Concepts:

List membership checking

Exception handling (ValueError)

User interaction and confirmations

Data validation and duplicate prevention

Loop control with break statements

Type conversion with error handling

User-friendly error messages

Features

Takes numeric input from user

Prevents duplicate entries with notification

Adds valid unique numbers to list

Error handling for non-numeric input

Option to continue or exit after each entry

Option to retry after errors

Displays final list of unique numbers

Example Usage
Enter a unique number: 5
Added 5 to the list.
Do you want to add more? (y/n): y

Enter a unique number: 5
This number already exists!
Do you want to add more? (y/n): y

Enter a unique number: 10
Added 10 to the list.
Do you want to add more? (y/n): n

Final list of unique numbers: [5, 10]

5. Log File Analysis and Reporting Tool

File: log_analysis.py

Description

A Python-based log analysis program that processes a CSV log file and generates statistical distributions for log levels, sources, events, and messages. The results are displayed in the console and exported to a structured JSON report.

Scope

Purpose: Analyze structured log data to identify trends, errors, and warnings, and produce a machine-readable summary report

Key Concepts:

CSV file parsing with csv.DictReader

Data aggregation using collections.Counter

Conditional filtering of log records

Percentage-based statistical analysis

JSON report generation

Console-based formatted reporting

Features

Reads log entries from a CSV file (logFile.csv)

Calculates distribution of:

Log levels (INFO, WARN, ERROR, etc.)

Sources generating WARN and ERROR logs

Events associated with WARN and ERROR logs

Messages associated with WARN and ERROR logs

Displays counts and percentages in a readable tabular format

Highlights issues (WARN + ERROR) in console output

Exports all computed statistics to output.json

Example Usage

Input: logFile.csv containing structured log data
Output:

Console summary of log distributions with counts and percentages

output.json file containing aggregated results

Technical Details

Imports: csv, json, collections.Counter

Input Format: CSV file with fields such as level, source, event, and message

Output Format: JSON with totals and frequency data

Time Complexity: O(n) where n is the number of log entries

Best For: Log monitoring, error analysis, and basic reporting automation

Prerequisites

Python 3.7+ (3.10+ recommended for rock-paper-scissors.py)

No external dependencies required (uses only Python standard library)

Setup
git clone https://github.com/ZaviqAlnour/Little-Pythons.git
cd Little-Pythons

License

This repository is created for Python learning purposes.
You can use, modify, and study the code freely to improve your skills.
Not intended for commercial use.

Last Updated: January 2025
Author: ZaviqAlnour