import tkinter as tk
from tkinter import Entry, StringVar, Label
from tkinter import messagebox
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import time

def get_numbers():
    '''Scrapes numbers from sudoku site'''
    global list
    global solution
    list = []
    website = 'http://nine.websudoku.com/?'
    response = requests.get(website)
    page_html = BeautifulSoup(response.text, 'html.parser')
    table_container = page_html.find("table", {"id": "puzzle_grid"})
    list = table_container.find_all("input")
def matrix9x9():
    '''makes matrix 9x9 with zeros'''
    global matrix
    matrix = []
    for i in range(9):
        a =[]
        for j in range(9):
            a.append(0)
        matrix.append(a) #adds to the matrix
def make_matrix9x9():
    global solution_matrix
    solution_matrix = []
    for i in range(9):
        a =[]
        for j in range(9):
            a.append(0)
        solution_matrix.append(a)
def make_entry_matrix():
    global entry_matrix
    entry_matrix = []
    for i in range(9):
        a =[]
        for j in range(9):
            a.append(0)
        entry_matrix.append(a)
def num_matrix():
    '''now we put numbers that we get using get_numbers() in matrix 9x9'''
    for k in range(9):
        for r in range(9):
            if list[9*k+r].get('value') is not None:
               matrix[k][r] = list[9*k+r].get('value')
               solution_matrix[k][r] = list[9*k+r].get('value')
def callback(var):
    '''puts new value(from entry) in matrix and checks if the matrix is ​​filled'''
    temp = var.__str__().replace('PY_VAR', '')
    temp = int(temp)
    matrix[temp//9][temp%9] = var.get()
def checkbutton_callback():
    #function called, check button
    k = 0
    for i in range(9):
        for j in range(9):
            matrix[i][j] = int(matrix[i][j])
            if matrix[i][j] == solution_matrix[i][j]:
                k = k + 1
    if k == 81:
        messagebox.showinfo("Bravoo!!!!", datetime.now() - start_time)
    else:
        messagebox.showinfo("Try again", datetime.now() - start_time)
def regular1(P):
    '''checks the number in the entry(0 < P < 10...)'''
    num = len(P) < 2 and (P.isdigit() or P == "")
    return num #returns num, after checking
def solvebutton_callback():
    #function called, solve button
    for i in range(9):
        for j in range(9):
            if entry_matrix[i][j] != 0:
                entry_matrix[i][j].delete(0, "end")
                entry_matrix[i][j].insert(0, solution_matrix[i][j])
def make_grid():
    '''function makes sudoku table with buttons and entries'''
    make_entry_matrix()
    regular = root.register(regular1)
    for row in range(9):
        for column in range(9):
            if matrix[row][column] == 0:
                var = tk.StringVar()
                var.trace("w", lambda name, index, mode, var=var: callback(var))
                entryb = Entry(root, bd = 2, textvariable = var, justify = "center", width = 5)
                entryb.grid(row = row, column = column, padx = 1, pady = 1, ipady = 10)
                entryb.config(validate="key", validatecommand=(regular, "%P"))
                entryb.config(cursor = "plus", font = ('Centry 10'))
                entry_matrix[row][column] = entryb
            else:
                vaar = StringVar()
                vaar.set(matrix[row][column])
                label = Label(root, bg = "white", bd = 1, justify = "center", width = 5, textvariable = vaar) 
                #makes label and puts number(from matrix) in it
                label.grid(row = row, column = column, padx = 1, pady = 1, ipady = 10)
                label.config(cursor = "plus", font = ('Centry 10'))
    b = tk.Button(root, text = "Check", command = checkbutton_callback)
    b.grid(row = 9, column = 0, padx = 1, pady = 1, ipady = 20, columnspan = 4, ipadx = 70)
    b1 = tk.Button(root, text = "Solve", command = solvebutton_callback)
    b1.grid(row = 9, column = 4, padx = 1, pady = 1, ipady = 20, columnspan = 5, ipadx = 95)

def ok_num(solution_matrix, row, col, num):
    
    for i in range(9):
        if solution_matrix[row][i] == num:
            return False
    for i in range(9):
        if solution_matrix[i][col] == num:
            return False

    start_row = row - row % 3
    start_col = col - col % 3

    for i in range(3):
        for j in range(3):
            if solution_matrix[start_row+i][start_col+j] == num:
                return False

    return True

def solve_sudoku(solution_matrix, row, col):
    if row == 8 and col == 9:
        return True
    
    if col == 9:
       row += 1
       col = 0
    solution_matrix[row][col] = int(solution_matrix[row][col])
    if solution_matrix[row][col] > 0:
        return solve_sudoku(solution_matrix, row, col+1)

    for num in range(1, 10):
        if ok_num(solution_matrix, row, col, num):
            solution_matrix[row][col] = num
            if solve_sudoku(solution_matrix, row, col+1):
                return True
            solution_matrix[row][col] = 0
    return False
def sudoku_gui():
    '''function makes root and print new matrix'''
    global root
    global start_time
    root = tk.Tk()
    root.title("S U D O K U   G A M E")
    root.configure(bg="black")
    make_grid()
    start_time = datetime.now()
    root.mainloop()
get_numbers()
matrix9x9()
make_matrix9x9()
num_matrix() 
solve_sudoku(solution_matrix, 0, 0)
sudoku_gui()


