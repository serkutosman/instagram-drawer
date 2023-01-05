from src.constants import CREDENTIALS_FILE, INSTALL_REQUIREMENTS_UNIX, INSTALL_REQUIREMENTS_WIN

import os
from sys import platform
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
        if platform == "win32":
            os.system(INSTALL_REQUIREMENTS_WIN)
        else:
            os.system(INSTALL_REQUIREMENTS_UNIX)
    except Exception as e:
        print("Error installing requirements. Please check whether you have pip.\n\nERROR MESSAGE: ", end="")
        print(e)
        exit()


def main():
    installRequirements()

    if not credentialsExist():
        getCredentials()


if __name__ == "__main__":
    main()
    exit()
