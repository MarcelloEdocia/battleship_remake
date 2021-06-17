import tkinter

class SignUpPage(tkinter.Frame):

    def __init__(self, parent, App):
        self.application = App
        self.config = App.config
        super().__init__(parent)
        self.configure(bg="grey")

        self.grid(row=0, column=0, sticky="nsew")
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)

        self.button_image = tkinter.PhotoImage(width=3, height=1)
        self.button_width = self.config.side//4
        self.button_height = self.config.side//21

        sign_uplabel = tkinter.Label(self, font=("Arial", 23), text="Sign Up", bg="grey")
        sign_uplabel.pack(pady=20)
        sign = tkinter.Label(self, font=("Arial", 23), text="------------------------", bg="grey")
        sign.pack(pady=30)

        name_label = tkinter.Label(self, font=("Arial", 15), text="New Username", bg="grey")
        name_label.pack(pady=10)

        self.name_var = tkinter.StringVar()
        namebox = tkinter.Entry(self, font=("Arial", 14, "bold"), textvariable=self.name_var)
        namebox.pack(pady=10)

        pass_label = tkinter.Label(self, font=("Arial", 15), text="New Password", bg="grey")
        pass_label.pack(pady=10)

        self.password_var = tkinter.StringVar()
        passbox = tkinter.Entry(self, font=("Arial", 14, "bold"), textvariable=self.password_var)
        passbox.pack(pady=20)


        submit_button = tkinter.Button(self, font=("Arial", 14, "bold"), image=self.button_image, height=self.button_height, width=self.button_width, compound="c", command=lambda:self.application.save_user(), text="Sign Up")
        submit_button.pack(pady=7)

        return_button = tkinter.Button(self, font=("Arial", 14, "bold"), image=self.button_image, height=self.button_height, width=self.button_width, compound="c", command=lambda:self.application.change_tologin(), text="Return")
        return_button.pack(pady=7)

