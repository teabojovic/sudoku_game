import tkinter as tk
from tkinter import Entry, StringVar, Label
from tkinter import messagebox
from bs4 import BeautifulSoup
import requests

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
    solution1 = page_html.find("input", {"name": "cheat"})
    solution = solution1.get("value")
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
def solution_matrixx():
    make_matrix9x9()
    for i in range(9):
        for j in range(9):
            solution_matrix[i][j] = solution[9*i+j]
    for i in range(9):
        for j in range(9):
            print(solution_matrix[i][j], end = " ")
        print()
def num_matrix():
    '''now we put numbers that we get using get_numbers() in matrix 9x9'''
    matrix9x9()
    get_numbers()
    solution_matrixx()
    for k in range(9):
        for r in range(9):
            if list[9*k+r].get('value') is not None:
                matrix[k][r] = list[9*k+r].get('value')
def callback(var):
    '''puts new value(from entry) in matrix and checks if the matrix is ​​filled'''
    temp = var.__str__().replace('PY_VAR', '')
    temp = int(temp)
    matrix[temp//9][temp%9] = var.get()
def checkbutton_callback():
    k = 0
    for i in range(9):
        for j in range(9):
            if matrix[i][j] == solution_matrix[i][j]:
                k = k + 1
    if k == 81:
        messagebox.showinfo("End","Bravoo!!!!")
    else:
        messagebox.showinfo("End","Try again")

def regular1(P):
    '''checks the number in the entry(0 < P < 10...)'''
    num = len(P) < 2 and (P.isdigit() or P == "")
    return num #returns num, after checking
def make_grid():
    '''function makes sudoku table with buttons and entries'''
    num_matrix()
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
            else:
                vaar = StringVar()
                vaar.set(matrix[row][column])
                label = Label(root, bg = "white", bd = 1, justify = "center", width = 5, textvariable = vaar) 
                #makes label and puts number(from matrix) in it
                label.grid(row = row, column = column, padx = 1, pady = 1, ipady = 10)
                label.config(cursor = "plus", font = ('Centry 10'))
    b = tk.Button(root, text ="Check", command = checkbutton_callback)
    b.grid(row = 9, padx = 1, pady = 1, ipady = 10)
def sudoku_gui():
    '''function makes root and mainloop and at the end print new matrix'''
    global root
    root = tk.Tk()
    root.title("S U D O K U   G A M E")
    root.configure(bg="black")
    make_grid()
    root.mainloop()
    for i in range(9):
        for j in range(9):
            print(matrix[i][j], end = " ")
        print()
sudoku_gui()

