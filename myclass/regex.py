import re

def isEmailValid(test_email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    if (re.fullmatch(regex, test_email)):
        return True
    else:
        return False

def test01():
    email1 = 'dhirachatchy@au.edu'
    email2 = "aaaaa"
    email3 = "admin@info.co"

    if isEmailValid(email1):
        print ('Valid!!!!')
    else:
        print ('Reject')

    if isEmailValid(email2):
        print ('Valid!!!!')
    else:
        print ('Reject')

    if isEmailValid(email3):
        print ('Valid!!!!')
    else:
        print ('Reject')

test01()
