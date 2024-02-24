import pywhatkit

contact = input('Enter a contact number:  ')
message = input('Enter a message to send to',contact,': ')
hours = int(input('Enter time to send message(hours): '))
minutes = int(input('Enter time to send message(minutes): '))

pywhatkit.sendwhatmsg(contact, message, hours, minutes)