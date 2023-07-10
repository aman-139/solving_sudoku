
N=9

# We will create a function to check whether given number can be positioned at the given place
def isSafe(sudoku,row,col,num):
#check if number is present in given row
    for i in range(0,9):
        if sudoku[row][i]==num:
            return False
#check if number is present in given column
    for i in range(0,9):
        if sudoku[i][col]==num:
            return False
#check if number is present in 3*3 matrix
    startRow= row-row%3
    startCol=col-col%3

    for i in range(3):
        for j in range(3):
            if sudoku[startRow+i][startCol+j]==num:
                return False

    return True
#main sudoku solving function
def solveSudoku(sudoku,row,col):
#if we reach the end of sudoku that means its solved
    if row==N-1 and col==N:
        return True
#if we reach end of a column go to next row's first column
    if col==N:
        row+=1
        col=0
#if number is valid check for the conditions
    if sudoku[row][col]>0:
        return solveSudoku(sudoku,row,col+1)
#iterate through all numbers
    for num in range(1,N+1):
        if isSafe(sudoku,row,col,num):
            sudoku[row][col]=num
            if solveSudoku(sudoku,row,col+1):
                return True
#if not found any valid position give that position zero
            sudoku[row][col]=0
    return False
#if sudoku is solvable return result else return no
def solver(sudoku):
    if solveSudoku(sudoku,0,0):
        return sudoku
    else:
        return "no"



