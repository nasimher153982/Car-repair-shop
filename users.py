import json
import os

USERS_FILE = 'data/users.json'

def load_users():
    if not os.path.exists(USERS_FILE):
        return []
    with open(USERS_FILE, 'r') as file:
        return json.load(file)

def save_users(users):
    os.makedirs(os.path.dirname(USERS_FILE), exist_ok=True)
    with open(USERS_FILE, 'w') as file:
        json.dump(users, file, indent=2)

def authenticate():
    users = load_users()
    while True:
        print("\n1. Login")
        print("2. Register")
        choice = input("Your choice: ").strip()

        if choice == '1':
            username = input("Username: ").strip()
            password = input("Password: ").strip()
            for user in users:
                if user['username'] == username and user['password'] == password:
                    print(f"\n Welcome, {username}!\n")
                    return user['role']
            print("Incorrect username or password!")

        elif choice == '2':
            username = input("New username: ").strip()
            password = input("Password: ").strip()
            role = input("User role (admin/user): ").strip().lower()
            if role not in ['admin', 'user']:
                print("Invalid role! Please enter 'admin' or 'user'.")
                continue
            users.append({'username': username, 'password': password, 'role': role})
            save_users(users)
            print("Registration successful!")
            return role
        else:
            print("Invalid input. Please enter 1 or 2.")
