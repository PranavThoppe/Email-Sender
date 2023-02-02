Please follow instructions to send use the emailsender.exe program. 


1) Unzip the file and copy it to a location on the PC

2) Open config.json and replace the following

a) Replace <sender email here> with the sender Email
b) Replace <sender password here> with the Email password
c) Replace <sender email SMTP server> with the server name

3) Open the data.csv file and enter the following information in the columns 
	Column 1 (Required field) -  Name - name of the person to whom email is sent 
	Column 2 (Required field) -  Email id - email address of person to whom email is sent (Required field)
	Column 3 (Required field) -- Subject of the email to be sent. (Required field)
	Column 4 (optional) - Content of the email to be sent. 	
		 - if ***left blank*** content or Body of the email will be picked from the Email Body.txt file. 
			This can be used to send general Broadcast message to all persons in the data.csv file. 
		 - This file can be edited too and can be found in the folder. 


4) Finally after updating the files you can run the emailSender.exe

5) The "logs" folder contains the emails sent sorted by date and time.

6) To send a new set of emails clear all the content of data.csv(except topmost row)  repeat 3)- 4) 

