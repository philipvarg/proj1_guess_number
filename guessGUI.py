import tkinter as tk
# from tkinter import END  # end of text in text-box for deletion
# from tkinter import IntVar  # for checkbox selection
from PIL import ImageTk, Image 
import random as rd

# **** FUNCTIONS ************************************************************************
# ********** LOWER FRAME ***********************************
def start_game():
    global halfMaxrd, halfTries, hints, guessNum,tries
    global try_label, num_but_list, lower_frame

    # **** setup random **********************************************
    maxrd = 20
    halfMaxrd = int(maxrd/2)
    tries = 10
    halfTries = int(tries/2)
    hints = {"odd": True, "half": True}
    guessNum = rd.randint(1, maxrd)

    # ********************************************************************************
    lower_frame = tk.Frame(root, bg= 'gray6', width=800, height=650)
    lower_frame.pack()
    lower_frame.grid_propagate(0)
    # ********************************************************************************

    # **** LABEL FRAME TO HOLD 20 NUMBER BUTTONS **************
    digit_frame = tk.LabelFrame(lower_frame, text=' Click on a number ', font= (14), 
                                bg= bgcol, fg= 'gray77', borderwidth=5, width=500, height=400)
    digit_frame.grid(row=0, column=0, padx= 20, pady= 20)


    # **** 20 num buttons arranged in label frame **************
    num_but_list = []  # list to hold num_but
    for r in range(0, 4):
        for c in range(0, 5):
            num = 5*r+c
            num_but = tk.Button(digit_frame, text=str(num+1), font= ('Arial', 16), 
                                fg='black', bg= 'DeepSkyBlue2', 
                                activebackground= 'DeepSkyBlue3', cursor= 'hand2',
                                width=4, height=2, border=4,  relief= 'raise',
                                command= lambda idx = num: on_click(idx, tries))

            num_but.grid(row=r, column=c, padx=(5,0), pady=(5,0))
            num_but_list.append(num_but)

    try_label = tk.Label(lower_frame, 
                        text= f'Tries remaining: {tries}', 
                        font= (12), bg= bgcol, fg= 'gray100', 
                        borderwidth=5)
    try_label.place(x= 460, y= 50, width= 280, height=50)


def on_click(idx, num):    
    global tries
    player = idx + 1

    if tries > 0:
        # blue to pink
        num_but_list[idx].config(bg= 'Hotpink1', fg= 'gray47') 
        # tries counter
        tries = num - 1

        if player != guessNum:
            try_label.config(text= f'Tries remaining : {tries}')
        else:
            try_label.config(text= f'You won in {10 - tries} tries')
        
        if player == guessNum:
            win_label = tk.Label(lower_frame, text= 'YOU WIN!!', 
                                 font= ('Arial',20), bg= 'green2')
            win_label.grid(row= 1, column= 0, ipadx= 20, ipady= 20)
            tries = 0
            # create_exit_but()
            create_replay_but()
            
        elif tries <= 0 and player != guessNum:
            lose_label = tk.Label(lower_frame, text= 'NO MORE TRIES !\nGAME OVER', 
                                  font= ('Arial',16), bg= 'red')
            lose_label.grid(row= 1, column= 0, ipadx= 20, ipady= 20)
            try_label.destroy()
            reveal_label = tk.Label(lower_frame, 
                    text= f'Winning number : {guessNum}', 
                    font= ('Arial',14,'bold'), bg= bgcol, fg= 'yellow', 
                    borderwidth=5)
            reveal_label.place(x= 460, y= 50, width= 280, height=50)
            create_exit_but()
            create_replay_but()
            
        else:
            # setup to show first hint
            if tries > halfTries and tries < 8 and hints["half"] == True:
                hints["half"] = False
                if guessNum <= halfMaxrd:
                    tex = f"My number is less than {halfMaxrd + 1}"
                else:
                    tex = f"My number is more than {halfMaxrd}"
                hint_1 = tk.Label(lower_frame, 
                                        text= tex, 
                                        font= (12), bg= bgcol, fg= 'gray77', 
                                        borderwidth=5)
                hint_1.place(x= 460, y= 150, width= 280, height=50)
                
            elif tries < halfTries and hints["odd"] == True:
                hints["odd"] = False
                if guessNum % 2 == 0:
                    tex = "My number is even"
                else:
                    tex = "My number is odd"
                hint_2 = tk.Label(lower_frame, 
                                        text= tex, 
                                        font= (12), bg= bgcol, fg= 'gray77', 
                                        borderwidth=5)
                hint_2.place(x= 460, y= 250, width= 280, height=50)

def create_replay_but():
    replay_but = tk.Button(lower_frame, text= 'Replay', font= ('Arial', 16), 
                            fg='black', bg= 'DeepSkyBlue2', cursor= 'hand2',
                            width=4, height=2, border=4,  relief= 'ridge', 
                            command= replay_game)
    replay_but.place(x= 460, y= 420, width= 120, height=50)

def replay_game():
    lower_frame.destroy()
    start_game()
    create_exit_but()
    
def create_exit_but():
    exit_but = tk.Button(lower_frame, text= 'Exit', font= ('Arial', 16), 
                            fg='black', bg= 'DeepSkyBlue2', cursor= 'hand2', 
                            width=4, height=2, border=4,  relief= 'ridge', 
                            command= kill_game)
    exit_but.place(x= 600, y= 420, width= 120, height=50)

def kill_game():
    root.destroy()

# **** CREATE ROOT WINDOW ********************************************************************
# Colors
bgcol = '#123456'

# define ROOT window
root = tk.Tk()
root.title('Test your Intuition')
root.iconbitmap('python.ico')
# calculate screen center into x, y.
root_width = 800
root_height = 700
sc_width = root.winfo_screenwidth()
sc_height = root.winfo_screenheight()
x = int((sc_width/2) - (root_width/2))
y = int((sc_height/2) - (root_height/2))

root.geometry(f'{root_width}x{root_height}+{x}+{y}')
root.resizable(0,0)
root.config(bg= bgcol)


# ********** CREATE TITLE FRAME ***********************************************************
# Define frames
title_frame = tk.Frame(root, bg= bgcol, width=630, height=150)
# Arrange frames onto root by using Pack
title_frame.pack(padx= 40, pady= 10)
# Use the correct propagate for each frame ie grid or pack
title_frame.grid_propagate(0)  # because we are using grid to arrange widgets in this frame

# ********** IMAGE for title frame **************
think_img = ImageTk.PhotoImage(Image.open('think2.png'))
think_label = tk.Label(title_frame, image=think_img, bg= bgcol)
think_label.grid(row=0, column=0, padx=10, pady=10)

# ********** TEXT for title frame **************
title = tk.Label(title_frame, 
                 text= (f'Test your intuition by guessing my number from 1 to 20.\nYou get 10 tries and 2 hints.'),
                 font= ('Arial', 16), bg= bgcol, fg='lime')
title.grid(row=0,column=1, padx=10, sticky= 'W')
title = tk.Label(title_frame, text=' Can you do it in less?', 
                 font= ('Arial', 16), bg= bgcol, fg='lime')
title.grid(row=1, column=1, padx=10)

start_game()
create_exit_but()
# **** runs the main root window *************
root.mainloop()