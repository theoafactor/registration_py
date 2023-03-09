def saveUserInfo(user_info):
    ##saves this info to the storage
    ## check if the storage exists already..
    ## the storage will be saved to the users.txt in the 'storage' folder
    ## check if users.txt file exists
    import os.path ## <--- What does this module do?

    if os.path.isdir("storage") and os.path.isfile("storage/users.py"):
        print("You may continue")
    else:
        if not os.path.isdir("storage"):
            print("the storage does not exist")
        if not os.path.isfile("storage/users.py"):
            print("the file does not exist")

