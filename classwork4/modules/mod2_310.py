class User():
    def __init__(self, first_name, last_name, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender

    def describe_user(self):
        print(f"{self.first_name.title()} {self.last_name.title()} is a {self.gender.title()}")
