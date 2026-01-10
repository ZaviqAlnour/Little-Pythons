🐍 Little Python

This repository contains small Python projects added one by one to track a step-by-step learning journey. All code stays in one place so progress, habits, and improvement are easy to see over time.
​

About this repo
A single repo that stores all Python practice projects with a focus on core concepts.
​

Projects are created for self-learning, problem solving, and building consistency in coding.
​

No specific framework is used at this stage; the first goal is to become strong in core Python only.
​

How projects are added
Each new project is added as a file or folder inside this repository.
​

A short description for that project stays in its own README.md (inside the project folder) or as comments in the code.
​

The main README.md only gets an updated serial list of projects so the structure almost never needs to change.
​

Project list
Starting with a simple serial list that grows as new projects are added:

Project 1:

Unique Number Collector
This is a small Python console project that lets the user build a list of unique numbers interactively. The program keeps asking for input until the user decides to stop and makes sure no duplicate numbers are added to the list.
​

What this project does
Continuously asks the user to enter a number using a while True loop.
​

Stores all numbers in a list only if they are not already in the list (enforcing uniqueness).
​

Asks after each input whether the user wants to add more numbers or exit.
​

Input validation
User input is converted to int, and invalid inputs are handled with a try/except block.
​

If the user types something that is not a valid integer, the program shows an error message instead of crashing.
​

After an invalid input, the user can choose whether to try again or stop the program.
​

Final output
When the user chooses not to continue, the loop stops using break.
​

The program prints the final list of all unique numbers that were successfully added.
​

Project 2:

Here’s a clean, detailed description you can use as that project’s own README:

Number Frequency Counter
This project is a small Python script that counts how many times each digit appears in a sequence of numbers entered by the user. It is a simple way to practice working with lists, loops, user input, and the Counter class from the collections module.
​

What this script does
Asks the user to input a sequence of digits in one line (for example: 11234511).
​

Converts each character from the input string into an integer and stores all digits in a list.
​

Uses Counter to calculate how many times each digit appears, then prints the frequency of every unique digit.
​

Key Python concepts practiced
User input using the input() function.

Iterating over a string and building a list of integers.

Using collections.Counter to count occurrences of elements in a list.
​

Looping over a dictionary-like object (counts.items()) and using f-strings for formatted output.
​

How the code works (step by step)
Import Counter from the collections module to handle frequency counting in a clean and efficient way.
​

Take a string input from the user and store it in number.

Create an empty list numbers and loop through each character in the input string, converting each one to int and appending it to the list.

Pass the numbers list to Counter to get a mapping of digit -> count.
​

Loop through counts.items() and print each digit and how many times it appears in a readable sentence.

Example usage
Input: Numbers: 11234511

Output format:

Number 1: 4 times.

Number 2: 1 times.

Number 3: 1 times.

Number 4: 1 times.

Number 5: 1 times.

This project is useful as an early exercise in your Little Python repo to understand frequency counting, basic data structures, and simple data analysis on user input.
​

Project 3:

CLI To-Do List Manager
This project is a command-line To-Do List Manager written in Python that stores tasks in a CSV file so they persist between runs. It is a practical exercise in file handling, basic data modeling, user input, and building a menu-driven CLI application.
​

What this app does
Lets you add new tasks with a task number, name, short details, and due date or time.
​

Allows viewing a single task by its task number or listing all saved tasks from the CSV file.
​

Supports editing an existing task and clearing the entire task list when all tasks are done.
​

Core features
Menu-based CLI interface

Prints a feature menu and takes a numeric choice from the user.

Uses a match statement to route the choice to the correct function.

Persistent storage with CSV

Stores tasks in tasks.csv using csv.DictWriter and csv.DictReader.
​

ensure_file_exists() creates the file with a header row if it does not already exist.

Task management operations

add_task(): Adds a new task with task_number, task_name, task_details, and task_due.

view_task_by_number(): Looks up and prints a single task by its number.

view_all_tasks(): Prints every task in the CSV file in a clean, formatted way.

edit_task(): Loads all tasks, allows updating name/details/due for a specific task, and then writes them back.

clear_tasks_list(): Clears the entire task list after a confirmation prompt.

Basic error handling

Handles invalid menu input using try/except for ValueError when converting to int.

Validates file existence and prints messages when tasks are not found or when no tasks exist.
​

Key Python concepts practiced
Standard library modules: csv, sys, and os for file operations and exiting the program.
​

File handling: Opening files in read, write, and append modes with proper encoding and newline="".
​

CSV with dictionaries: Using DictWriter and DictReader to work with rows as dictionaries instead of raw lists.
​

Control flow: Menu handling with match/case, conditionals, and loops.

User input and validation: Reading from input(), converting types, and confirming destructive actions like clearing all tasks.
​

How it works (high level flow)
The program starts in main(), prints a welcome message, and shows the available features.

The user enters a menu choice; the code checks that it is a valid integer and routes the choice using match.

Before any operation on tasks, ensure_file_exists() makes sure tasks.csv exists and has the correct header.

Depending on the chosen option, the program reads or writes task data in the CSV file and prints clear feedback messages to the user.
​

Example usage
Start the script:

The menu appears with options 1–5.

Choose 1 to add a task, then enter name, number, details, and due date.

Choose 3 to view all tasks and see them printed one by one from the CSV file.

Choose 4 to edit an existing task by its task number.

Choose 5 to clear all tasks after confirming with y or yes.

This project is a solid step in your Little Python journey for practicing real-world CLI apps, persistence with CSV files, and structured code organization.
​

Project 4:

