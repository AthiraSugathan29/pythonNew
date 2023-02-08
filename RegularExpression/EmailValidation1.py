import re

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


def check(email):
    if (re.search(regex, email)):
        print("Valid Email")
    else:
        print("Invalid Email")

mail = input("Enter the mail id : ")
check(mail)
# if __name__ == '__main__':
#     email = "rohit.gupta@mcnsolutions.net"
#     check(email)
#
#     email = "praveen@c-sharpcorner.com"
#     check(email)
#
#     email = "inform2atul@gmail.com"
#     check(email)