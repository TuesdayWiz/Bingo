import random
from tkinter import Tk, N, E, S, W, StringVar, ttk, font

letters = ['B', 'I', 'N', 'G', 'O']
been_called = []
buttons = []
draws = []
been_pressed_after = 0

def bingo_let_num():
    return random.choice(draws)

def get_bingo_call():
    if len(been_called) < 75:
        call = bingo_let_num()
        
        # Makes sure the same call isn't made twice
        valid_call = False
        while valid_call != True:
            if call in been_called:
                call = bingo_let_num()
            else:
                valid_call = True
        
        been_called.append(call)
        bingo_call.set(call)
        buttons[draws.index(call)].config(background='#ff5c5c')
    else:
        no_more.grid(column=0, columnspan=5)
        
        global been_pressed_after
        if been_pressed_after % 2 == 0:
            color = '#1035ac'
        else:
            color = '#fbe5cd'
        
        for b in buttons:
            b.config(background=color)
        
        been_pressed_after += 1

def reset_board():
    # Sets some variables back to their default states, removes the "please reset" text
    been_called.clear()
    bingo_call.set('')
    no_more.grid_remove()
    
    # Resets the squares back to green
    for b in buttons:
        b.config(background='#bcf5bc')

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
BoardFont = font.Font(family='Helvetica', name='appBoardFont', size=24, weight='bold')
NoMoreFont = font.Font(family='Helvetica', name='appNoMoreFont', size=16, weight='bold')

# Sets up the various buttons and labels that will be shown/used
ttk.Button(mainframe, text="Call", command=get_bingo_call, width=10).grid(column=0, row=16, sticky=(N, W, E, S))
ttk.Button(mainframe, text='Reset', command=reset_board, width=10).grid(column=4, row=16, sticky=(N, W, E, S))
ttk.Label(mainframe, textvariable=bingo_call, font=BingoFont).grid(column=2, row=16, sticky=(N, W, E, S))
no_more = ttk.Label(mainframe, text="The board is full.  Please reset.", font=NoMoreFont)

#------------------------------ BINGO BOARD ------------------------------#
# Sets up the BINGO heading
bingo_pos = 0
for l in letters:
    ttk.Label(mainframe, text=l, font=BoardFont, background='#b22b27', width=10, anchor='center').grid(column=bingo_pos, row=0, sticky=(N, W, E, S))
    bingo_pos += 1

# Creates the bingo 
#    NOTE FOR THE FUTURE: This definitely isn't the best idea, but it allows me to create variables 
#    with custom names without individually doing it, so it works for this
plus = 0
for x in letters:
    for n in range(1, 16):
        globals()[f'{x.lower()}{n + (15 * plus)}'] = ttk.Label(mainframe, text=f'{n + (15 * plus)}', font=BoardFont, background='#bcf5bc', width='10', anchor='center')
        buttons.append(globals()[f'{x.lower()}{n + (15 * plus)}'])
        draws.append(f'{x}-{n + (15 * plus)}')
    plus += 1

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
