import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.MIMEImage import MIMEImage
from random import randint

# Compute 2 random numbers for Essex

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

num1 = random_with_N_digits(60)
num2 = random_with_N_digits(60)

bodyText = "Dear Dr.Essex, \n\nIs the solution \n" + str(num1) + " \nX\n" + str(num2) + " ?"
bodyText = bodyText + "\n\n Let me know, \n Dylan Harness"

mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
mail.login('<youremail>', '<password>')
numSent = 290;


def sendMail():
	while True:
	# Build and send the email to Essex
	numSent = numSent + 1
	msg = MIMEText(bodyText)
	msg['Subject'] = 'Attempt ' + str(numSent)
	msg['From'] = "<youremail>"
	msg['Reply-To'] = "<youremail>"
	msg['To'] = "aessex@uwo.ca"
	mail.sendmail('<youremail>', 'aessex@uwo.ca', msg.as_string())
	if(numSent%10==0):
		print("Sent at least " + str(numSent) + "\n")


try:
	sendMail()
except:
    print "Caught it!"



# mail.close()

