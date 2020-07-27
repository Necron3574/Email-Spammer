# Email-Spammer
- This is a small program which sends messages to single/multiple users.  
- This script can also be used to spam messages to one/many gmail accounts.  
### Requirements  
- Python3  
### Set-up  
- Clone into this repository using `git clone https://github.com/Necron3574/Email-Spammer.git`  
- After cloning move into the email spammer directory `cd Email-Spammer` and the setup is complete.  
### Usage  
- To run the program use the command `python3 Email_spammer.py  [-sid] [-rid] [-sn]`  
- This program takes 3 arguments:  
    - [-sid], Sender ID is the email address of the account with which you want to send the emails.
    - [-rid], Receiver IDs, this is a list of all the email addresses of the accounts you want to send the email to.  
              Note that they should be separated by comma's. Ex:- `abc@gmail.com,abd@gmail.com,abe@gmail.com`
    - [-sn], Spam Number is the number of times an email should be sent to each member on the list.  
              The default is 1.
- After this you will be prompted to confirm your gmail password.
- After entering the password you will be asked to type the contents of your email.
- You can write it in a multiline format and press ENTER twice to end the mail.
- After this step the program will begin sending messages to all the people in your list.
### Example
`python3 Email_Spammer.py -sid myemail@gmail.com -rid receiver1@gmail.com,receiver2@gmail.com -sn 2`
Shell
```
The sender's email address is myemail@gmail.com
Password:
You are now logged in.
Please enter the contents of your email in multiline format.
To end the mail please press ENTER twice
Hello,
      This is a test email.
Regards


Sending Mails.
Loading...
```
At this point the program would be sending the messages.(Do not close/interrupt)  
On completion it shows the below snippet and exits.
```
Process Completed.
Ending Script.
```
### Notes
- This unfortunately only works on the Gmail interface.  
- Also this program does not support HTML entries yet. (Working on that update)  
- This program is strictly educational and the author cannot be held responsible for any illegal activities in which the script is used.  
