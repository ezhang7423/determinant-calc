from tkinter import *
#for v2:
#make tabbing work
#fix lables for system of eqns
#add show steps button
# final windows
import sys
from decimal import *
def firstWin():

    '''creates the first window which asks the user which program they would like to use'''

    global root
    root = Tk()
    root.title('Linear Algebra Kit')

    def goDet(event):
        '''calls to Determinant function'''
        Det()

    def goSyst(event):
        '''calls to System of Eqn function'''
        Syst()
    title = Label(root, text='What would you like to calculate today?', font=('Comic Sans MS', 36))
    det = Button(root, text='Determinant', font=('Comic Sans MS', 36), bg = 'light grey')
    syst = Button(root, text='System of Equations', font=('Comic Sans MS', 36), bg = 'light grey') #creates buttons
    title.grid(row=0, sticky=N+S+E+W)
    det.grid(row=1, sticky=N+S+E+W)
    syst.grid(row=2, sticky=N+S+E+W)
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_rowconfigure(2, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1) #configures buttons to resize
    det.bind('<Button-1>', goDet)
    syst.bind('<Button-1>', goSyst)
    root.mainloop()




def Det():
    root.destroy()
    global roota #setup window
    roota = Tk()
    roota.title('Determinant')
    global matrixSize
    matrixSize = 2
    global entries
    entries = []

    def goCalulate():
        for entry in entries:
            if entry.get() == '':
                return
        '''calls to backend'''
        CalculateDet()

    def addRC():
        '''add a row and column, because a determinant must be operated on a n X n matrix'''
        global matrixSize
        global history
        for x in range(matrixSize):#create rows
            entry = Entry(width=3, relief=GROOVE)
            entry.grid(row=matrixSize+1, column=x + 1, pady=15, padx=15)
            entries.insert(int(matrixSize*(x+1)), entry)
        for x in range(matrixSize+1): #create columns
            entry = Entry(width=3, relief=GROOVE)
            entry.grid(row=x+1, column=matrixSize + 1, pady=15, padx=15)
            entries.append(entry)
        Label(roota, text='X' + str(matrixSize)).grid(column=x + 1, row=0)
        matrixSize+=1
        history.append(roota.grid_slaves())

    def subtractRC():
        '''subtract a row and column'''
        global matrixSize
        global history
        if len(history)>1: #doesn't operate if matrix is 2 X 2
            for x in history[len(history)-1]:
                tempList = []
                if x not in history[len(history)-2]:
                    tempList.append(x) #create list of most recent widgets
                    if 'label' not in str(x):
                        entries.remove(x) #remove widgets from list of widgets
                for widg in tempList:
                    widg.destroy() #destroy most recent widgets
            matrixSize-=1
            history = history[:-1]


    for x in range(2):
        for y in range(2):
            entry = Entry(width=3, relief=GROOVE)
            entry.grid(column=x+1, row=y+1, pady=15, padx=15)
            entries.append(entry)
        Label(roota, text='X'+str(x)).grid(column=x+1, row=0) #create inital matrix

    addRC = Button(roota, text='Add row and column', font=('Comic Sans MS', 14), bg='light grey', command=addRC)
    addRC.grid(row=0,  pady=5, padx=30)
    subtractRC = Button(roota, text='Subtract row and column', font=('Comic Sans MS', 12), bg='light grey',
                   command=subtractRC)
    subtractRC.grid(row=1, pady=5, padx=30)
    submit = Button(roota, text='Submit', font=('Comic Sans MS', 12), bg='light grey', command=goCalulate)
    submit.grid(row=2) #create buttons
    global history
    history = [] #to find most recent widgets, before i found the supereasy parameter to use for grid_slaves
    history.append(roota.grid_slaves())
    roota.mainloop()

