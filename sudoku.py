#importing required modules and their libraries
from tkinter import*
from solver import solver
#creating a GUI window using tkinter
root=Tk()
#providing title
root.title("Sudoku Solver")
#providing size
root.geometry("324x550")
#defining a label asking the user to fill required numbers
label=Label(root,text="Fill in the numbers and click solve").grid(row=0,column=1,columnspan=10)
#defining error label
errLabel=Label(root,text="",fg="red")
errLabel.grid(row=15,column=1,columnspan=10,pady=5)
#defining solved label
solvedLabel=Label(root,text="",fg="green")
solvedLabel.grid(row=15,column=1,columnspan=10,pady=5)

cells={}
#checking if number is valid
def ValidateNumber(P):
    out=(P.isdigit() or P=="") and len(P)<2
    return out

reg=root.register(ValidateNumber)
#creating the 3*3 grid
def draw3x3Grid(row,column,bgcolor):
    for i in range(3):
        for j in range(3):
            e=Entry(root,width=5,bg=bgcolor,justify="center",validate="key",validatecommand=(reg,"%P"))
            e.grid(row=row+i+1,column=column+j+1,sticky="nsew",padx=1,pady=1,ipady=5)
            cells[(row+i+1,column+j+1)]=e
#creating a 9*9 grid
def draw9x9Grid():
    color="#D0ffff"
    for rowNo in range(1,10,3):
        for colNo in range(0,9,3):
            draw3x3Grid(rowNo,colNo,color)
            if color=="#D0ffff":
                color="#ffffd0"
            else:
                color="#D0ffff"
#creating a function for clearing values
def clearValues():
    errLabel.configure(text="")
    solvedLabel.configure(text="")
    for row in range(2,11):
        for col in range(1,10):
            cell=cells[(row,col)]
            cell.delete(0,"end")
#creating a function which retrieves the values entered and constructs a 2D list representing the Sudoku-like board.
def getValues():
    board=[]
    errLabel.configure(text="")
    solvedLabel.configure(text="")
    for row in range(2,11):
        rows=[]
        for col in range(1,10):
            val=cells[(row,col)].get()
            if val=="":
                rows.append(0)
            else:
                rows.append(int(val))

        board.append(rows)
    updateValues(board)
#creating a solve button
btn=Button(root,command=getValues,text="Solve",width=10)
btn.grid(row=20,column=1,columnspan=5,pady=20)
#creating a clear button
btn = Button(root, command=getValues, text="Clear", width=10)
btn.grid(row=20, column=5, columnspan=5, pady=20)
#updating values in grid
def updateValues(s):
    sol=solver(s)
    if sol!="no":
        for rows in range(2,11):
            for col in range(1,10):
                cells[(rows,col)].delete(0,"end")
                cells[(rows,col)].insert(0,sol[rows-2][col-1])
        solvedLabel.configure(text="Sudoku solved!")
    else:
        errLabel.configure(text="No solution exists for this sudoku")


draw9x9Grid()
root.mainloop()