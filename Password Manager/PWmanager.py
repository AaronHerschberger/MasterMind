import os
import json
from cryptography.fernet import Fernet


# Generate a key and save it to a file (run this once to create the key)
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Load the encryption key from the file
def load_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()

# Encrypt a password
def encrypt_password(password, key):
    fernet = Fernet(key)
    return fernet.encrypt(password.encode()).decode()

# Decrypt a password
def decrypt_password(encrypted_password, key):
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_password.encode()).decode()

# Save passwords to a file
def save_passwords(passwords, filename="passwords.json"):
    with open(filename, "w") as file:
        json.dump(passwords, file)

# Load passwords from a file
def load_passwords(filename="passwords.json"):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    return {}

# Main program
def main():
    key = load_key()
    passwords = load_passwords()

    while True:
        print("\nPassword Manager")
        print("1. Add a new password")
        print("2. Retrieve a password")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            account = input("Enter the account name: ")
            password = input("Enter the password: ")
            encrypted_password = encrypt_password(password, key)
            passwords[account] = encrypted_password
            save_passwords(passwords)
            print("Password saved successfully!")

        elif choice == "2":
            account = input("Enter the account name: ")
            if account in passwords:
                encrypted_password = passwords[account]
                password = decrypt_password(encrypted_password, key)
                print(f"The password for {account} is: {password}")
            else:
                print("Account not found!")

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # Uncomment the line below to generate a key (run this only once)
    # generate_key()
    main()