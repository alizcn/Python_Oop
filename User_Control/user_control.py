import json
import os


class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email


class UserRepository:
    def __init__(self):
        self.users = []
        self.isLogged = False
        self.currentuser = {}
        self.loadUsers()

    def loadUsers(self):
        if os.path.exists('users.json'):
            with open('users.json', 'r', encoding='utf-8') as file:
                users = json.load(file)
                for user in users:
                    user = json.loads(user)
                    newUser = User(user['username'], user['password'], user['email'])
                    self.users.append(newUser)
                print(self.users)

    def register(self, user: User):
        self.users.append(user)
        self.savetoFile()
        print("Kullanıcı oluşturuldu")

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLogged = True
                self.currentuser = user
                print("Login yapıldı")
                break

    def logout(self):
        self.isLogged = False
        self.currentuser = {}
        print("Çıkış yapıldı")

    def identity(self):
        if self.isLogged:
            print(f"username : {self.currentuser.username}")
        else:
            print("giriş yapılmadı")

    def savetoFile(self):
        list = []
        for user in self.users:
            list.append(json.dumps(user.__dict__))
        with open('users.json', 'w') as file:
            json.dump(list, file)


repository = UserRepository()

while True:
    print("Menü".center(50, '*'))
    secim = input("""
    1- Register
    2- Login
    3- Logout
    4- İdentity
    5- Exit
    Seçiminiz : """)

    if secim == "5":
        break
    else:
        if secim == "1":
            username = input("username : ")
            password = input("password : ")
            email = input("email : ")
            user = User(username, password, email)
            repository.register(user)

        elif secim == "2":
            if repository.isLogged:
                print("Giriş yapılmış!!")
            else:
                username = input("username : ")
                password = input("password : ")
                repository.login(username, password)
        elif secim == "3":
            repository.logout()
        elif secim == "4":
            repository.identity()
        else:
            print("Yanlış Seçim !!")
