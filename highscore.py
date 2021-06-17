import tkinter
from tkinter import ttk

from json import load


class HighScorePage(tkinter.Frame):

    def __init__(self, parent, App):
        self.application = App
        self.config = App.config
        super().__init__(parent)
        self.configure(bg="white")

        self.grid(row=0, column=0, sticky="nsew")
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)

        self.pixelVirtual = tkinter.PhotoImage(width=5, height=2)
        self.button_width = self.config.side//6
        self.button_height = self.config.side//20

        #Highscore
        self.highscores = self.load_data()

        #self.mainframe = tkinter.Frame(self, height=self.config.side, width=self.config.side)
        #self.mainframe.pack(expand=True)

        self.firstframe = tkinter.Frame(self, height=4*self.config.side//5, width=self.config.side, bg="white")
        self.firstframe.grid(row=0, column=0)

        self.secondframe = tkinter.Frame(self, height=self.config.side//5, width=self.config.side, bg="white")
        self.secondframe.grid(row=1, column=0)

        self.grid_rowconfigure(0, weight=4)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.create_leaderboard()

    def load_data(self):
        with open("./data/score.json", "r") as file:
            self.data = load(file)
            return self.data


    def create_leaderboard(self):

        #Creating scrollbar
        self.tree_scroll = tkinter.Scrollbar(self.firstframe)
        self.tree_scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)


        self.style = ttk.Style()
        self.style.configure("my_style.Treeview", highlightthickness=0, font=("Arial", 12), rowheight=38, bd=0)
        self.style.configure("my_style.Treeview.Heading", font=("Arial", 12, "bold"))


        self.highscores_treeview = ttk.Treeview(self.firstframe, style="my_style.Treeview", yscrollcommand=self.tree_scroll.set)
        #Configuring the scrollbar
        self.tree_scroll.config(command=self.highscores_treeview.yview)

        #Configuring the treeviewc
        self.highscores_treeview['columns'] = ("Username", "Score", "Win Rate")
        self.highscores_treeview.column("#0", width=0, stretc=tkinter.NO)
        self.highscores_treeview.column("Username", anchor=tkinter.CENTER, width=self.config.side//3)
        self.highscores_treeview.column("Score", anchor=tkinter.CENTER, width=self.config.side//3)
        self.highscores_treeview.column("Win Rate", anchor=tkinter.CENTER, width=self.config.side//3)


        # Creating headings
        self.highscores_treeview.heading("#0", text="", anchor=tkinter.W)
        self.highscores_treeview.heading("Username", text="Username", anchor=tkinter.CENTER)
        self.highscores_treeview.heading("Score", text="Score", anchor=tkinter.CENTER)
        self.highscores_treeview.heading("Win Rate", text="Win Rate", anchor=tkinter.CENTER)

        scores = self.highscores
        count = 0
        for score in scores:
            for name, user_detail in score.items():
                username = f"{user_detail['nick']}"
                username_score = f"{user_detail['user_score']}"
                username_winrate = f"{user_detail['win_rate']}%"
                self.highscores_treeview.insert(parent="", index="end", iid=count, text="", values=(username, username_score, username_winrate))
                count += 1
        self.highscores_treeview.pack(expand=True)



        self.returnbutton = tkinter.Button(self.secondframe,font=("Arial", 15),  image=self.pixelVirtual, compound="c", height=self.button_height,bg="grey", bd=1, width=self.button_width, text="Return", command=lambda:self.application.gotomenu())
        self.returnbutton.pack(expand=True, pady=5)

