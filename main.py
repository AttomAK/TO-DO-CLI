import json
from datetime import datetime 

user_TODO = {}
now = datetime.now()
read_TODO = {}



# get task info
def getTask():

    numTasks = int(input("How many tasks do you have today: "))

    for num in range(numTasks):
        task = input("What do you have on your TO-DO list: ")
        status = input("What is the status on this TO-DO: ")
        user_TODO.update({task: status})
        print(user_TODO)
        print(f"Date Made: {now.strftime("%I:%H:%M:%p")}")




# update the status in progress, done or not done
def updateStatus(numTasks):

    with open("tasks.json", "r") as file:
        data = json.load("tasks.json")
        print(data)
    
    updateTask = int(input("What task would you like to update ?: "))

    if updateTask in range(numTasks):
        newStatus = input("What is the new status of this task: ")
        numTasks[updateTask] = []

        
        

        

# remove task
def deleteTask():
    pass

    


def showTODO():
    userOption = input("Do you want to show your current to-do list Y/N: ")
    if userOption == "y":
        with open("tasks.json") as read:
            loadFile = json.load(read)
            print(loadFile)
    else:
        return None

def writeToJason():
    file_name = "tasks.json"
    with open(file_name, "w") as transfer:
        json.dump(user_TODO, transfer, indent=4)


def runALL():
    getTask()
    writeToJason()
    showTODO()

runALL()