def Syst():

    '''The frontend for solving a system of equations'''

    root.destroy()
    global rootb
    rootb = Tk()
    rootb.title('System of Equations')

    global rMatrixSize
    rMatrixSize = 2 #how many rows in matrix
    global cMatrixSize
    cMatrixSize = 2 #how many columns in matrix
    global entries1
    entries1 = [] #used to store widget names wwqqesince it don't matter what =goes in a comment
    ''' multiline eqeqqqqqeewrrrrrwre
    eeqqewwrrrrrrrqeewwwbasdcwdsrward   qwe '''

    '''when are you going to stop feeding edwin?
    i'm not toop sure
    but teh sooner the better'''

    combo1 = 'eq'

    plan = 'weq'

    kill = 'qq'








    def goCalulate():
        for entry in entries1:

            if entry.get() == '':
                return
        '''calls to backend'''
        CalculateSyst()

    def addR():

        '''adds a row to the matrix'''
        global rMatrixSize
        global cMatrixSize

        for x in range(cMatrixSize):  # create rows
            entry = Entry(width=3, relief=GROOVE)
            entry.grid(row=rMatrixSize + 2, column=x + 1, pady=15, padx=15)
            entries1.insert(int(rMatrixSize * (x + 1)+x), entry) #adds widget to list of widgets
        rMatrixSize += 1

    def addC():

        '''adds a column to the matrix'''
        global cMatrixSize
        global rMatrixSize
        for x in range(rMatrixSize):  # create columns
            entry = Entry(width=3, relief=GROOVE)
            entry.grid(row=x + 2, column=cMatrixSize + 1, pady=15, padx=15)
            entries1.append(entry)
        Label(rootb, text='X' + str(cMatrixSize)).grid(column=cMatrixSize + 1, row=1)
        #creates a label that tells you which column/variable you're on
        cMatrixSize += 1

    def subtractR():

        '''subtract a row'''
        global rMatrixSize
        if rMatrixSize>2:
            for widget in rootb.grid_slaves(row=rMatrixSize+1):
                widget.destroy() #delete widget
                entries1.remove(widget) #delete widget from list of widgets
            rMatrixSize-=1

    def subtractC():

        '''subtract a column'''
        global cMatrixSize
        if cMatrixSize > 2:
            for widget in rootb.grid_slaves(column=cMatrixSize):
                widget.destroy()
                if 'label' not in str(widget): #test to see if this is a widget in list of widgets
                    entries1.remove(widget)
            cMatrixSize -= 1

    for x in range(rMatrixSize):
        for y in range(rMatrixSize):
            entry = Entry(width=3, relief=GROOVE)
            entry.grid(column=x + 1, row=y + 2, pady=15, padx=15)
            entries1.append(entry)
        Label(rootb, text='X' + str(x)).grid(column=x + 1, row=1) #create initial matrix
    addR = Button(text='+', font=('Comic Sans MS', 14), bg='light grey',  command=addR) #binds functions to buttons
    addR.grid(row=2, column=0, columnspan=2, pady=5, padx=30)
    subtractR = Button(rootb, text='-', font=('Comic Sans MS', 14), bg='light grey',
                        command=subtractR)
    subtractR.grid(row=1, columnspan=2, sticky = S, padx=30)
    addC = Button(rootb, text='+', font=('Comic Sans MS', 14), bg='light grey', command=addC)
    addC.grid(row=0, column=2)
    subtractC = Button(rootb, text='-', font=('Comic Sans MS', 14), bg='light grey',
                       command=subtractC)
    subtractC.grid(row=0, column=1)
    submit = Button(rootb, text='Submit', font=('Comic Sans MS', 12), bg='light grey', command=goCalulate)
    submit.grid(row=0, padx=10, pady=10)
    rootb.mainloop()


def column(matrix, columnNo):
    return [matrix[x][columnNo] for x in range(len(matrix))]


def rowReduce(matrix, topLeft):
    #recalculate rmatrixsize and cmatrixsize
    rMatrixSize = len(matrix)
    cMatrixSize = len(matrix[0])
    if rMatrixSize != 1:
        #find pivot
        for x in range(cMatrixSize):
            if column(matrix, x) != [0.0 for y in range(rMatrixSize)]:
                pivotColumn = x
                break
            elif x == cMatrixSize - 1:
                return
        for x in range(rMatrixSize):
            potentialPivot = column(matrix, pivotColumn)[x]
            if potentialPivot != 0:
                pivotRow = x
                break
        if pivotRow+1 == rMatrixSize:
            return
        #create zeros below pivot
        for y in range(rMatrixSize-1):
            scalaR1R2 = matrix[pivotRow+y+1][pivotColumn]/matrix[pivotRow][pivotColumn]
            scaledR1 = [scalaR1R2*matrix[0][x] for x in range(cMatrixSize)]
            matrix[y+1] = [matrix[y+1][x]-scaledR1[x] for x in range(cMatrixSize)]
        #cover row containing pivot, and repeat
        for x in range(rMatrixSize):
            for y in range(cMatrixSize):
                # print(matrix[x][y])
                # print(imatrix[topLeft[0]+x][topLeft[1]+y])
                imatrix[topLeft[0]+x][topLeft[1]+y] = matrix[x][y]
        topLeft = [topLeft[0] + 1 + pivotRow, topLeft[1] + 1 + pivotColumn]
        matrix = matrix[1:]
        matrix = [matrix[x][1:] for x in range(rMatrixSize-1)]
        rowReduce(matrix, topLeft)
    else:
        return

