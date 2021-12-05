import smtplib, ssl, sys
import getpass
import argparse
parser = argparse.ArgumentParser(description = "This is a program used to send Multiline Emails to single/multiple users. It can also be used as a Email Spammer.")
parser.add_argument('-sid',metavar="sender-email-id",type=str,help='Enter the senders email ID.',dest='sender',required=True)
parser.add_argument('-rid',metavar="--receiver-email-id",type=str,help="Enter a list of email-ids of the receivers separated by commas (,)",dest='list_of_receivers',required=True)
parser.add_argument('-sn',metavar= "--spam-number",type=int,help="Enter the number of times the email must be sent to the receivers.",dest='number_of_messages',default=1)
args = parser.parse_args()

def Email_sender(sender,list_of_receivers,password,message,number_of_messages):
    if check(sender,list_of_receivers) == 1:
        print('Sending Mail')
        for i in range(number_of_messages):
            for receiver in list_of_receivers:
                with smtplib.SMTP_SSL("smtp.gmail.com", port, context = ssl.create_default_context()) as server:
                    server.login(sender, password)
                    server.sendmail(sender,receiver,message)
                    print('Mail Sent')
    else:
        print("Incorrect email ID.")
        print("This program only supports the gmail smtp service.")
        print("Exiting")
        return 0

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

def check(sender,list_of_receivers):
    if '@gmail.com' in sender:
        pass
    else:
        return 0
    for i in list_of_receivers:
        if '@gmail.com' in i:
            pass
        else:
            return 0
    return 1

port = 465
list_of_receivers = args.list_of_receivers.split(',')
number_of_messages = args.number_of_messages
sender = args.sender
print("The sender's email address is " + str(sender))
password = getpass.getpass()
print('You are now logged in.')
print("Please enter the contents of your email in multiline format.")
print("To end the mail please press ENTER twice.")
message = entermessage()
Email_sender(sender,list_of_receivers,password,message,number_of_messages)
print('Ending Script')
