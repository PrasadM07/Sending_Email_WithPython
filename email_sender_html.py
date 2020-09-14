#  SENDING EMAILS USING PYTHON
import smtplib   #smtp server needs to be estabilished first that follows smtp protocol.
from email.message import EmailMessage # email is a inbuilt Python Module
from string import Template
from pathlib import Path 

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = '' # Your Name
email['to'] = '' # email id to whom you want too send the mail
email['subject'] = 'You are so Lucky To receive this Mail'

email.set_content(html.substitute({'name': ''}), 'html') #enter the recipient's name

# developing the smtp server with the gmail
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()  #encrytion needs to estabilished with server(tls)
	smtp.login('1','2') #1.Your Email ID, 2.Your Password
	smtp.send_message(email)
	print('all Good, Mail Sent Successfully')


