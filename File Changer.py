import os
# This input prompt the user on the file directory they wish to change and stores it as userDirectory
userDirectory = input("Please enter the file directory for the files you want to change: ")
# the directory is then found by the program and stored as selectedFiles
selectedFiles = os.listdir(userDirectory)

# The following code asks the user for the file they wish to change and the file type to change it
userSelection = input("Please select the type of file you wish to change (Example: jpg, png, etc.): ")
userChange = input("Please enter the type of filetype you wish to replace " + userSelection + " with (Example: jpg, png, etc.): ")
userConfirmation = input("Are you sure you wish to replace " + userSelection + " with " + userChange + " In " + str(selectedFiles) + " ? (yes/no) ")
if userConfirmation == 'yes':
    # The following code finds the selected file types and changes them with the new ones
    for file in selectedFiles:
        if file.lower().endswith(userSelection):
            old_path = os.path.join(userDirectory, file)
            newFile = file.lower().replace(userSelection, userChange)
            new_path = os.path.join(userDirectory, newFile)
            os.rename(old_path, new_path)
            print("File change Successful")
elif userConfirmation == 'no':
    print("File change successfully aborted.")
else:
    print("Error: please enter 'yes' or 'no'.")