Here’s a detailed README description for this Rock, Paper, Scissors project:

Rock, Paper, Scissors – CLI Game
This project is a command-line Rock, Paper, Scissors game written in Python where the user plays against the computer over a chosen number of rounds. It adds a custom scoring system and uses structural pattern matching (match/case) to handle all game outcomes in a clean, readable way.
​

What this game does
Greets the player by name and asks how many rounds they want to play.

Lets the user choose between rock, paper, or scissors each round, with the option to type q to quit at any time.
​

Randomly selects the computer’s move and calculates points based on who wins or if it is a draw.

Shows the final total scores for both player and computer, then prints who won the game overall.
​

Custom scoring rules
The game uses a non-standard scoring system to make each choice feel a bit different:

Rock win → +2 points

Paper win → +1 point

Scissors win → +3 points

In case of a draw, both the player and the computer get the points for the move they chose (for example, rock vs rock gives both +2 points).
​

Core features and logic
Input and validation

Asks for player name and number of rounds at the start.

In each round, repeatedly asks for the user’s choice until a valid option (rock, paper, scissors, or q) is entered.

If the user types q, the game exits early with a message.

Computer move generation

Uses random.randint(1, 3) to generate the computer’s move, mapping 1 → rock, 2 → paper, 3 → scissors.
​

Outcome handling with match

Uses a match (computer_choice, user_choice) statement to cover all combinations of user vs computer.

Each case updates user_point and/or computer_point and prints a message like “You won this round!” or “Draw!”.
​

Final result

After all rounds, prints total user points and computer points.

Compares the scores to decide if the user won, lost, or drew the game, and prints a final message.
​

Key Python concepts practiced
Randomness: Using the random module to simulate computer choices.
​

Loops:

for loop to control the number of rounds.

while True loop for validating user input each round.

Conditional logic: Structural pattern matching (match/case) to handle many outcome combinations clearly.
​

User interaction: Reading input, validating it, and giving immediate feedback through printed messages.
​

Example flow
User enters their name and number of rounds (e.g., 5).

For each round, the user enters rock, paper, or scissors.

The computer randomly chooses a move, and the program prints whether it was a win, loss, or draw and how many points were gained.

After the last round, the game prints final scores and a message like “Congratulations, you won the game!” or “The game ended in a draw.”
​

This project is a fun addition to your Little Python repo for practicing control flow, randomness, input validation, and working with a slightly more advanced match/case structure in Python.

Project 5:

Here’s a detailed README description for this log analyzer project:

Core Python Log Analyzer
This project is a command-line log analyzer written in Python that reads log data from a CSV file, summarizes it, prints human-readable distributions, and exports a structured JSON report. It is designed to practice CSV parsing, data cleaning, frequency analysis with Counter, and simple report generation.
​

What this tool does
Loads log entries from a CSV file named logFile.csv, cleaning up extra spaces in headers and values.
​

Calculates how often each log level appears and how frequently different sources, events, and messages occur for warning and error logs.
​

Prints formatted distribution tables to the terminal and writes a summary report to output.json.
​

Core features
CSV log loading and cleanup

load_logs(csv_file) checks if the CSV file exists; if not, it prints a red error message and exits.

Uses csv.DictReader and strips whitespace from fieldnames and row values so inconsistent spacing in the log file does not break the analysis.
​

Log level distribution

log_level_distribution(logs) extracts the "level" field from each log row (defaulting to "UNKNOWN" if missing).

Uses collections.Counter to count how many times each level appears and prints a table showing counts and percentages.
​

Returns a summary dictionary with total logs and per-level counts.

Error and warning analysis

error_distribution(logs, field) focuses only on logs where level is "WARN" or "ERROR".

Counts how often each value of a chosen field (source, event, or message) appears in those problematic logs.
​

Prints a colored “Issues Detected (WARN + ERROR)” header and a distribution table, then returns the results as a dictionary.

Formatted console output

print_distribution() prints a title, total items, and a neatly aligned table with columns for label, count, and percentage.

Handles the case where there is no data and prints “No data available.” instead of failing.

JSON report generation

In main(), after analysis, a report dictionary is created with keys: "logs_levels", "sources", "events", and "messages".

The script writes this dictionary to output.json using json.dump() with indentation for readability.
​

Key Python concepts practiced
Standard library usage:

csv for reading structured log data.

json for exporting summarized metrics.

os for file existence checks and sys.exit() for graceful termination on errors.
​

Collections:

collections.Counter to compute frequency distributions without writing manual counting loops.
​

Data cleaning: Stripping whitespace from CSV headers and values to avoid subtle bugs caused by inconsistent formatting.
​

Console UX: Using formatted strings and ANSI color codes to make CLI output easier to read and debug.
​

High-level flow
The script starts in main() and calls load_logs(csv_file) to read and clean all log entries.

If no logs are loaded, the script exits; otherwise, it prints a header: “Core python Log Analyzer”.

It generates:

Overall log level distribution (log_level_distribution).

WARN + ERROR distributions for source, event, and message (error_distribution).

All results are stored in report and written to output.json, followed by a success message confirming the file creation.
​

This project is a strong step in your Little Python journey for working with real-world-style log data, doing simple analytics, and producing both terminal and JSON outputs from the same analysis pipeline.
​

Only the project name or a short title needs to be added here; extra details stay in the separate project folder/README.
​

Goal & usage
This repo exists to show personal Python growth, compare progress in the future, and serve as a clean part of a portfolio.
​

Anyone can clone the repo, run the code, read it, and modify it for their own practice.
​

It is not a production-ready project, but a learning-focused collection of scripts and mini projects.
​