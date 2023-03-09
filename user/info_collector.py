def collectUserInfo():
    
    firstname = input("Enter your first name: ")
    lastname = input("Enter your last name: ")
    email = input("Enter your email address: ")

    user_info = {
        "firstname": firstname,
        "lastname": lastname,
        "email": email
    }

    return user_info

