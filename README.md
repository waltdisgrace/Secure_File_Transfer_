# COMP 3611 Project - Secure File Transfer

Team members: David Razmadze, Grace Chin, William Stewart

## Goal: Securely transfer a file to another person's computer who is in our contact list and is on the same network (wired/wirelss)

## Install requirements

```
./setup.sh 
```

## Cleanup program files

```
./cleanup.sh 
```

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
AES_KEY_SIZE
symm_key

aesEncryptFile(file_name, key)
aesDecryptFile(file_name, key)


```


8. MAIN
