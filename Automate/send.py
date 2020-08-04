import ssl,smtplib
import os,pandas
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def read_filecontent(filename):
    with open(filename, 'r') as content_file:
        content = content_file.read()
    return content


def message(subject,to_addr,from_addr):
	message = MIMEMultipart('alternative')
	message['subject'] = subject
	# message['To'] = to_addr
	message['From'] = from_addr
	message.preamble = """This message is in HTML only, which your mail reader doesn't seem to support!"""
	html_body = MIMEText(read_filecontent('body.html'), 'html')
	message.attach(html_body)
	return message.as_string()


os.chdir("C:/Users/deepa/Desktop/Automate")

# download file
file_id="1zyKt8QzmRX1swkAP2aUX7OWgwXuuVDehrjgG76Koi5U"

date=datetime.date.today()

#open file and get data
data=pandas.read_csv('data.csv')

email=data['Email']
emails=list(set(email.tolist()))

def readurl():
	with open('content/url.txt','r+') as file:
		return file.read()


#send mails

em=open("cred/email.txt",'r+')

sender=em.read()

em.close()
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
# sender_email = "my@gmail.com"  # Enter your address
# receiver_email = "your@gmail.com"  # Enter receiver address
ps=open("cred/passwd.txt",'r+')

password = ps.read()
ps.close()
url=readurl()
rw=open("content/info.txt",'r+')
info=rw.read()
rw.close()
rh=open("content/header.txt",'r+')
header=rh.read()
# print(url)
for email in emails:
	message=MIMEMultipart("alternative")
	message['Subject'] = header
	message['To'] = email
	message['From'] = sender

	html = """\
	      <body>
	 <h2>{}</h2> {}<br>	
	      <p>{}</p>
	      <br>
	<center> <a href="{}" style="text-decoration: none;color: white;background-color: black;padding: 10px;border-radius: 5px;margin-top: 10px;">Click Here</a></center>
		</body></html> """.format(header,date,info,url)
	

	html=html.replace('\n','<br>')
	part=MIMEText(html,'html')
	message.attach(part)




	context = ssl.create_default_context()
	with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
	    
	    subject="First one"
	    server.login(sender, password)
	    server.sendmail(sender,email, message.as_string())
	    server.quit()
	    print("sent to "+email)
