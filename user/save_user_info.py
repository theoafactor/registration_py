def saveUserInfo(user_info):
    ##saves this info to the storage
    ## check if the storage exists already..
    ## the storage will be saved to the users.txt in the 'storage' folder
    ## check if users.txt file exists
    import os ## <--- What does this module do?

    if os.path.isdir("storage") and os.path.isfile("storage/users.py"):
        #print("You may continue")
        feedback = commitUserData(user_info)
        return feedback
    else:
        if not os.path.isdir("storage"):
            print("the storage folder does not exist ... creating it ...")
            os.mkdir("storage")
        if not os.path.isfile("storage/users.py"):
            print("the file: user.py does not exist... creating it ...")
            f_object = open("storage/users.py", "w")
            f_object.close()
        
        feedback = commitUserData(user_info)
        return feedback


def getStorage():
    #f_object = open("storage/users.py", "r")
    #data = f_object.read()
    from storage import users
    try:
         data = users.users
    except:
        data = []
        
    return data


## This function commits(saves) the user data to file
def commitUserData(user_info):
    #print("Save: " + str(user_info))

    #retrieve old data
    current_storage = getStorage()

    if len(current_storage) == 0:
        # this is the first data to be added
        current_storage.append(user_info)
        f_object = open("storage/users.py", "a")
        f_object.write("users="+str(current_storage))

        print("User saved successfully!")

        return "saved"
    else:
        # this is not the first data to be added
        from storage import users

        # check if the user exists already
        result = checkIfUserExists(user_info["email"])

        if result == True:
            return "duplicate-error"
        else:
            users.users.append(user_info)
            f_object = open("storage/users.py", "w")
            f_object.write("users="+str(users.users))
            print("User saved successfully!")
            
            return "saved"


def checkIfUserExists(email):
    # retrieve the current users from storage
    current_storage = getStorage()

    if len(current_storage) == 0:
        # current storage is empty
        return False
    else:
        # current storage is not empty
        for user in current_storage:
            if user["email"] == email:
                # the user exists
                return True
        else:
            return False





