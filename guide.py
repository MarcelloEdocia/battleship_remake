import tkinter
from tkinter import ttk

class GuidePage(tkinter.Frame):

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


        self.mainFrame = tkinter.Frame(self, height=self.config.side, width=self.config.side, bg="white")
        self.mainFrame.pack(expand=True)

        self.create_guide()
        self.create_returnbutton()


    def create_guide(self):

        self.style = ttk.Style()
        self.style.configure("my_style.Treeview", highlightthickness=0, font=("Helvetica", 40, "bold"), rowheight=40, bd=0)
        self.style.configure("my_style.Treeview.Heading", font=("Helvetica",25, "bold"), rowheight=40)

        self.guide_treeview = ttk.Treeview(self.mainFrame, style="my_style.Treeview")
        self.guide_treeview['columns'] = ("How To Play", "ghost")
        self.guide_treeview.column("#0", width=0, stretch=tkinter.NO)
        self.guide_treeview.column("How To Play", anchor=tkinter.CENTER, width=self.config.side)
        self.guide_treeview.column("ghost", anchor=tkinter.E , width=0, stretch=tkinter.NO)

        self.guide_treeview.heading("#0", text="", anchor=tkinter.W)
        self.guide_treeview.heading("How To Play", text="How To Play", anchor=tkinter.CENTER)
        self.guide_treeview.heading("ghost", text="", anchor=tkinter.E)

        self.guide_treeview.insert(parent="", index="end", text="", iid=1, values=("", ""))
        self.guide_treeview.insert(parent="", index="end", text="", iid=2, values=("", ""))

        self.guide_treeview.insert(parent="",index= "end",  text="",iid=3, values=("You have to find a ship located in one of the boxes", ""))
        self.guide_treeview.insert(parent="", index="end", text="", iid=4,
                                   values=("The default image in the box is Spongebob", ""))
        self.guide_treeview.insert(parent="", index="end", text="", iid=5,
                                   values=("If you're wrong, the image will turn into Courage the Cowardly Dog", ""))
        self.guide_treeview.insert(parent="", index="end", text="", iid=6,
                                   values=("But if you're right, the image will turn into Finn the Human", ""))
        self.guide_treeview.insert(parent="", index="end", text="", iid=7, values=("All your score will be saved automatically ;)", ""))

        self.guide_treeview.pack(expand=True)


    def create_returnbutton(self):
        self.returnbutton = tkinter.Button(self.mainFrame, text="Return", font=("Arial", 15),image=self.pixelVirtual,height=self.button_height, width=self.button_width,  compound="c",
                                           command=lambda:self.application.gotomenu(), bg="grey")
        self.returnbutton.pack(side="bottom",pady=20)