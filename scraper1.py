from bs4 import BeautifulSoup
import requests
import tkinter as tk
from tkinter import *
from tkinter import messagebox


website = 'http://nine.websudoku.com/?'

response = requests.get(website)
page_html = BeautifulSoup(response.text, 'html.parser')

table_container = page_html.find("table", {"id": "puzzle_grid"})
list = table_container.find_all("input")


matrix = []

for i in range(9):          
    a =[]
    for j in range(9):      
        a.append(0)
    matrix.append(a)

for k in range(9):
    for r in range(9):
        if list[9*k+r].get('value') != None:
            matrix[k][r] = list[9*k+r].get('value')

def callback(var):
    temp = var.__str__().replace('PY_VAR', '')
    temp = int(temp)
    matrix[temp//9][temp%9] = var.get()
    

def regular1(P):
     num = len(P) < 2 and (P.isdigit() or P == "")
     return num

def make_grid():
    regular = root.register(regular1)
    for row in range(9):
        for column in range(9): 
            if matrix[row][column] == 0: 
               var = tk.StringVar()
               var.trace("w", lambda name, index, mode, var=var: callback(var))
               entryb = Entry(root, bd = 2, textvariable = var, cursor = "plus", font = ('Centry 10'), justify = "center", width = 5,
                             validate="key", validatecommand=(regular, "%P"))
               entryb.grid(row = row, column = column, padx = 1, pady = 1, ipady = 10)
            else:
                vaar = StringVar()
                vaar.set(matrix[row][column])
                label = Label(root, bd = 1, cursor = "plus", font = ('Centry 10'), justify = "center", width = 5, textvariable = vaar)
                label.grid(row = row, column = column, padx = 1, pady = 1, ipady = 10)
def sudoku_GUI():
    global root
    root = tk.Tk()
    root.title("S U D O K U   G A M E")
    root.configure(bg="black")
    make_grid()
    root.mainloop()
         
sudoku_GUI()
for i in range(9): 
    for j in range(9): 
       print(matrix[i][j], end = " ") 
    print() 
