import re

def isValidEmail(email):

    # Regular expression for validating an Email
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
 
    if(re.fullmatch(regex, email)):
        return True
    else:
        return False

email = input("Emailinizi girin ")

if isValidEmail(email):
    username = email[0:email.index('@')]
    domain = email[email.index('@')+1: ]
    print("Kullanıcı Adı - ", username)
    print("Domain - ", domain)
else:
    print("Geçersiz Email")