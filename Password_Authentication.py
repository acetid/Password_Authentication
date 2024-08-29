import getpass

database = {"ace": "simple", "acetid": "password"}

def password_auth():
    username = input("Enter Your Username: ")
    password = getpass.getpass("Enter Your Password: ")
    if username in database:    
        # Loop until the correct password is entered
        while password != database[username]:
            print("Incorrect password. Please try again.")
            password = getpass.getpass("Enter Your Password Again: ")
        
        print("Verified")
    else:
        print("Your username or password is incorrect.")
        password_auth()

# Call the function
password_auth()
