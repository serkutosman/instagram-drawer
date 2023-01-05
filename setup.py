from src.constants import CREDENTIALS_FILE, INSTALL_REQUIREMENTS

import os
from getpass import getpass


def credentialsExist():
    return os.path.isfile(CREDENTIALS_FILE)


def getCredentials():
    username = input("Username: ")
    password = getpass("Password: ")

    with open(CREDENTIALS_FILE, "w", encoding="utf-8") as file:
        file.write(username + "\n" + password)

    print(f"Credentials saved to {CREDENTIALS_FILE}. You can change them anytime you want.")


def installRequirements():
    print("Installing requirements...")

    try:
        os.system(INSTALL_REQUIREMENTS)
    except Exception as e:
        print("Error installing requirements. Please install them manually.\n\nERROR MESSAGE: ", end="")
        print(e)
        exit()


def main():
    if not credentialsExist():
        getCredentials()

    installRequirements()


if __name__ == "__main__":
    main()
    exit()
