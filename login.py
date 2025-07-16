def login(id, pw):
    if id == "admin" and pw == "password123":
        return "Login successful"
    else:
        return "Login failed"
