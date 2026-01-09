🐍 Little Pythons
A curated collection of beginner-friendly Python scripts that teach core programming concepts through practical, hands-on examples. Perfect for Python newcomers and intermediate learners building foundational skills.

✨ Featured Projects
#	Project	Core Concepts	Difficulty
1	Number Frequency Counter	Collections, Data Analysis	🟢 Beginner
2	Rock Paper Scissors	Game Logic, Pattern Matching	🟡 Intermediate
3	CLI To-Do Manager	File I/O, CRUD Operations	🟡 Intermediate
4	Unique Elements	Data Structures, Validation	🟢 Beginner
5	Log File Analyzer	Data Processing, Reporting	🟠 Advanced
🚀 Quick Start
Clone the repo:

bash
git clone https://github.com/ZaviqAlnour/Little-Pythons.git
cd Little-Pythons
Run any script:

bash
python number_frequency.py
# or
python rock-paper-scissors.py
No setup required - uses only Python standard library!

📋 Project Details
1. Number Frequency Counter
number_frequency.py

What it does: Counts digit frequency in a number string using collections.Counter.

Key Learning:

String → List conversion

Frequency analysis

F-string formatting

Demo:

text
Input: "112233"
Output:
Number 1: 2 times
Number 2: 2 times  
Number 3: 2 times
Time Complexity: O(n)

2. Rock Paper Scissors
rock-paper-scissors.py

What it does: Multi-round game with weighted scoring (Rock=2pts, Paper=1pt, Scissors=3pts).

Key Learning:

match-case statements (Python 3.10+)

Input validation loops

Random module

Game state management

Features:

Customizable rounds

'q' to quit anytime

Detailed score tracking

Demo:

text
Ahmed vs Computer - Best of 3
Round 1: rock vs paper → You lose!
Final: Ahmed 6pts | Computer 4pts → YOU WIN! 🎉
3. CLI To-Do List Manager
to_do_with_txt_file.py

What it does: Full CRUD app with persistent CSV storage.

Key Learning:

csv.DictReader/Writer

File existence checking

Menu-driven interfaces

Data validation

Features:

Add/Edit/View/Delete tasks

Auto-creates tasks.csv

Search by task number

CSV Format:

text
task_number,task_name,task_details,task_due
1,Project,Backend,2024-01-15
4. Unique Elements Collector
unique-elements.py

What it does: Builds list of unique numbers with duplicate prevention.

Key Learning:

List membership testing (in operator)

try/except for input validation

Loop control patterns

Demo:

text
Enter number: 5 → Added!
Enter number: 5 → Duplicate skipped!
Enter number: abc → Please enter a number!
Final: [5, 10, 7]
5. Log File Analysis
log_analysis.py

What it does: Analyzes logFile.csv → generates JSON reports + console stats.

Key Learning:

CSV parsing + aggregation

collections.Counter

JSON export

Percentage calculations

Output: Console tables + output.json

🛠️ Prerequisites
Python 3.7+ (3.10+ recommended for match-case)

No external packages needed

🎯 Learning Path
text
Beginner → Intermediate → Advanced
  ↓             ↓             ↓
Freq Counter  RPS Game    Log Analyzer
Unique List   To-Do App
Perfect for:

CS50 Python students

Bootcamp learners

Self-taught programmers

Interview prep

📄 License
text
MIT License - Free for learning & personal use
Created for educational purposes by ZaviqAlnour

Last Updated: January 2026