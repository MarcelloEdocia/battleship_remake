import tkinter
import time
import sys

from config import Config
from board import Board
from login_page import LoginPage
from signup import SignUpPage
from player import Player
from ship import Ship
from menu import MenuPage
from guide import GuidePage
from highscore import HighScorePage
from endpage import EndPage
from json import load, dump


class Window(tkinter.Tk):

    def __init__(self, App):
        self.game = App
        self.config = App.config

        super().__init__()
        self.title(self.config.game_title)
        self.geometry(self.config.login_page_screen)
        self.resizable(False, False)
        self.create_container()


        self.pages = {}

        self.users = self.load_user()
        self.new_score = self.load_score()

        self.create_endpage()
        self.create_board()
        self.create_guidepage()
        self.create_highscore()
        self.create_menupage()
        self.create_signuppage()
        self.create_loginpage()

    def create_userwarning(self):
        self.buttonVirtual = tkinter.PhotoImage(width=3, height=1)
        button_width = self.config.side // 5
        button_height = self.config.side // 21
        userwarning = tkinter.Toplevel(self)
        userwarning.title("Warning")
        userwarning.geometry("250x190+700+300")
        userwarning.config(bg="white")
        used_warning = tkinter.Label(userwarning, text="This Username has already been used",
                                     font=("Arial", 10, "bold"), bg="white")
        used_warning.pack(expand=True, pady=10)
        used_warning_button = tkinter.Button(userwarning, text="Return", font=("Arial", 17),
                                             image=self.buttonVirtual, compound="c", height=button_height,
                                             width=button_width, command=userwarning.destroy)
        used_warning_button.pack(expand=True, pady=10)

    def load_score(self):
        with open("./data/score.json", "r") as file:
            new_score = load(file)
            return new_score

    def load_user(self):
        with open("./data/users.json", "r") as file:
            users = load(file)
            return users

    def save_user(self):
        new_username = self.pages["SignUpPage"].name_var.get()
        new_password = self.pages["SignUpPage"].password_var.get()
        if new_username in self.users:
            self.create_userwarning()
        else:
            self.users[new_username] = {
                "password": new_password,
                "level": "level"
            }
            with open("./data/users.json", "w") as file:
                dump(self.users, file)
            self.new_score.append({new_username: {"nick": new_username, "user_score": "0", "win_rate": "0"}})
            with open("./data/score.json", "w") as file:
                dump(self.new_score, file)
            self.create_highscore()
            self.change_page("loginPage")
            # print(len(self.new_score))

    def create_container(self):
        self.container = tkinter.Frame(self, bg="grey")
        self.container.pack(fill="both", expand=True)

    def create_board(self):
        self.pages["Board"] = Board(self.container, self.game)

    def create_loginpage(self):
        self.pages["loginPage"] = LoginPage(self.container, self)

    def create_signuppage(self):
        self.pages["SignUpPage"] = SignUpPage(self.container, self)


    def create_menupage(self):
        self.pages["MenuPage"] = MenuPage(self.container, self)

    def create_guidepage(self):
        self.pages["GuidePage"] = GuidePage(self.container, self)

    def create_highscore(self):
        self.pages["HighScore"] = HighScorePage(self.container,self)

    def create_endpage(self):
        self.pages["EndPage"] = EndPage(self.container, self)

    def yes_button(self):
        time.sleep(1)
        sys.exit()

    def change_tologin(self):
        self.change_page("loginPage")

    def create_popup(self):
        self.pixelVirtual = tkinter.PhotoImage(width=2, height=1)
        self.button_width = 80
        self.button_height = 30

        pop = tkinter.Toplevel(self)
        pop.title("Warning")
        pop.geometry("250x150+700+300")
        pop.config(bg="white")
        #Text warning
        pop_warning = tkinter.Label(pop, text="Are you sure to exit?", font=("Arial", 14), bg="white")
        pop_warning.pack(pady=10)
        #Warning button
        pop_frame = tkinter.Frame(pop, bg="white")
        pop_frame.pack(pady=5)
        button1 = tkinter.Button(pop_frame, text="Yes", image=self.pixelVirtual, width=self.button_width, height=self.button_height, compound="c", command=self.yes_button)
        button1.pack(side="left", pady=10, padx=10)
        button2 = tkinter.Button(pop_frame,text="No", image=self.pixelVirtual, width=self.button_width, height=self.button_height, compound="c", command=pop.destroy)
        button2.pack(side="right", pady=10, padx=10)


    def change_page(self, page):
        new_page = self.pages[page]
        new_page.tkraise()

    def create_falselogin(self):
        self.pixelVirtual = tkinter.PhotoImage(width=2, height=1)
        self.button_width = 80
        self.button_height = 30
        pop = tkinter.Toplevel(self)
        pop.title("Warning")
        pop.geometry("250x150+700+300")
        pop.config(bg="white")
        # Text warning
        pop_warning = tkinter.Label(pop, text="Wrong username or password", font=("Arial", 12), bg="white")
        pop_warning.pack(pady=10)
        # Warning button
        pop_frame = tkinter.Frame(pop, bg="white")
        pop_frame.pack(pady=5)
        button1 = tkinter.Button(pop_frame, text="Okay", image=self.pixelVirtual, width=self.button_width,
                                 height=self.button_height, compound="c", command=pop.destroy)
        button1.pack(pady=15)


    def check_login(self):
        username = self.pages["loginPage"].var_username.get()
        password = self.pages["loginPage"].var_password.get()

        granted = self.config.login(username, password)
        if granted:
            self.change_page("MenuPage")
        else:
            self.create_falselogin()


    def sign_up(self):
        self.change_page("SignUpPage")

    def open_guide(self):
        self.change_page("GuidePage")

    def open_highscore(self):
        self.change_page("HighScore")

    def open_game(self):
        self.change_page("Board")

    def gotomenu(self):
        self.change_page("MenuPage")

    def play_again(self):
        time.sleep(1)
        self.create_board()
        self.change_page("Board")


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#---------------------------------------------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________________________________________


