import smtplib, ssl
import getpass
import sys

def Email_sender(sender,list_of_recievers,password,message,number_of_messages):
    print('Loading...')
    for i in range(number_of_messages):
        for receiver in list_of_recievers:
            with smtplib.SMTP_SSL("smtp.gmail.com", port, context = ssl.create_default_context()) as server:
                server.login(sender, password)
                server.sendmail(sender,receiver,message)
    print('Process Completed.')
    print('Ending Script.')

def entermessage():
    user_writing = []
    while True:
        line = input()
        if len(line) == 0 and len(user_writing[-1]) == 0:
            break
        else:
            user_writing.append(line)
        message = '\n'.join(user_writing)
    return message

port = 465
list_of_recievers = []
sender = input('Enter your gmail username here: ')
password = getpass.getpass()

print("If you want to enter recipients manually enter 1.")
print("Else if you want to enter a list of recipients enter 2.")
print("Also if you want to spam someone's email with your account enter 3.")
print("Finally if you want to spam multiple email accounts with your account enter 4.")
choice = input()

if choice == '1':
    k = int(input('Enter number of recipients: '))
    for i in range(k):
        x = input('Enter the gmail address of receiver ' + str(i+1) + ': ')
        list_of_recievers.append(x)
    print('Now please enter the message')
    print('You can type the message in a multiline format.')
    print('To end the message press ENTER twice.')
    message = entermessage()
    Email_sender(sender,list_of_recievers,password,message,1)

elif choice == '2':
    print("Please enter the list such that the email ID's are separated by commas.")
    print("Example: reciever1@gmail.com,reciever2@gmail.com,reciever3@gmail.com")
    list_of_recievers = input("Enter list: ").split(',')
    print('Now please enter the message.')
    print('You can type the message in a multiline format.')
    print('To end the message press ENTER twice.')
    message = entermessage()
    Email_sender(sender,list_of_recievers,password,message,1)

elif choice == '3':
    print("Please enter the email address which you wish to spam.")
    print("NOTE: You will be spamming with the account with YOUR OWN email address.")
    print("The Author CANNOT be held responsible for any illegal actions with this script.")
    spam_email = input("Enter email: ")
    list_of_recievers.append(spam_email)
    print('Now please enter the message to be spammed')
    print('You can type the message in a multiline format.')
    print('To end the message press ENTER twice')
    message = entermessage()
    spam_num = int(input("Enter number of times the message should be spammed: "))
    Email_sender(sender,list_of_recievers,password,message,spam_num)

elif choice == '4':
    print("NOTE: You will be spamming with the account with YOUR OWN email address.")
    print("The Author CANNOT be held responsible for any illegal actions with this script.")
    print("Please enter the list of emails such that the email ID's are separated by commas.")
    print("Example: reciever1@gmail.com,reciever2@gmail.com,reciever3@gmail.com")
    spam_list = input("Enter list: ").split(',')
    print('Now please enter the message to be spammed')
    print('You can type the message in a multiline format.')
    print('To end the message press ENTER twice')
    message = entermessage()
    spam_num = int(input("Enter number of times the message should be spammed: "))
    Email_sender(sender,spam_list,password,message,spam_num)

else:
    print("Wrong choice please enter 1, 2, 3 or 4")
    print("Ending script.")
