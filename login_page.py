import tkinter
from PIL import Image, ImageTk


class LoginPage(tkinter.Frame):

    def __init__(self, parent, App):
        self.application = App
        self.config = App.config
        super().__init__(parent)
        self.configure(bg="grey")

        self.grid(row=0, column=0, sticky="nsew")
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)

        self.mainFrame = tkinter.Frame(self, height=self.config.side, width=self.config.side, bg="grey")
        self.mainFrame.pack(expand=True)

        image = Image.open(self.config.logo_path)
        image_w, image_h = image.size
        ratio = image_w/self.config.side

        image = image.resize((int(image_w//ratio//2), int(image_h//ratio//2)))

        #Putting logo on the screen
        self.logo = ImageTk.PhotoImage(image)
        self.label_logo = tkinter.Label(self.mainFrame, image=self.logo)
        self.label_logo.pack()

        self.button_image = tkinter.PhotoImage(width=3, height=1)
        self.button_width = self.config.side//4
        self.button_height = self.config.side//21

        self.label_username = tkinter.Label(self.mainFrame, text="Username", bg="grey", fg="black", font=("Arial", 14, "bold"))
        self.label_username.pack(pady=5)

        self.var_username = tkinter.StringVar()
        self.username_box = tkinter.Entry(self.mainFrame,font=("Arial", 14, "bold"), textvariable=self.var_username)
        self.username_box.pack()

        self.label_password = tkinter.Label(self.mainFrame, text="Password", font=("Arial", 14, "bold"), bg="grey")
        self.label_password.pack(pady=5)

        self.var_password = tkinter.StringVar()
        self.password_box = tkinter.Entry(self.mainFrame,font=("Arial", 14, "bold"), show="*", textvariable=self.var_password)
        self.password_box.pack(pady=5)

        self.login_button = tkinter.Button(self.mainFrame, text="Login", font=("Algerian", 14), image=self.button_image,compound="c", height=self.button_height,fg="black", width=self.button_width, command=lambda:self.application.check_login())
        self.login_button.pack(pady=5)

        self.signup_button = tkinter.Button(self.mainFrame, text="Sign up", font=("Algerian", 14), image=self.button_image,compound="c", height=self.button_height, width=self.button_width,command=lambda:self.application.sign_up())

        self.signup_button.pack(pady=5)