def CalculateDet():
    #get data from determinant program inputs
    global data
    global matrixSize
    global imatrix
    data = []
    imatrix = []
    rMatrixSize = matrixSize
    cMatrixSize = matrixSize
    for entry in entries:
        data.append(entry.get())
    for num in range(len(data)):
        try:
            data[num] = float(data[num])
        except ValueError:
            print('you gotta use numbers, silly!')
    for x in range(rMatrixSize):
        imatrix.append(data[cMatrixSize * x:cMatrixSize * (x + 1)])
    for x in range(cMatrixSize):
        if column(imatrix, x) != [0.0 for y in range(rMatrixSize)]:
            initpivotColumn = x
            break
        elif x == cMatrixSize - 1:
            roota.destroy()
            root = Tk()
            root.title('Determinant')
            answer = Label(root, text='Your determinant is', font=('Comic Sans MS', 36))
            ans2 = Label(root, text='0', font=('Comic Sans MS', 36))
            answer.pack()
            ans2.pack()
            root.mainloop()
    for x in range(rMatrixSize):
        potentialPivot = column(imatrix, initpivotColumn)[x]
        if potentialPivot != 0:
            initpivotRow = x
            break
    firstTopLeft = [initpivotRow, initpivotColumn]
    roota.destroy()
    rowReduce(imatrix, firstTopLeft)

    determinant = 1
    for x in range(len(imatrix)):
        determinant *= imatrix[x][x]

    root = Tk()
    root.title('Determinant')
    answer = Label(root, text='Your determinant is', font=('Comic Sans MS', 36))
    ans2 =  Label(root, text=int(determinant), font=('Comic Sans MS', 36))
    answer.pack()
    ans2.pack()
    root.mainloop()



def CalculateSyst():
    #get data from determinant program inputs
    global data
    global rMatrixSize
    global cMatrixSize
    global imatrix
    data = []
    imatrix = []
    temp = []
    for entry in entries1:
        data.append(entry.get())
    for num in range(len(data)):
        try:
            data[num] = Decimal(data[num])
        except ValueError:
            print('you gotta use numbers, silly!')
    for x in range(rMatrixSize):
        for y in range(cMatrixSize):
            temp.append(data[rMatrixSize*y+x])
    for x in range(rMatrixSize):
        imatrix.append(temp[cMatrixSize * x:cMatrixSize * (x + 1)])
    for x in range(cMatrixSize):
        if column(imatrix, x) != [0.0 for y in range(rMatrixSize)]:
            initpivotColumn = x
            break
    for x in range(rMatrixSize):
        potentialPivot = column(imatrix, initpivotColumn)[x]
        if potentialPivot != 0:
            initpivotRow = x
            break
    firstTopLeft = [initpivotRow, initpivotColumn]
    rootb.destroy()
    rowReduce(imatrix, firstTopLeft)
    #check for no solution
    rMatrixSize = len(imatrix)
    cMatrixSize = len(imatrix[0])

    for x in range(rMatrixSize):
        for y in range(cMatrixSize):
            imatrix[x][y] = imatrix[x][y] / imatrix[x][x]
    for x in range(rMatrixSize - 1):
        for y in range(cMatrixSize - 2 - x):
            imatrix[rMatrixSize - 2 - y - x][cMatrixSize - 1] = \
                imatrix[rMatrixSize - 2 - y - x][cMatrixSize - 1] - (imatrix[rMatrixSize - 2 - y][cMatrixSize - 2 - x] * \
                                                                     imatrix[rMatrixSize - 1 - x][cMatrixSize - 1])
            imatrix[rMatrixSize - 2 - y - x][cMatrixSize - 2 - x] = 0
    for x in range(rMatrixSize):
        for y in range(cMatrixSize):
            imatrix[x][y] = imatrix[x][y] / imatrix[x][x]
            imatrix[x][y] = round(imatrix[x][y], 2)
    # for x in range(rMatrixSize):
    #     for y in range(cMatrixSize):
    #         imatrix[x][y] = round(imatrix[x][y], 2)
    root = Tk()
    root.title('System of Equations')
    answer = Label(root, text=imatrix, font=('Comic Sans MS', 36))
    answer.pack()
    root.mainloop()




#Det()
#Syst()

firstWin()