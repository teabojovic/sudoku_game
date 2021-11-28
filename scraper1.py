from bs4 import BeautifulSoup
import requests
from tkinter import *
from tkinter import messagebox



website = 'http://nine.websudoku.com/?'

response = requests.get(website)
page_html = BeautifulSoup(response.text, 'html.parser')

table_container = page_html.find("table", {"id": "puzzle_grid"})
list = table_container.find_all("input")


matrix = []
mmatrix2 = []

for i in range(9):          
    a =[]
    for j in range(9):      
        a.append(0)
    matrix.append(a)
    mmatrix2.append(a)

for k in range(9):
    for r in range(9):
        if list[9*k+r].get('value') != None:
            matrix[k][r] = list[9*k+r].get('value')

def callback(var, entry):
    o = var.get()
    i = 0
    j = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if mmatrix2[i][j] == entry:
               matrix[i][j] = var.get()



def make_grid():
    for row in range(9):
        for column in range(9):
            if matrix[row][column] == 0: 
               var = StringVar()
               var.trace("w", lambda name, index, mode, var=var: callback(var, entry))
               entry = Entry(root, bd = 1, textvariable = var, cursor = "plus", font = ('Centry 10'), justify = "center", width = 20)
               entry.grid(row = row, column = column, padx = 1, pady = 1, ipady = 20)
               mmatrix2[row][column] = entry
            else:
                vaar = StringVar()
                vaar.set(matrix[row][column])
                label = Label(root, bd = 1, cursor = "plus", font = ('Centry 10'), justify = "center", width = 17, textvariable = vaar)
                label.grid(row = row, column = column, padx = 1, pady = 1, ipady = 20)
def sudoku_GUI():
    global root
    root = Tk()
    root.title("S U D O K U   G A M E")
    root.configure(bg="black")
    make_grid()
    root.mainloop()

sudoku_GUI()
for r in range(9): 
     for c in range(9): 
        print(matrix[r][c], end = " ") 
     print() 


        


