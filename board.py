import tkinter
from PIL import Image, ImageTk


class Board(tkinter.Frame):

    def __init__(self, parent, Game):

        self.game = Game
        self.config = Game.config

        # Config frame
        super().__init__(parent)
        self.configure(bg="black")
        self.grid(row=0, column=0, sticky="nsew")
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)

        self.create_mainframe()
        self.create_board()
        self.show_board()
        self.create_buttons()
        self.show_buttons()

    def create_mainframe(self):
        self.mainframe = tkinter.Frame(self, height=self.config.side, width=self.config.side, bg="black")
        self.mainframe.pack(expand=True)

    def create_board(self):
        self.frame_rows = []  # row

        color = 756867
        n_row, n_column = self.config.row, self.config.column
        row_height, row_width = self.config.side // n_row, self.config.side

        for i in range(n_row):
            row_color = f"#{color}"
            frame = tkinter.Frame(self.mainframe, height=row_height, width=row_width, bg=row_color)
            self.frame_rows.append(frame)
            color += 500

    def show_board(self):
        for every_frame in self.frame_rows:
            every_frame.pack()

    def put_image(self, original_image):
        image = Image.open(original_image)
        return ImageTk.PhotoImage(image)

    def change_button_image(self, pos_x, pos_y, win):
        if not win:
            self.buttons_board[pos_x][pos_y].configure(image=self.btn2_image)
        else:
            self.buttons_board[pos_x][pos_y].configure(image=self.btn3_image)

    def create_buttons(self):
        self.buttons_board = []
        n_row, n_column = self.config.row, self.config.column
        btn_height = self.config.side // n_row - 5
        btn_width = self.config.side // n_column - 5
        # self.buttonPixel = tkinter.PhotoImage(width=1, height=1)

        # image
        self.btn1_image = self.put_image(self.config.first_image)
        self.btn2_image = self.put_image(self.config.second_image)
        self.btn3_image = self.put_image(self.config.third_image)

        for i in range(n_row):
            row = []
            for j in range(n_column):
                buttonx = tkinter.Button(self.frame_rows[i], image=self.btn1_image, height=btn_height, width=btn_width,
                                         command=lambda x=i, y=j: self.game.button_pressed(x,
                                                                                           y))  # , text="O", compound="c", font=("Arial", 36, "bold")
                buttonx.pack(side="left", expand=True)
                row.append(buttonx)
            self.buttons_board.append(row)

    def show_buttons(self):
        n_row, n_column = self.config.row, self.config.column
        for i in range(n_row):
            for j in range(n_column):
                self.buttons_board[i][j].pack(side="left")



