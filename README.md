# Sudoku CSP 🧩

## 📌 Overview
Welcome to the **Sudoku CSP**, a powerful AI-based solver that utilizes **Constraint Satisfaction Problems (CSP)** and the **AC-3 Algorithm** to enforce arc-consistency on a 9x9 Sudoku grid. If the AC-3 algorithm does not fully solve the puzzle, our **backtracking algorithm** kicks in to guarantee a complete solution.

## 🎯 Features
✅ **Solves 9x9 Sudoku puzzles efficiently using AI techniques**  
✅ **Implements AC-3 Algorithm for arc consistency**  
✅ **Uses Backtracking for complete solving when needed**  
✅ **Dynamic domain reduction based on Sudoku constraints**  
✅ **Step-by-step visualization of the queue length during AC-3 execution**  
✅ **Python-based with clean, modular code**  

## ⚡ Quick Start
### 1️⃣ Clone the Repository
```bash
   git clone https://github.com/yourusername/Sudoku-CSP.git
   cd Sudoku-CSP
```

### 2️⃣ Install Dependencies
```bash
   pip install -r requirements.txt
```

### 3️⃣ Run the Program
```bash
   python sudoku_csp.py test_sudoku.txt
```

## 📊 Sample Output
```
📜 Original Sudoku:
5 3 . . 7 . . . .
6 . . 1 9 5 . . .
. 9 8 . . . . 6 .
...

🔍 Running AC-3 Algorithm...
Step 1: Queue length = 1620
Step 2: Queue length = 1619
...

✅ AC-3 successfully solved the puzzle!

🏁 Final Sudoku Solution:
5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
...
```

## 🏗️ Project Structure
```
📂 Sudoku-CSP/
│── 📜 sudoku.py             # AC-3 & Backtracking Sudoku Solver
│── 📜 README.md             # Overview
│── 📜 CP468-A2-8.pdf        # Project Documentation 

```


## 📜 License
Developed as part of **CP 468 - Artificial Intelligence** at **Wilfrid Laurier University**.
⚠️ Do Not Copy

---

## 👥 Team Members
👨‍💻 **Romin Gandhi** | 👨‍💻 **Jenish Bharucha** | 👨‍💻 **Nakul Patel** | 👨‍💻 **Arsh Patel**  
👨‍💻 **Dhairya Patel** | 👨‍💻 **Paarth Bagga** | 👨‍💻 **Devarth Trivedi** | 👨‍💻 **Gleb Silin**  
👨‍💻 **Emmet Currie** | 👨‍💻 **Parker Riches**  
