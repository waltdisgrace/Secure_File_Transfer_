# COMP 3611 Project - Secure File Transfer

# Milestone 4 (Temporary place in README)

<img src="https://i.ibb.co/tHs7SrJ/Project-5.jpg" alt="Project-5" border="0">

Team members: David Razmadze, Grace Chin, William Stewart

## Goal: Securely transfer a file to another person's computer who is in our contact list and is on the same network (wired/wireless)

## How to run the program

### Install required packages
```
./setup.sh 
```

### Run program
```
./secure_drop
```

### User Registration (Milestone 1) and Login (Milestone 2)
```
./secure_drop 
No users are registered with this client.
Do you want to register a new user (y/n)?  [Y/n] 
y
The user registration is a one-time process. Once a user is registered on a client, the login module is activated subsequently. After a successful login, a "secure_drop>" shell is started.
Enter Full Name: David Razmadze
Enter Email Address: david@gmail.com
Password: 
Re-enter Password: 
Do you want to log in (y/n)?  [Y/n] 
y
Enter Email Address: david@gmail.com
Password: 
Passwords Match.
Logging In.
secure_drop> 
```

### Help

```
secure_drop> help
  "add"  -> Add a new contact
  "list" -> List all online contacts
  "send" -> Transfer file to contact
  "exit" -> Exit SecureDrop
```

### Adding Contacts (Milestone 3) and Listing Contacts
```
secure_drop> add 
Enter Full Name: Grace Chin
Enter Email Address: grace@gmail.com
  Contact Added.
secure_drop> list
  Listing!
[{'Grace Chin': {'name': 'Grace Chin', 'email': 'grace@gmail.com'}}]
secure_drop>
```

### Optional: Cleanup program files

```
./cleanup.sh 
```

---

## Summary of Security Features Implemented

1. Password Requirements: Passwords must adhere to a password policy that ensures a certain length and level of complexity.
2. Salted Hashes: Passwords are hashed and salted; only the password hashes are stored in memory, not the actual passwords.
3. Hidden Characters when Typing Passwords: When users type their passwords via stdin, no characters visibly appear on the screen.
4. File Permissions: Files that contain confidential information are set to have the strictest possible permissions such that the program can still read and write to those files.
5. Encryption: The contacts file is symmetrically encrypted using AES; it is decrypted using a key that is derived from the user's password hash.

---

## Sections of Code 

1. Shell commands 

```
secureDropShell()
psh_cd(path)
psh_help()
psh_add()
psh_list()
psh_send()
execute_command(command)
```

2. Credentials

```
getEmail()
getName()
```

3. Password

```
setPassword()
getPassword()
getHashedPassword(password)
passwordMeetsRequirements(password)
checkPassword(password, hashed_password)
```

4. Logging In

```
logIn()
storeUserInfo(name, email, password)
```

5. Database

```
storeData(name, email, filename)
loadData(filename)
registerNewUser()
dumpUserToTextFile(data, file_name)
dumpRegisterToTextFile(data, file_name)
printDataFile()
```

6. Helper Functions

```
query_binary(question, default="yes")
touch(fname)
```

7. Encryption

```
aesEncryptFile(file_name, key)
aesDecryptFile(file_name, key)
```


8. MAIN

```
main()
```
