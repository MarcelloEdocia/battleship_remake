import tkinter

class EndPage(tkinter.Frame):

    def __init__(self, parent, App):
        self.application = App
        self.config = App.config
        super().__init__(parent)
        self.configure(bg="grey")

        self.grid(row=0, column=0, sticky="nsew")
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)

        self.pixelVirtual = tkinter.PhotoImage(width=5, height=2)
        self.button_width = self.config.side//4
        self.button_height = self.config.side//20

        self.pixelVirtual = tkinter.PhotoImage(width=5, height=2)

        self.button_width = self.config.side//2.5
        self.button_height = self.config.side//20

        self.mainFrame = tkinter.Frame(self, height=self.config.side, width=self.config.side, bg="grey")
        self.mainFrame.pack(expand=True)

        self.create_label()
        self.create_playbutton()
        self.see_highscore()
        self.create_exitbutton()


    def create_label(self):
        self.firsttext = tkinter.Label(self.mainFrame, text="You Win!", font=("Arial", 22), bg="grey")
        self.firsttext.pack()
        self.secondtext = tkinter.Label(self.mainFrame, text="", bg="grey")
        self.secondtext.pack()
        self.thirdtext = tkinter.Label(self.mainFrame, text="", bg="grey")
        self.thirdtext.pack()

    def create_playbutton(self):
        self.playbutton = tkinter.Button(self.mainFrame, text="Play again", font=("Arial", 18), image=self.pixelVirtual, width=self.button_width, height=self.button_height, compound="c", command=lambda:self.application.play_again())
        self.playbutton.pack(pady=10)

    def create_exitbutton(self):
        self.exitbutton = tkinter.Button(self.mainFrame, text="Exit", font=("Arial", 18), command=lambda:self.application.create_popup(),  image=self.pixelVirtual, width=self.button_width,height=self.button_height, compound="c")
        self.exitbutton.pack(pady=10)

    def see_highscore(self):
        self.returnbutton = tkinter.Button(self.mainFrame, text="Return", font=("Arial", 18), command=lambda:self.application.gotomenu(),  image=self.pixelVirtual, width=self.button_width,height=self.button_height, compound="c")
        self.returnbutton.pack(pady=50)