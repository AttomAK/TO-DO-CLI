import json
from datetime import datetime 

user_TODO = {}
now = datetime.now()

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
def updateTask():
    updatedStatus = input("What is the current ")

# remove task
def deleteTask():
    pass

def writeToJason():
    file_name = "tasks.json"
    with open(file_name, "w") as transfer:
        json.dump(user_TODO, transfer, indent=4)


def runALL():
    getTask()
    writeToJason()

runALL()
