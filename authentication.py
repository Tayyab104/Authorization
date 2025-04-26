from fastapi import FastAPI
import random

app = FastAPI()
USER_FILE = "credentials.txt"

@app.post("/signup")
def signup(username: str, password: str):
    user_object = f'{{"user": {{"credentials": {{"username": "{username}", "password": "{password}"}}}}}}\n'
    with open(USER_FILE, "a") as f:
        f.write(user_object)
    return f"User {username} created!"

@app.post("/signin")
def signin(username: str, password: str):
    with open(USER_FILE, "r") as f:
        for line in f:
            if f'"username": "{username}"' in line and f'"password": "{password}"' in line:
                token = random.randint(1000, 9999)
                return f"Welcome {username}! Token: {token}"
    return "Login failed!"