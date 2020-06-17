"""Script to run some part of my project."""

# This adds the directory above to our Python path
#   This is so that we can add import our custom python module code into this script
import sys
sys.path.append('../')

# Imports
from my_module.functions import has_digits

from my_module.functions import sign_up

from my_module.functions import login

from my_module.test_functions import test_has_digits

from my_module.test_functions import test_sign_up

from my_module.test_functions import test_login

###
###

# PYTHON SCRIPT HERE
test_has_digits()

test_sign_up()

test_login()

print("Welcome to the website!")
    
# This code serves the purpose of the main page
if input("Do you already have an account? (yes/no)") == "yes":
    print("Please wait patiently until directed to login page.")
        
    # If an account exists, it will lead directly to login page through login function
    login()
   
else:
    print("Please wait patiently until directed to sign up page.")
        
    # If there is no account, it will ask user to signup and login
    sign_up()
    login()
pass
