"""Test for my functions."""

from my_module.functions import has_digits

from my_module.functions import sign_up

from my_module.functions import login

##
##

def test_has_digits():
    """Tests for the `has_digits` function."""
    
    # Test a string that has no digits
    assert has_digits("no digits") == False
    
    # Test a string that has 1 digit
    assert has_digits("I have 1 digit") == True
    
    # Test a string that has more than 1 digit
    assert has_digits("I have 24 digits") == True
    
def test_sign_up():
    """Tests for the `sign_up` function."""
    
    # Test that username and password are saved into the dictionary
    assert type(sign_up()) == dict
    
def test_login():
    """Tests for the `login` function."""
    
    # Test that login function matches dictionary instead of storing key value pairs in dictionary
    assert type(login()) != dict
    



                 
    