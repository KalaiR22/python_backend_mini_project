#get an email from the user
#split the email using split()

def email_slicer():
    print("welcome to the email slicer")
    user_email = input("Enter the mail id to slice: ")

    (username, domain) = user_email.split('@')
    (domain, extension) = domain.split('.')

    print("Username:",username)
    print("Domain:",domain)
    print("Extension:",extension)

email_slicer()

