# filename: login.py

def login(username, password):
    # 🚨 VULNERABILITY: hardcoded credentials
    if username == "admin" and password == "1234":
        print("Login successful")
    else:
        print("Invalid credentials") 

if __name__ == "__main__":
    user = input("Username: ")
    pwd = input("Password: ")
    login(user, pwd)
