"""A collection of function for doing my project."""

import string 
import getpass

def has_digits(value):
    """Checks whether a digit exists in a string.
    
    Parameters
    ----------
    value : string
        The string that must be checked whether a digit exist or not. 
    
    Returns
    -------
    answer : boolean
    If a digit exists, it will give True, but if a digit doesn't exist, it will give False. 
    """
    # To check  whether a digit exists in the value, it uses for loop to go through the string with isdigit() function
    answer = any(user_input.isdigit() for user_input in value)
    
    return answer



def sign_up(): 
    """Signs up for new account for the website by storing new username and password that are valid.
    
    Parameters
    ---------- 
    None
    
    Returns
    -------
    stored : dictionary
        It stores new username and password that have been verified. 
    """
    # To use stored dictionary for login function, global keyword is used
    # Since username and password must match and will most likely remain unchanged, using dictionary is the most efficient 
    global stored
    stored = {}
    
    while True:
        # Since this is a website, it must take user input with instructions on how to add a valid username
        username = input("Please choose your username with combination of lowercase letters and integers")
        
        # The if statement is necessary to make sure all lettters of the string is lowercase and string includes digits
        if username.islower() and has_digits(username) == True:
            # Since key cannot exist without a value, a preliminary value is added to be replaced after password input
            stored.update({username : "empty_password"})
            print("Username created: " + username)
            
            break
        
    
        else:
            print("Please Try again")
            
            # To make sure the loop doesn't end after invalid, username, else must be True.
            True     
    
    while True:
        # getpass function allows password input to be replaced by * for security
        password = getpass.getpass("Your password must include uppercase letters and integers")
        
        # In this case, password must include uppercase, so having all lowercase string must be false
        if  password.islower() == False and has_digits(password) == True:
            # This replaces "empty_password" as the valuefor username (key)
            stored[username] = password
            print("Password created: " + password)
            
            break
        
        else:
            print("Please Try again")
            
            True
    
    return stored 

def login():
    """login using the username and password created from signup.
    
    Parameters
    ---------- 
    None 

    
    Returns
    -------
    None 
    
    """
    while True:
        # The user must input the username they stored in signup function
        username = input("Type in you username")
        
        if username in stored:
            # If username is found in the stored dictionary, this checks for key and value pairs.
            if getpass.getpass("Type in your password") == stored[username]:
                print("Login sucessful!")
                
                break
            
            else:
                # The password value does not match provided username
                print("Invalid password")
                
                True
        else:
            # The username does not exist in stored dictionary
            print("Invalid username")
            
            True 