# Sudoku CSP - AC-3 and Backtracking Solver

Solves 9x9 Sudoku by treating it as a constraint satisfaction problem. AC-3 prunes each cell's options first, and backtracking finishes any cells AC-3 cannot settle on its own.

## At a Glance

- **Stack:** Python (standard library only)
- **Context:** CP 468 Artificial Intelligence, Wilfrid Laurier University (Assignment 2, Group 8)
- **State:** Complete

## Features

- Models every cell as a variable with a domain of 1 to 9
- AC-3 enforces arc consistency across rows, columns and 3x3 boxes
- Falls back to backtracking search when AC-3 leaves cells open
- Prints the board before AC-3, after AC-3, and once solved

## Project Structure

```
sudoku-csp/
├── sudoku.py                 # AC-3, backtracking and the solve loop
└── sudoku-csp-overview.pdf   # Write-up of the approach and results
```

## Running Locally

1. Clone the repo and move into the solver folder:
   ```bash
   git clone https://github.com/nakulpatel0306/sudoku-csp-algorithm.git
   cd sudoku-csp-algorithm/sudoku-csp
   ```
2. Add a `sudoku.txt` next to `sudoku.py`. Use nine lines of nine space-separated digits, with `0` for blank cells:
   ```
   5 3 0 0 7 0 0 0 0
   6 0 0 1 9 5 0 0 0
   ...
   ```
3. Run it:
   ```bash
   python sudoku.py
   ```

## Team

Romin Gandhi, Jenish Bharucha, Nakul Patel, Arsh Patel, Dhairya Patel, Paarth Bagga, Devarth Trivedi, Gleb Silin, Emmet Currie, Parker Riches

Built as coursework for CP 468 at Wilfrid Laurier University. Please do not copy for academic submissions.
