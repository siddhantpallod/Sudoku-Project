import math, random

class SudokuGenerator:
    '''
	create a sudoku board - initialize class variables and set up the 2D board
	This should initialize:
	self.row_length		- the length of each row
	self.removed_cells	- the total number of cells to be removed
	self.board			- a 2D list of ints to represent the board
	self.box_length		- the square root of row_length

	Parameters:
    row_length is the number of rows/columns of the board (always 9 for this project)
    removed_cells is an integer value - the number of cells to be removed

	Return:
	None
    '''

    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        #self.board = [[0 for i in range(self.row_length)] for j in range(9)]
        self.board = []
        for j in range(9):
            row = []
            for i in range(self.row_length):
                row.append(0)
            self.board.append(row)

        self.box_length = int((row_length)**(1/2))

    def get_board(self):
        result = []
        for j in range(9):
            row = []
            for i in range(self.row_length):
                row.append(self.board[j][i])
            result.append(row)
        return result
        #return [[self.board[j][i] for i in range(self.row_length)] for j in range(9)]

    def print_board(self):
        for row in self.board:
            print(row)

    def valid_in_row(self, row, num):
        for cell in self.board[row]:  # Iterate through row
            if cell == num:
                return False
        return True

    def valid_in_col(self, col, num):
        for row in self.board:
            if row[col] == num:
                return False
        return True

    def valid_in_box(self, row_start, col_start, num):
        for row in range(row_start, row_start + 3):
            for col in range(col_start, col_start + 3):
                if self.board[row][col] == num:
                    return False
        return True

    def is_valid(self, row, col, num):
        if self.board[row][col] != 0:
            return False
        if self.valid_in_row(row, num) and self.valid_in_col(col, num) and self.valid_in_box(row - row % 3, col - col % 3, num):
            return True
        return False

    def fill_box(self, row_start, col_start):
        nums = list(range(1, 10))  # Numbers 1 to 9
        random.shuffle(nums)
        for i in range(3):
            for j in range(3):
                self.board[row_start + i][col_start + j] = nums.pop()


    def fill_diagonal(self):
        for i in range(0, self.row_length, 3):
            self.fill_box(i, i)

    '''
    DO NOT CHANGE
    Provided for students
    Fills the remaining cells of the board
    Should be called after the diagonal boxes have been filled

	Parameters:
	row, col specify the coordinates of the first empty (0) cell

	Return:
	boolean (whether or not we could solve the board)
    '''

    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    '''
    DO NOT CHANGE
    Provided for students
    Constructs a solution by calling fill_diagonal and fill_remaining

	Parameters: None
	Return: None
    '''

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    def remove_cells(self):
        count = self.removed_cells
        while count > 0:
            row = random.randint(0, self.row_length - 1)
            col = random.randint(0, self.row_length - 1)

            if self.board[row][col] != 0:
                self.board[row][col] = 0
                count -= 1


'''
DO NOT CHANGE
Provided for students
Given a number of rows and number of cells to remove, this function:
1. creates a SudokuGenerator
2. fills its values and saves this as the solved state
3. removes the appropriate number of cells
4. returns the representative 2D Python Lists of the board and solution

Parameters:
size is the number of rows/columns of the board (9 for this project)
removed is the number of cells to clear (set to 0)

Return: list[list] (a 2D Python list to represent the board)
'''


def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board
