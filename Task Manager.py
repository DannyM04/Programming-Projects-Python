# Line 2 creates a list that will be used in the taskAdd function to store all the tasks
userTasks = []

# the taskAdd function asks for the user's task name and if it has a deadline. It will then store the relevant information and then prompt the user if there is another task needed.
def taskAdd():
        while True:

            taskName = input("Please enter the task's name: ")
            userDirectoryResponse = input("is there a deadline to this task? (yes/no): ")
            
            if userDirectoryResponse.lower() == 'yes':
                taskDeadline = input("Please enter the task's deadline date (DD/MM/YYYY): ")
                userSubmittedTasks = {'task': taskName, 'deadline': taskDeadline}
            
            else:
                userSubmittedTasks = {'task': taskName}
        
            userTasks.append(userSubmittedTasks)
            
            extraTasks = input("Do you have another task to add? (yes/no): ")
            
            if extraTasks.lower() == 'yes':
                 taskAdd()
            
            if extraTasks.lower() == 'no':
                 break

            return

# viewTask displays the current tasks along with their deadlines in a set format.
def viewTask():
     print("Current Tasks: ")
     for idx, task in enumerate(userTasks, start=1):
          print(f"{idx}. Task: {task['task']}, Deadline: {task.get('deadline', 'No deadline')}")

# deleteTask asks the user whether they want to remove the task name or deadline and then finds and removes the matching task. 
def deleteTask():
     while True:
          taskNameDeletion = input("Please enter the task's name you wish to delete: ")
          found = False
          for task in userTasks:
               if task.get('task') == taskNameDeletion:
                    userConfirmation = input(print("Are you sure you want to delete the selected task? (yes/no) "))
                    if userConfirmation.lower() == 'yes':
                         userTasks.remove(task)
                         found = True
                         print("Task deleted successfully")
                    if userConfirmation.lower() == 'no':
                         print("Deletion cancelled")
                         break
          
          if not found:
               print("Error: Task not found")
          
          anotherDeletion = input("Do you wante to delete another task (yes/no): ")
          if anotherDeletion.lower() == 'no':
               break

# modifyTask asks the user whether they want to change the deadline or the name of a task. 
def modifyTask():
     while True:
          modificationSelection = input("Would you like to change a task's name or a task's deadline? (name/deadline) ")
          
          tasknameModification = None

          if modificationSelection == 'name':
               tasknameModification = input("Please enter the name of the task you wish to change: ")
          found = False
          for task in userTasks:
               if task.get('task') == tasknameModification:
                    userChange = input("Please enter the task's new name ")
                    task['task'] = userChange
                    found = True
                    print("Task name successfully updated")
          
               elif modificationSelection == 'deadline':
                    tasknameModification = input("Please enter the name of the task you wish to change the deadline for: ")
                    found = False
                    for task in userTasks:
                         if task.get('task') == tasknameModification:
                              userChange = input("Please enter the task's new deadline (DD/MM/YYYY): ")
                              task['deadline'] = userChange
                              found = True
                              print("Task deadline updated successfully")
                              break     
                  
          if not found:
               print("Error: Task not found")

          anotherModification = input("Do you want to modify another task? (yes/no): ")
          if anotherModification.lower() == 'no':
               break
          


# the Directory acts as the UI for the Task Manager. It allows the user to operate the task manager and return to the directory after using the functions. 
def Directory():
     while True:

        userDirectory = int(input("Please enter the following numbers to navigate the program: 1. Create Task, 2. View Tasks, 3. Delete Tasks, 4. Modify Tasks "))
        if userDirectory == 1:
             taskAdd()
        elif userDirectory == 2:
             viewTask()
        elif userDirectory == 3:
             deleteTask()
        elif userDirectory == 4:
             modifyTask()
        else:
             print("Error: Please enter a valid number")
             continue
        
        directoryReturn = input("Do you want to go back to the directory? (yes/no): ")
        if directoryReturn.lower() == 'no':
                 print("Thank you for using the Task Manager!")
                 break
        if directoryReturn.lower() == 'yes':
             Directory()

# line 121 runs the Directory that connects all the functions previously established.
Directory()

