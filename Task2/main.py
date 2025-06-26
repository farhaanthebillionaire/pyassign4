while True:
    user_text = input("\nEnter text to write to the file: ")
    file = open("./Assignments/A4/Task2/output.txt", "w")
    file.write(user_text + "\n")
    print("Data Successfully Written To The File")
    file.close()
    
    user_advn_text = input("\nEnter Additional Text To Append: ")
    file = open("./Assignments/A4/Task2/output.txt", "a")
    file.write(user_advn_text + "\n")
    print("Data Successfully Appended.")
    file.close()
    
    file = open("./Assignments/A4/Task2/output.txt","r")
    print("\nFinal Output Of File:")
    print(file.read())
    file.close()

    user_choice = input("\nDo You Want To Continue? (Y/n): ")
    if user_choice == "n":
        break
