import glob # module for looking for files matching a pattern

# function that handles display of .txt files
def viewTasks():
    print("\n******************************")
    print("You will now be viewing tasks!\n")

    # acquires all .txt files in project repository
    taskFiles = glob.glob('**/*.txt', recursive=True)

    # displays all .txt files to console
    for index,task in enumerate(taskFiles):
        if index == (len(taskFiles)-1):
            print(f"{index+1}. {task}\n")
            break
        print(f"{index+1}. {task}")

    print("Which task would you like to specifically view? (Input the number)")
    try:
        userChoice = int(input())
        taskChoice = taskFiles[userChoice - 1]
        with open(taskChoice, 'r') as file:
            contents = file.read()
            print(contents)
            print("---------------------------------------")
            userChoice = input("Press any key to continue.")
        main()
    except:
        print("Please input appropriately.")
        main()

# function that handles creation of .txt files
def addTasks():
    # addTasks function local variables
    taskList = []

    print("You will now be adding tasks!")

    # creation of .txt file
    print("What specific date would this task be on? (Month-Day-Year)")
    taskDate = input()
    fileName = (f"{taskDate}.txt")
    taskFile = open(fileName, "w")

    # creation of .txt file contents
    print("How many tasks will this day be having?")
    # user input validator
    try:
        numberOfTasks = int(input())
    except ValueError:
        print("Please ensure that your input is appropriate.")
        addTasks()
    for i in range(0, numberOfTasks):
        print(f"Input task #{i+1}:")
        taskList.append(f"{i+1}. {input()}")
    with open(fileName, 'w') as file:
        for task in taskList:
            file.write(f"{task}\n")

    print(".txt file for this specific day has been created!")

    # back to main function
    main()

def editTasks():
    print("\n******************************")
    print("You will now be editing tasks!")

    # acquires all .txt files in project repo
    taskFiles = glob.glob('**/*.txt', recursive=True)

    # displays list of .txt files to console
    for index, task in enumerate(taskFiles):
        if index == (len(taskFiles)-1):
            print(f"{index+1}. {task}\n")
            break
        print(f"{index+1}. {task}")

    # displays contents of chosen text file before continuing
    print("Which task would you like to specifically edit? (Input the number)")
    try:
        userChoice = int(input())
        taskChoice = taskFiles[userChoice - 1]
        with open(taskChoice, 'r') as file:
            contents = file.read()
            print(contents)
            print("---------------------------------")
    except:
        print("Please input appropriately.")
        main()

    try:
        print("Would you like to 1. Add to the content or 2. Edit a specific line? (Input the number)")
        userChoice = int(input())
        if userChoice == 1:
            print("You have chosen to append to the file.")
            with open(taskChoice, "a+") as file:
                file.seek(0)
                lines = file.readlines()
                lineCount = len(lines)
                print(lineCount)
                print("Please input the individual task that you would like to add.")
                userInput = input()
                file.write(f"{lineCount + 1}. {userInput}\n")
            main()
        elif userChoice == 2:
            print("You have chosen to edit the contents of the file.")
            print("Please input the number of the specific task you wish to edit.")
            chosenTask = int(input())
            with open(taskChoice, "r") as file:
                tasks = file.readlines()
                taskCount = len(tasks)
                if chosenTask > taskCount:
                    print("Please input an appropriate value.")
                    main()
            print("Please input the new task to place in-line with the chosen number.")
            taskInput = input()
            tasks[chosenTask - 1] = f"{chosenTask}. {taskInput}\n"
            with open(taskChoice, "w") as file:
                file.writelines(tasks)
            main()
        else:
            print("Please input appropriately.")
            main()
    except:
        main()

def deleteTasks():
    print("You will now be deleting tasks!")

def main():
    print("Welcome to the To-Do-List Python Application.")
    print("What would you like to do?")
    print("1. View Tasks to accomplish")
    print("2. Add Tasks to accomplish")
    print("3. Edit existing Tasks")
    print("4. Delete existing Tasks")

    # user choice validator
    try:
        userChoice = int(input())

        match userChoice:
            case 1:
                viewTasks()
            case 2:
                addTasks()
            case 3:
                editTasks()
            case 4:
                deleteTasks()
            case _:
                print("Only choose from the given options.")

    except ValueError:
        print("Please ensure that your input is appropriate.")

if __name__ == "__main__":
    main()