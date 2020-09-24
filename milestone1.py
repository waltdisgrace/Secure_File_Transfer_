import json
import os
import re
from email_validator import validate_email, EmailNotValidError

filesize = os.path.getsize("data.txt")


def registerNewUser():
    register = input("Do you want to register a new user (y/n)? ")
    while register not in ["y", "n", "Y", "N"]:
        print("Invalid response. Try again.")
        register = input("Do you want to register a new user (y/n)? ")


def getEmail():
    while True:
        try:
            email = input("Enter Email Address: ")
            valid = validate_email(email)
            email = valid.email
        except EmailNotValidError as e:
            print(str(e))
            continue
        else:
            break


def getFullName():
    name = input("Enter Full Name: ")
    while name.isalpha() == False:
        print("Invalid Name. Try again.")
        name = input("Enter Full Name: ")


def getPassword():
    password = input("Enter Password: ")
    password_copy = input("Re-enter Password: ")

    while password_copy != password:
        print("Passwords do not match. Try again.")
        password = input("Enter Password: ")
        password_copy = input("Re-enter Password: ")


def storeUserInfo():
    data = {}
    data["users"] = []

    data["users"].append({
        "name": name,
        "email": email,
        "password": password
    })


def dumpDataToTextFile():
    with open("data.txt", "w") as outfile:
        json.dump(data, outfile)


def printDataFile():
    with open("data.txt") as json_file:
        data = json.load(json_file)
        for u in data["users"]:
            print()
            print("Name: " + u["name"])
            print("Email: " + u["email"])
            print("Password: " + u["password"])


# Main

if filesize == 0:
    print("No users are registered with this client.")

    registerNewUser()

    if register == 'y':
        getFullName()
        getEmail()
        getPassword()

        storeUserInfo()
        dumpDataToTextFile()

        printDataFile()
