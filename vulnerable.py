import os

def run_command():
    user_input = input("Enter command: ")
    os.system(user_input)  # 🚨 Vulnerability: Command injection

if __name__ == "__main__":
    run_command()