class App:

    def __init__(self):
            self.config = Config()
            self.window = Window(self)
            self.ship = Ship(self)
            self.player = Player()
            self.highscores = self.load_score()
            self.index = 0
            self.step = 0

    def load_score(self):
        with open("./data/score.json", "r") as file:
            new_score = load(file)
            return new_score

    def update_score(self):
        self.highscores = self.load_score()
        username = self.window.pages["loginPage"].var_username.get()
        if username in self.highscores[self.index]:
            if username == self.highscores[self.index][username]["nick"]:
                score = int(self.highscores[self.index][username]["user_score"])
                score += 1
                score = str(score)
                self.highscores[self.index][username]["user_score"] = score
                with open("./data/score.json", "w") as file:
                    dump(self.highscores, file)
                self.window.create_highscore()
        else:
            # print(self.index)
            self.index += 1
            self.update_score()

    def update_winrate(self):
        win_rate = self.load_score()
        username = self.window.pages["loginPage"].var_username.get()
        if username in self.highscores[self.index]:
            if username == self.highscores[self.index][username]["nick"]:
                if self.highscores[self.index][username]["win_rate"] == "0":
                    new_winrate = ((25 - self.step) / 25) * 100
                    win_rate = new_winrate
                    win_rate = str(win_rate)
                    self.highscores[self.index][username]["win_rate"] = win_rate
                    with open("./data/score.json", "w") as file:
                        dump(self.highscores, file)
                    self.window.create_highscore()
                else:
                    win_rate = int(float(self.highscores[self.index][username]["win_rate"]))
                    new_winrate = ((25 - self.step) / 25) * 100
                    win_rate = (win_rate + new_winrate) // 2
                    win_rate = str(win_rate)
                    self.highscores[self.index][username]["win_rate"] = win_rate
                    with open("./data/score.json", "w") as file:
                        dump(self.highscores, file)
                    self.window.create_highscore()
        else:
            self.index += 1
            self.update_winrate()


    def check_location(self):
        if self.ship.location == self.player.location:
            return True
        else:
            return False


    def button_pressed(self, pos_x, pos_y):
        #print(pos_x + 1, pos_y + 1)
        self.player.current_location(pos_x, pos_y)
        # +1 because index starts with zero
        win = self.check_location()
        self.window.pages["Board"].change_button_image(pos_x, pos_y, win)
        self.step += 1
        if win:
            self.index = 0
            self.ship.setup_location()
            self.update_score()
            self.update_winrate()
            self.step = 0
            self.window.create_board()
            time.sleep(1)
            self.window.change_page("EndPage")


    def run(self):
        #For testing only
        #print(self.ship.location[0]+1, self.ship.location[1]+1)
        self.window.mainloop()


def main():
    my_app = App()
    my_app.run()


if __name__ == "__main__":
    main()


