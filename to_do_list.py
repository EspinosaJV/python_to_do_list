def viewTasks():
    print("You will now be viewing tasks!")

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
    print("You will now be editing tasks!")

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