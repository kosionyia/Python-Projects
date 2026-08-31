from .mod2_310 import User


class Admin(User):
    def __init__(self, first_name, last_name, gender):
        super().__init__(first_name, last_name, gender)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_priviledges(self):
        print(f"{self.privileges} are your priviledges.")
