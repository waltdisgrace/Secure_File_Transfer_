import json
import os
import re
#from email_validator import validate_email, EmailNotValidError
import sys



#TODO:
#Registering:
#  User already exists
#  Passwords don't match
#Login:
#  Basic impl.
#  Password is incorrect
#  User doesn't exist
#Adding Contacts:
#  Basic impl.
#  Contact already exists
#
#TODO SECURITY:
#Password is insecure (not enough chars, etc)
#Too many attempts -> lockout
#Clean up data / encrypt data



def query_binary(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        print(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            print("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').")

def touch(fname):
    if os.path.exists(fname):
        os.utime(fname, None)
    else:
        open(fname, 'a').close()

def getEmail():
    return "Email"
#    while True:
#        try:
#            email = input("Enter Email Address: ")
#            valid = validate_email(email)
#            email = valid.email
#        except EmailNotValidError as e:
#            print(str(e))
#            continue
#        else:
#            break


def getName():
    name = input("Enter Full Name: ")
    while name.isalpha() == False:
        print("Invalid Name. Try again.")
        name = input("Enter Full Name: ")
    return name


def getPassword():
    password = input("Enter Password: ")
    password_copy = input("Re-enter Password: ")

    while password_copy != password:
        print("Passwords do not match. Try again.")
        password = input("Enter Password: ")
        password_copy = input("Re-enter Password: ")

    return password

def dumpDataToTextFile(data):
    """
    data is a dict of dict
    """
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


def storeUserInfo(name,email,password):
    """
    returns the dict of dict that constitutes the user info
    """
    data = {}
    data["users"] = []

    user_dict = {}

    user_dict["name"] = name
    user_dict["email"] = email
    user_dict["password"] = password

    data["users"].append(user_dict)
    return data

def registerNewUser():
    print("Registering New User")
    dumpDataToTextFile(storeUserInfo(getName(), getEmail(), getPassword()))
    printDataFile()

def main():
    touch("data.txt")
    if os.path.getsize("data.txt") == 0:
        print("No users are registered with this client.")
    if query_binary("Do you want to register a new user (y/n)? "):
        registerNewUser()

if __name__ == "__main__":
    sys.exit(main())
