with open("pass.txt", "r") as f:
    read = f.read()
    password = input("Enter the password inorder to access the data: ")
if(password in read):
    print("Your password was correct the file data is here: ")
    with open("en_file.txt", "r") as f:
        print(f.read())
else:
    print("The entered password is incorrect")
    print("Do you wish to change the password")
    check = int(input("Enter 1 if you wish to change the password or else press 0: "))
    if(check == 1):
        with open("pass.txt", "w") as f:
            new_pass = input("Enter the new password: ")
            f.write(new_pass)
    elif(check == 0):
        print("Try again later!")
    else:
        print("Please enter a valid choice")
print("End of program")