import smtplib
import pyautogui
import pytesseract
import time

def mail(msg):
    senders_email = 'alliswell7778869@gmail.com'
    senders_password = 'efqthhbwortyfqvz'
    receiver_email = senders_email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(senders_email, senders_password)
    server.sendmail(senders_email, receiver_email, msg)


x1, y1, x2, y2 = 991, 47, 1102, 71


while True:
    time.sleep(5)
    ss = pyautogui.screenshot(region=(x1, y1, x2 - x1, y2 - y1))
    text_raw = pytesseract.image_to_string(ss)
    text = text_raw.split('.')[0]
    print(text)

    if "25" in text:
        mail("Progress 25%")

    if "50" in text:
        mail("Progress 50%")

    if "75" in text:
        mail("Progress 75%")

    if "100" in text:
        mail("Progress 100% ..terminating script")
        exit()








