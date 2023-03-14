def saveUserInfo(user_info):
    ##saves this info to the storage
    ## check if the storage exists already..
    ## the storage will be saved to the users.txt in the 'storage' folder
    ## check if users.txt file exists
    import os ## <--- What does this module do?

    if os.path.isdir("storage") and os.path.isfile("storage/users.py"):
        print("You may continue")
        commitUserData(user_info)
    else:
        if not os.path.isdir("storage"):
            print("the storage does not exist ... creating it ...")
            os.mkdir("storage")
        if not os.path.isfile("storage/users.py"):
            print("the file does not exist... creating it ...")
            f_object = open("storage/users.py", "w")
            f_object.close()
        
        commitUserData(user_info)


def getStorage():
    #f_object = open("storage/users.py", "r")
    #data = f_object.read()
    from storage import users
    try:
         data = users.users
    except:
        data = []
        
    return data



def commitUserData(user_info):
    #print("Save: " + str(user_info))

    #retrieve old data
    current_storage = getStorage()

    if len(current_storage) == 0:
        current_storage.append(user_info)
        f_object = open("storage/users.py", "a")
        f_object.write("users="+str(current_storage))
    else:
        from storage import users
        users.users.append(user_info)
        f_object = open("storage/users.py", "w")
        f_object.write("users="+str(users.users))

    print("User saved successfully!")




