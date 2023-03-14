## import the user modle
from user import info_collector, save_user_info

## call the collectUserInfo function inside the info_collector module
user_info = info_collector.collectUserInfo()

## save the user_info returned dictionary 
## save by calling the save_info module
result = save_user_info.saveUserInfo(user_info)

while result == "duplicate-error":
    print("This email has been used already...")
    print("Please try again!")
    user_info = info_collector.collectUserInfo()
    result = save_user_info.saveUserInfo(user_info)

    if result == "saved":
        break