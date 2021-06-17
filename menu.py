import tkinter

class MenuPage(tkinter.Frame):

    def __init__(self, parent, App):
        self.application = App
        self.config = App.config
        super().__init__(parent)
        self.configure(bg="grey")

        self.grid(row=0, column=0, sticky="nsew")
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)

        self.pixelVirtual = tkinter.PhotoImage(width=4, height=2)

        self.create_mainframe()


    def create_mainframe(self):
        self.mainframe = tkinter.Frame(self, height=self.config.side, bg="grey")
        self.mainframe.pack(expand=True)
        btn_width = self.config.side//2
        btn_height = self.config.side//18

        self.menu_label = tkinter.Label(self.mainframe, text="MENU", font=("Helvetica", 40), bg="grey")
        self.menu_label.pack(expand=True, pady=10)

        self.baseng = tkinter.Label(self.mainframe, text="", bg="grey")
        self.baseng.pack(expand=True)
        self.baseng2 = tkinter.Label(self.mainframe, text="", bg="grey")
        self.baseng2.pack(expand=True)

        self.button1 = tkinter.Button(self.mainframe, text="How To Play", image=self.pixelVirtual, width=btn_width, height=btn_height, compound="c", font=("Arial", 14, "bold"), command=lambda:self.application.open_guide())
        self.button1.pack(expand=True, pady=10)

        self.button2 = tkinter.Button(self.mainframe, text="Play the Game", image=self.pixelVirtual, width=btn_width, height=btn_height, compound="c", font=("Arial", 14, "bold"), command=lambda:self.application.open_game())
        self.button2.pack(expand=True, pady=10)

        self.button3 = tkinter.Button(self.mainframe, text="See The Leaderboard", image=self.pixelVirtual, width=btn_width, height=btn_height, compound="c", font=("Arial", 14, "bold"), command=lambda:self.application.open_highscore())
        self.button3.pack(expand=True, pady=10)

        self.button4 = tkinter.Button(self.mainframe, text="Exit Game", image=self.pixelVirtual, width=btn_width, height=btn_height, compound="c" ,font=("Arial", 14, "bold"), command=lambda:self.application.create_popup())
        self.button4.pack(expand=True, pady=10)