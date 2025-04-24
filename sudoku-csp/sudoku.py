from collections import deque

# Helper function to read Sudoku from a file
def read_puzzle(file_path):
    with open(file_path, 'r') as f:
        return [[int(num) for num in line.split()] for line in f]

# Helper function to print Sudoku grid
def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))
    print()

# Get all peers for a given cell (row, col)
def get_peers(row, col):
    peers = set()
    for i in range(9):
        peers.add((row, i))  # Same row
        peers.add((i, col))  # Same column
    # Same 3x3 box
    box_row, box_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            peers.add((i, j))
    peers.discard((row, col))  # Remove the cell itself
    return peers

# Initialize domains for all cells
def initialize_domains(board):
    domains = {}
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                domains[(row, col)] = set(range(1, 10))
            else:
                domains[(row, col)] = {board[row][col]}
    return domains

# AC-3 algorithm implementation
def ac3(board, domains):
    queue = deque([(cell, peer) for cell in domains for peer in get_peers(*cell)])

    while queue:
        cell, peer = queue.popleft()
        if revise(domains, cell, peer):
            if not domains[cell]:  # Domain is empty -> failure
                return False
            if len(domains[cell]) == 1:
                board[cell[0]][cell[1]] = next(iter(domains[cell]))  # Update board
            for neighbor in get_peers(*cell) - {peer}:
                queue.append((neighbor, cell))
    return True

# Revise function to enforce arc-consistency
def revise(domains, cell, peer):
    revised = False
    if len(domains[peer]) == 1:
        peer_value = next(iter(domains[peer]))
        if peer_value in domains[cell]:
            domains[cell].remove(peer_value)
            revised = True
    return revised

# Function to find an empty cell
def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

# Backtracking algorithm to solve Sudoku if AC-3 doesn't fully solve
def backtrack(board, domains):
    empty = find_empty(board)
    if not empty:
        return True  # No empty cells left, puzzle solved
    row, col = empty
    for value in sorted(domains[(row, col)]):
        if is_consistent(board, row, col, value):
            board[row][col] = value
            # Create a copy of domains for backtracking
            new_domains = {key: domains[key].copy() for key in domains}
            new_domains[(row, col)] = {value}

            if backtrack(board, new_domains):
                return True
            board[row][col] = 0  # Undo assignment
    return False

# Function to check if a value can be placed in a cell without conflicts
def is_consistent(board, row, col, val):
    for peer_row, peer_col in get_peers(row, col):
        if board[peer_row][peer_col] == val:
            return False
    return True

# Solve function
def solve_sudoku(file_path):
    board = read_puzzle(file_path)
    print("Original Sudoku:")
    print_board(board)

    domains = initialize_domains(board)
    if ac3(board, domains):
        print("Sudoku after AC-3:")
        print_board(board)
        if find_empty(board):
            print("AC-3 did not completely solve the puzzle. Applying backtracking...")
            if not backtrack(board, domains):
                print("No solution exists.")
        else:
            print("Solved using AC-3!")
    else:
        print("AC-3 failed to achieve arc-consistency.")
        
    print("Final Solution:")
    print_board(board)

# Example usage
solve_sudoku('sudoku.txt')
