import json
from datetime import date 

newDoc = False
task = {}

while True :

    with open("todoDB.json","r") as f:
        #reading the todoDB.json
        todoData = json.load(f)

        keys = list(todoData.keys())
        currentDate = date.today()

     #checking whether the user is a new user or not
        if len(todoData) == 0:
            emptyDoc = True
            username = input(
                "\nHi! welcome to TodoCLI, Please enter your name."
            )
            todoData["name"] = username
            todoData["date"] = str(currentDate)
            print("\nHey {username}! I hope you had a good start of the day, let's plan your day togrther\nYou can create your first task by typing task or add task") 

            cmd = input(">>")

            todoData["today"] = []
            if cmd == "create task" or cmd == "add task":
                print("\nPlease provide datails about your task as per cli instructions")  
                print("\nAdd time in military formant i.e. if it's 9AM write 0900 or ti's 9PM write 2100")
                #take the task description as input
                task_description = input("please enter your task description: ")
                scheduled_time = input("please enter the schedule time: ")

                task = {
                    "description": task_description,
                    "scheduled_time": scheduled_time
                }
                todoData["today"].append(task)
                with open("todoDB.json","w") as f:
                    json.dump(todoData, f, indent=4)
            elif cmd == "break" or cmd == "close":
                   break