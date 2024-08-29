# Password_Authentication

# Password Authentication Script

This is a simple Python script for password authentication, designed to validate user credentials against a predefined database. The script prompts the user to enter their username and password, and it checks these against a dictionary of stored credentials.

## How It Works

1. The script prompts the user to enter their username.
2. If the username exists in the database, the user is prompted to enter their password.
3. The script will continue to prompt the user for the correct password until it matches the stored password.
4. If the username does not exist in the database, the script informs the user that the credentials are incorrect and allows the user to try again.

## Usage

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/your-repository-name.git
    cd your-repository-name
    ```

2. **Run the Script**:
    ```bash
    python3 password_auth.py
    ```

3. **Input Credentials**:
    - Enter a valid username from the database (e.g., "ace" or "acetid").
    - Enter the corresponding password (e.g., "simple" or "password").

4. **Verification**:
    - If the credentials are correct, the script will print "Verified."
    - If the password is incorrect, the script will prompt for the password again.
    - If the username does not exist, the script will inform the user and restart the authentication process.
