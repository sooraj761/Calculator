import tkinter as tk
import tkinter.ttk as ttk
from ttkthemes import ThemedStyle


from tkinter import *

root = tk.Tk ()

# root.configure(background="#272533")
style = ThemedStyle(root)
style.set_theme("winxpblue")

root.iconbitmap ( r"calculator.ico" )

root.geometry ( "600x660" )
root.resizable ( 0, 0 )
root.title ( "Calculator" )


value = ""


def clicked(num):
    global value
    value = value + str ( num )
    data.set ( value )


def clickedEqual():
    try:
        global value
        equation = (eval(value))
        value = str("%.4f" % (equation))
        data.set(value)
        value = ""
    except:
        data.set("Error")
        value = ""


def clear():
    global value
    value = ""
    data.set ( value )



data = StringVar ()

font = ('Digital-7', 48)

screen = ttk.Label ( root, text = '0.0000', font = font, textvariable = data, justify = 'right', relief = SUNKEN )
screen.pack (pady =15, padx = 5, fill = X )

numRow1 = ttk.Frame ( root)
numRow1.pack ( expand = True, padx = 6, fill = "both" )

btn7 = ttk.Button ( numRow1, text = "7", command = lambda : clicked(7) )
btn7.pack ( side = LEFT, expand = True, pady =5, padx = 5, fill = "both" )

btn8 = ttk.Button ( numRow1, text = "8", command = lambda : clicked(8) )
btn8.pack ( side = LEFT, expand = True, pady =5, padx = 5, fill = "both" )

btn9 = ttk.Button ( numRow1, text = "9", command = lambda : clicked(9) )
btn9.pack ( side = LEFT, expand = True, pady =5, padx = 5, fill = "both" )

btnDiv = ttk.Button ( numRow1, text = "÷",command = lambda : clicked("/") )
btnDiv.pack ( side = LEFT, expand = True, pady =5, padx = 5, fill = "both" )

numRow2 = ttk.Frame ( root)
numRow2.pack ( expand = True, padx = 6, fill = "both" )

btn4 = ttk.Button ( numRow2, text = "4",command = lambda : clicked(4) )
btn4.pack ( side = LEFT, expand = True, pady =5, padx = 5, fill = "both" )

btn5 = ttk.Button ( numRow2, text = "5", command = lambda : clicked(5) )
btn5.pack ( side = LEFT, expand = True, pady =5, padx = 5, fill = "both" )

btn6 = ttk.Button ( numRow2, text = "6", command = lambda : clicked(6) )
btn6.pack ( side = LEFT, expand = True, pady =5, padx = 5, fill = "both" )

btnMul = ttk.Button ( numRow2, text = "x",  command = lambda : clicked("*") )
btnMul.pack ( side = LEFT, expand = True, pady =5, padx = 5, fill = "both" )

numRow3 = ttk.Frame ( root)
numRow3.pack ( expand = True, padx = 6, fill = "both" )

btn1 = ttk.Button ( numRow3, text = "1", command = lambda : clicked(1) )
btn1.pack ( side = LEFT, expand = True, pady =5, padx = 5, fill = "both" )

btn2 = ttk.Button ( numRow3, text = "2", command = lambda : clicked(2) )
btn2.pack ( side = LEFT, expand = True, pady =5, padx = 5, fill = "both" )

btn3 = ttk.Button ( numRow3, text = "3", command = lambda : clicked(3) )
btn3.pack ( side = LEFT, expand = True, pady =5, padx = 5, fill = "both" )

btnMin = ttk.Button ( numRow3, text = "−", command = lambda : clicked("-") )
btnMin.pack ( side = LEFT, expand = True, pady =5, padx = 5, fill = "both" )

numRow4 = ttk.Frame ( root )
numRow4.pack ( expand = True, padx = 6, fill = "both" )

btn0 = ttk.Button ( numRow4, text = "0", command = lambda : clicked(0) )
btn0.pack ( side = LEFT, expand = True, pady =5, padx = 5, fill = "both" )

btnDot = ttk.Button ( numRow4, text = "•", command = lambda : clicked(".") )
btnDot.pack ( side = LEFT, expand = True, pady =5, padx = 5, fill = "both" )

btnPers = ttk.Button ( numRow4, text = "%", command = lambda : clicked("%") )
btnPers.pack ( side = LEFT, expand = True, pady =5, padx = 5, fill = "both" )

btnPlus = ttk.Button ( numRow4, text = "+", command = lambda : clicked("+") )
btnPlus.pack ( side = LEFT, expand = True, pady =5, padx = 5, fill = "both" )

numRow5 = ttk.Frame ( root)
numRow5.pack ( expand = True, padx = 6, pady = (0, 5), fill = "both" )

btnC = ttk.Button ( numRow5, text = "AC", command = clear )
btnC.pack ( side = LEFT, expand = True, pady =5, padx = 5, fill = "both" )

btnEqual = ttk.Button ( numRow5, text = "=", command = clickedEqual )
btnEqual.pack ( side = LEFT, expand = True, pady =5, padx = 5, fill = "both" )

mainloop ()