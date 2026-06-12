def login_system():
    users = {
        "admin": "password123",
        "user": "userpass",
    }

    print("欢迎使用登录系统")
    username = input("用户名: ")
    password = input("密码: ")

    if username in users and users[username] == password:
        print("登录成功！欢迎，{}。".format(username))
    else:
        print("登录失败，用户名或密码错误。")


if __name__ == "__main__":
    login_system()
