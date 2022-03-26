import time
import os
from selenium import webdriver
driver = webdriver.Firefox(executable_path="C:\\Program Files\\Mozilla Firefox\\geckodriver.exe")
driver.maximize_window()
driver.get("https://play.typeracer.com/")
time.sleep(4.5)
driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/table/tbody/tr/td[3]/div/div[2]/div[1]/div[2]/a[2]").click()
driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/div/div[1]/div/table[1]/tbody/tr[2]/td/div/table/tbody/tr[1]/td[2]/input").send_keys("prophet0069")
driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/div/div[1]/div/table[1]/tbody/tr[2]/td/div/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/input").send_keys("654321")
driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/div/div[1]/div/table[1]/tbody/tr[2]/td/div/table/tbody/tr[4]/td[2]/table/tbody/tr/td[1]/button").click()
time.sleep(1.5)
driver.find_element_by_xpath("//a[@title='Keyboard shortcut: Ctrl+Alt+I']").click()
time.sleep(14.4)
times = 2      #how many times to race
for i in range(times):
    text = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/div[1]/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div").text
    print(text)
    for character in text:
        driver.find_element_by_class_name("txtInput").send_keys(character)
        time.sleep(0.11)     # the time after which each letter is typed
    if times > 1:
        time.sleep(0.5)
        driver.find_element_by_xpath("//a[@title='Keyboard shortcut: Ctrl+Alt+K']").click()
        time.sleep(13.8)
driver.close()
time.sleep(5)
os.remove("geckodriver.log")
