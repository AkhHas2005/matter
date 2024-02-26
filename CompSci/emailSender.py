#Send an email with python
import smtplib, ssl

class emailSender:
	def __init__():
		port = 465  # For SSL
		smtp_server = "smtp.gmail.com"
		sender_email = ''
		receiver_email = ''
		password = ''
		message = ''
		
	def setDetails():
		sender_email = input("Enter your email: ")
		receiver_email = input("Enter the email you wish to send it to: ")
		password = input("Type your password and press enter: ")
		
	def setMessage():
		subject = input("Enter subject: ")
		message += 'Subject: '+subject
		body = ''
		print("Enter body of email (Enter to stop):")
		while True:
			body = input()
			if body == '':
				break
			message += body
			
	def sendEmail():
		context = ssl.create_default_context()
		with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
		    server.login(sender_email, password)
		    server.sendmail(sender_email, receiver_email, message)
    
