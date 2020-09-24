import json
import os
import re

filesize = os.path.getsize("data.txt")

if filesize == 0:
    print("No users are registered with this client.")

    register = input("Do you want to register a new user (y/n)? ")
    while register not in ["y", "n", "Y", "N"]:
        print("Invalid response. Try again.")    
        register = input("Do you want to register a new user (y/n)? ")

    if register == 'y':
        name = input("Enter Full Name: ")
        
        while name.isalpha() == False:
            print("Invalid Name. Try again.")
            name = input("Enter Full Name: ")

        email = input("Enter Email Address: ")
        regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"

        while re.search(regex, email):
            print("Invalid Email. Try again.")
            email = input("Enter Email Address: ")

        password = input("Enter Password: ")
        password_copy = input("Re-enter Password: ")

        while password_copy != password:
            print("Passwords do not match. Try again.")
            password = input("Enter Password: ")
            password_copy = input("Re-enter Password: ")

        #Store user info
        data = {}
        data["users"] = []

        data["users"].append({
            "name": name,
            "email": email,
            "password": password
        })

        #Dump data into data.txt
        with open("data.txt", "w") as outfile:
            json.dump(data, outfile)
        
        #Print data.txt contents
        with open("data.txt") as json_file:
            data = json.load(json_file)
            for u in data["users"]:
                print()
                print("Name: " + u["name"])
                print("Email: " + u["email"])
                print("Password: " + u["password"])
