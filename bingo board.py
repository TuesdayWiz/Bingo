import random
from tkinter import Tk, N, E, S, W, StringVar, ttk, font, Button

letters = ['B', 'I', 'N', 'G', 'O']
been_called = []
buttons = []

def reset_board():
    # Sets some variables back to their default states, removes the "please reset" text
    been_called.clear()
    bingo_call.set('')
    no_more.grid_remove()
    
    # Resets the squares back to green
    for b in buttons:
        b.config(background='#bcf5bc')

def on_click(button_num):
    b = buttons[button_num - 1]
    if b.cget('bg') == '#bcf5bc':
        b.config(bg='#ff5c5c')
    else:
        b.config(bg='#bcf5bc')

# Sets up the window with the correct title and icon
root = Tk()
root.title("Bingo!")
root.iconbitmap("bingo.ico")    # Icon by IconMarketPK on Flaticon.com


# Sets up the grid for use in positioning
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Sets up some variables (including fonts)
bingo_call = StringVar()
BingoFont = font.Font(family='Helvetica', name='appBingoFont', size=48, weight='bold')
BoardFont = font.Font(family='Helvetica', name='appBoardFont', size=15)
NoMoreFont = font.Font(family='Helvetica', name='appNoMoreFont', size=16, weight='bold')

# Sets up the various buttons and labels that will be shown/used
Button(mainframe, text='Reset', command=reset_board, width=10).grid(column=4, row=16, sticky=(N, W, E, S))
ttk.Label(mainframe, textvariable=bingo_call, font=BingoFont).grid(column=2, row=16, sticky=(N, W, E, S))
no_more = ttk.Label(mainframe, text="The board is full.  Please reset.", font=NoMoreFont)

#------------------------------ BINGO BOARD ------------------------------#
# Sets up the BINGO heading
bingo_pos = 0
for l in letters:
    ttk.Label(mainframe, text=l, font=NoMoreFont, background='#b22b27', width=10, anchor='center').grid(column=bingo_pos, row=0, sticky=(N, W, E, S))
    bingo_pos += 1

# Creates the bingo 
#   Bs
b1 = Button(mainframe, text='1', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(1))
b2 = Button(mainframe, text='2', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(2))
b3 = Button(mainframe, text='3', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(3))
b4 = Button(mainframe, text='4', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(4))
b5 = Button(mainframe, text='5', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(5))
b6 = Button(mainframe, text='6', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(6))
b7 = Button(mainframe, text='7', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(7))
b8 = Button(mainframe, text='8', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(8))
b9 = Button(mainframe, text='9', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(9))
b10 = Button(mainframe, text='10', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(10))
b11 = Button(mainframe, text='11', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(11))
b12 = Button(mainframe, text='12', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(12))
b13 = Button(mainframe, text='13', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(13))
b14 = Button(mainframe, text='14', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(14))
b15 = Button(mainframe, text='15', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(15))
#   Is
i16 = Button(mainframe, text='16', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(16))
i17 = Button(mainframe, text='17', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(17))
i18 = Button(mainframe, text='18', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(18))
i19 = Button(mainframe, text='19', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(19))
i20 = Button(mainframe, text='20', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(20))
i21 = Button(mainframe, text='21', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(21))
i22 = Button(mainframe, text='22', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(22))
i23 = Button(mainframe, text='23', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(23))
i24 = Button(mainframe, text='24', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(24))
i25 = Button(mainframe, text='25', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(25))
i26 = Button(mainframe, text='26', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(26))
i27 = Button(mainframe, text='27', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(27))
i28 = Button(mainframe, text='28', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(28))
i29 = Button(mainframe, text='29', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(29))
i30 = Button(mainframe, text='30', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(30))
#   Ns
n31 = Button(mainframe, text='31', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(31))
n32 = Button(mainframe, text='32', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(32))
n33 = Button(mainframe, text='33', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(33))
n34 = Button(mainframe, text='34', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(34))
n35 = Button(mainframe, text='35', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(35))
n36 = Button(mainframe, text='36', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(36))
n37 = Button(mainframe, text='37', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(37))
n38 = Button(mainframe, text='38', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(38))
n39 = Button(mainframe, text='39', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(39))
n40 = Button(mainframe, text='40', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(40))
n41 = Button(mainframe, text='41', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(41))
n42 = Button(mainframe, text='42', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(42))
n43 = Button(mainframe, text='43', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(43))
n44 = Button(mainframe, text='44', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(44))
n45 = Button(mainframe, text='45', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(45))
#   Gs
g46 = Button(mainframe, text='46', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(46))
g47 = Button(mainframe, text='47', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(47))
g48 = Button(mainframe, text='48', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(48))
g49 = Button(mainframe, text='49', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(49))
g50 = Button(mainframe, text='50', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(50))
g51 = Button(mainframe, text='51', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(51))
g52 = Button(mainframe, text='52', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(52))
g53 = Button(mainframe, text='53', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(53))
g54 = Button(mainframe, text='54', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(54))
g55 = Button(mainframe, text='55', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(55))
g56 = Button(mainframe, text='56', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(56))
g57 = Button(mainframe, text='57', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(57))
g58 = Button(mainframe, text='58', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(58))
g59 = Button(mainframe, text='59', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(59))
g60 = Button(mainframe, text='60', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(60))
#   Os
o61 = Button(mainframe, text='61', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(61))
o62 = Button(mainframe, text='62', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(62))
o63 = Button(mainframe, text='63', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(63))
o64 = Button(mainframe, text='64', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(64))
o65 = Button(mainframe, text='65', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(65))
o66 = Button(mainframe, text='66', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(66))
o67 = Button(mainframe, text='67', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(67))
o68 = Button(mainframe, text='68', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(68))
o69 = Button(mainframe, text='69', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(69))
o70 = Button(mainframe, text='70', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(70))
o71 = Button(mainframe, text='71', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(71))
o72 = Button(mainframe, text='72', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(72))
o73 = Button(mainframe, text='73', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(73))
o74 = Button(mainframe, text='74', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(74))
o75 = Button(mainframe, text='75', font=BoardFont, background='#bcf5bc', width='3', anchor='center', command=lambda: on_click(75))

buttons = [
    b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15,
    i16, i17, i18, i19, i20, i21, i22, i23, i24, i25, i26, i27, i28, i29, i30,
    n31, n32, n33, n34, n35, n36, n37, n38, n39, n40, n41, n42, n43, n44, n45,
    g46, g47, g48, g49, g50, g51, g52, g53, g54, g55, g56, g57, g58, g59, g60,
    o61, o62, o63, o64, o65, o66, o67, o68, o69, o70, o71, o72, o73, o74, o75
           ]

# Puts them all on the grid (thank god for loops)
row = 1
column = 0
for b in buttons:
    b.grid(row=row, column=column, sticky=(N, W, E, S))
    
    row += 1
    if row > 15:
        row = 1
        column += 1

g_columns, g_rows = mainframe.grid_size()
for row in range(g_rows):
    mainframe.rowconfigure(index=row, weight=1)

for column in range(g_columns):
    mainframe.columnconfigure(index=column, weight=1)

# Starts the window loop (to make sure it doesn't close)
root.state('zoomed')
root.mainloop()
