'''
This program takes an email address and a string of text on the commandline
and then, using Selenium, logs into your email account and sends an email of the string
to the provided address
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os, re, sys,time
user = "your_email@gmail.com"
password = "your_password"

def sendEmail():
    #Get email address
    ToEmail = sys.argv[1]
    #Get string of text
    text = " ".join(sys.argv[2:])

    #Log into email account
    url = "https://accounts.google.com/ServiceLogin"
    browser = webdriver.Firefox()
    browser.get(url)

    emailElem = browser.find_element_by_id("Email")
    emailElem.send_keys(user)
    browser.find_element_by_id("next").click()

    time.sleep(1)
    passwordElem = browser.find_element_by_id("Passwd")
    passwordElem.send_keys(password)
    browser.find_element_by_id("signIn").click()

    #Send an email of the string to the provided address
    browser.get("https://mail.google.com/mail/u/0/#inbox?compose=new")
    time.sleep(2)
    browser.find_element_by_xpath("//textarea[@aria-label='To']").send_keys(ToEmail)
    time.sleep(2)
    browser.find_element_by_xpath("//input[@aria-label='Subject']").send_keys("Hi!")
    time.sleep(10)
    browser.find_element_by_xpath("//div[@aria-label='Message Body']").send_keys(text)
    time.sleep(5)
    browser.find_element_by_xpath("//div[contains(text(), 'Send')]").click()

sendEmail()
