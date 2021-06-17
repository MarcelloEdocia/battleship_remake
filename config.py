import json

class Config:

    def __init__(self):
        #Game config
        self.game_title = "Battleship"

        #Board settings
        self.row = 5
        self.column = 5

        #Login page settings
        self.login_page_height = 500
        self.login_page_width = 500
        self.login_page_screen = "500x500+550+170"


        #Game Window settings
        base = 100
        ratio = 5
        self.side = base*ratio
        self.screen = f"{self.side}x{self.side}+550+170"

        #Image path
        self.logo_path = "./image/battleship.png"
        self.first_image = "./image/1.png"
        self.second_image = "./image/2.png"
        self.third_image = "./image/3.png"

        #Login authorization
        self.users_path = "./data/users.json"

    def load_data(self, path):
        with open(path, "r") as json_data:
            data = json.load(json_data)
        return data

    def login(self, username, password):
        users = self.load_data(self.users_path)
        if username in users:
            if password == users[username]["password"]:
                return True
        else:
            return False

