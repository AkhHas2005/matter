#Run length encoder
class RunLengthEncoder:
	message = ''
	
	def setMessage():
		message = input('Enter a string to encode: ')
		
	def encode(message):
	    encoded_message = ""
	    i = 0
	 
	    while (i <= len(message)-1):
	        count = 1
	        ch = message[i]
	        j = i
	        while (j < len(message)-1):
	            if (message[j] == message[j+1]):
	                count = count+1
	                j = j+1
	            else:
	                break
	        encoded_message=encoded_message+str(count)+ch
	        i = j+1
	    return encoded_message	
