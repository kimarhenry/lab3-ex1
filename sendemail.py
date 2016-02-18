import smtplib

fromaddr = 'kimarhenry@gmail.com'
toaddr = 'kimarhenry@gmail.com'
message = """From: {} <{}>
To: {} <{}>
Subject: {}
{}
"""
fromname ='Kimar'
fromaddr = 'kimarhenry@gmail.com'
toname = 'Kimar'
toaddr='kimarhenry@gmail.com'
subject = 'Hello'
msg = 'This is a test email.'
messagetosend = message.format(

 fromname,
 fromaddr,
 toname,
 toaddr,
 subject,
 msg)

# Credentials (if needed)

username = 'kimarhenry@gmail.com'

password = 'nfkdxlhdicvehlez'

# The actual mail send

server = smtplib.SMTP('smtp.gmail.com:587')

server.starttls()

server.login(username,password)

server.sendmail(fromaddr, toaddr, messagetosend)

server.quit()