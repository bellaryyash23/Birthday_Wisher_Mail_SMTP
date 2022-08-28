# 🎂Birthday Wisher Mail using SMTP of Python

🌟An automated birthday wish mail sender program which reads the list of birthdays input to it and then, checks the dates with present date. If any match
is found then formates the mail from different templates already created and cutomizes the message for respective user. Then sends the mail to the users email id using 
the SMTP module of Python language.

👉In the 'main.py' file, first the data of birthdays is read from the 'birthdays.csv' file using the pandas package. Then, the present days month and date is fetched
using the datetime module. 

👉Now, the birthday data file is itterated rowwise and for each entry the corresponding date and month is checked with preset date. Once, a match is found a random 
template from the already created letter's template is selected. 

👉This letter template is then cutomized by updating the users name in the message. After that, the SMTP module is used to create a connection with users mail id.

👉After the connection is established the sender address is fetched from the matched dataline. Then the message is formated according to proper SMTP syntax and 
the mail gets sent to the user.

👉In this way the process of birthday wisher mail is automated.

![Sample of mail sent 1](https://github.com/bellaryyash23/Birthday_Wisher_Mail_SMTP/blob/master/samples/letter1.JPG?raw=true)

👆Sample of Birthday Wisher Mail 1👆

![Sample of mail sent 2](https://github.com/bellaryyash23/Birthday_Wisher_Mail_SMTP/blob/master/samples/letter2.JPG?raw=true)

👆Sample of Birthday Wisher Mail 2👆

![Sample of mail sent 1](https://github.com/bellaryyash23/Birthday_Wisher_Mail_SMTP/blob/master/samples/letter3.JPG?raw=true)

👆Sample of Birthday Wisher Mail 3👆
