from email.message import EmailMessage
import ssl
import smtplib
import csv
import os
import json
import datetime


#print("path " + os.getcwd() + "\\Email Body.txt")

def emailSend(name, email, subject, content,config):

    """ path = os.getcwd() + "\\Logs"
    now = datetime.datetime.now()
    date_string = now.strftime("%Y-%m-%d")
    file_path = os.path.join(path, f"{date_string}.txt") """



    email_receiver = email
    subject = subject
    body = 'Hi ' + name + ','+ content
    print(name)
    
    email_sender = config['sender']
    email_password = config['key']
    smtp = config['smtp']
    reply =config['replyto']

    #print('email'+ '' + email_sender)
    #print('email'+ '' + smtp)
    #print('email'+ '' + reply)


    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['subject'] = subject
    em.set_content(body)
    em.add_header('reply-to', reply)


    context = ssl.create_default_context()

    with smtplib.SMTP_SSL( smtp , 465, context=context) as smtp:
       
       try:
            smtp.login(email_sender, email_password)
            logMail('Success: Email sent', email)
       except:
            message = "Could not Log in to email"
            logMail(message, email)


       try:
          smtp.sendmail(email_sender, email_receiver, em.as_string())
          logMail('Success: Email sent', email)
       except:
          message = "Email could not be sent"
          logMail(message, email)
        
    

           

def logMail(message, email):
    path = os.getcwd() + "\\logs"
    now = datetime.datetime.now()
    date_string = now.strftime("%Y-%m-%d")
    file_path = os.path.join(path, f"{date_string}.txt")
    time_string = now.strftime("%H:%M:%S")

    if os.path.isfile(file_path):
        with open(file_path, "a") as file:
            file.write(message + " for <" + email + ">: " + time_string + "\n")
    else:
        with open(file_path, "w") as file:
            file.write(message + " for <" + email + ">: " + time_string + "\n")

with open('config.json', 'r') as f:
    config = json.load(f)


with open(os.getcwd() + "\\Email Body.txt", 'r') as file:

    body = file.read()
    #print(reader)

with open(os.getcwd() + "\\data.csv", 'r') as file:

    reader = csv.reader(file)
    next(reader)
    for row in reader:
        #print(row[0])
        name = row[0]
        email = row[1]
        subject = row[2]
        if row[3] != '':
            content = row[3]
        else:
            content = body
        #print(email)
        emailSend(name, email,subject,content,config)


